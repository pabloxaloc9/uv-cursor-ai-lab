"""Mide pares de colores opacos sRGB. Recibe JSON por stdin; no modifica archivos."""

import json
import math
import re
import sys


def unique_object(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError(f"Clave repetida: {key}")
        result[key] = value
    return result


def luminance(value):
    if not isinstance(value, str) or not re.fullmatch(
        r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})", value
    ):
        raise ValueError("Usa colores opacos #RGB o #RRGGBB.")
    digits = value[1:]
    if len(digits) == 3:
        digits = "".join(digit * 2 for digit in digits)
    channels = [int(digits[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * weight for c, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def measure(data):
    if not isinstance(data, dict) or set(data) != {"colores", "pares"}:
        raise ValueError("La entrada debe contener solo 'colores' y 'pares'.")
    colors, pairs = data["colores"], data["pares"]
    if not isinstance(colors, dict) or not colors:
        raise ValueError("Define al menos un color en 'colores'.")
    if any(not name.strip() for name in colors):
        raise ValueError("Los colores necesitan nombres no vacíos.")
    light = {name: luminance(value) for name, value in colors.items()}
    if not isinstance(pairs, list) or not pairs:
        raise ValueError("Define al menos una combinación en 'pares'.")
    results = []
    names = set()
    for pair in pairs:
        if not isinstance(pair, dict) or set(pair) != {"nombre", "frente", "fondo", "minimo"}:
            raise ValueError("Cada par necesita 'nombre', 'frente', 'fondo' y 'minimo'.")
        name, front, back, minimum = (pair[k] for k in ("nombre", "frente", "fondo", "minimo"))
        if not isinstance(name, str) or not name.strip() or name in names:
            raise ValueError("Los pares necesitan nombres únicos y no vacíos.")
        names.add(name)
        if any(not isinstance(token, str) or token not in light for token in (front, back)):
            raise ValueError(f"El par '{name}' utiliza un color no definido.")
        if (
            isinstance(minimum, bool)
            or not isinstance(minimum, (int, float))
            or not 1 <= minimum <= 21
        ):
            raise ValueError(f"El mínimo de '{name}' debe ser un número entre 1 y 21.")
        high, low = sorted((light[front], light[back]), reverse=True)
        ratio = (high + 0.05) / (low + 0.05)
        results.append(
            {"nombre": name, "frente": front, "fondo": back,
             "contraste": round(ratio, 4), "minimo": minimum, "cumple": ratio >= minimum}
        )
    return results


def finite_float(value):
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("El JSON contiene un número fuera de rango.")
    return number


def reject_constant(value):
    raise ValueError(f"El JSON no admite {value}.")


def main():
    try:
        data = json.load(
            sys.stdin, object_pairs_hook=unique_object,
            parse_float=finite_float, parse_constant=reject_constant,
        )
        results = measure(data)
    except (ValueError, OverflowError, RecursionError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2
    passed = all(result["cumple"] for result in results)
    print(json.dumps({"pares": results, "todos_cumplen": passed}, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
