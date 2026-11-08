#!/usr/bin/env python3
"""Valida el material del taller; no ejecuta ni certifica las apps de los equipos."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
AGENTS = {"product-manager", "asesor-stack", "disenador-producto", "arquitecto", "auditor"}
SKILLS = {"extraer-design-system", "verificar-mvp"}
RULES = {"01-seguridad", "02-desarrollo", "03-producto-y-diseno"}
CORE = (
    "README.md", "AGENTS.md", "PREPARACION.md", "INICIO-RAPIDO.md", "LICENSE",
    ".gitignore", ".cursorignore", ".editorconfig", ".gitattributes",
    "taller.json", "entregables/EQUIPO.md", "entregables/ARRANQUE.md",
    "plantillas/DECISION.md", "plantillas/ERROR.md", "plantillas/DEMO.md",
    "profesor/GUIA.md", "profesor/RUBRICA.md", "profesor/VALIDACION.md",
    "profesor/CONTROL-CLASE.md", "docs/CURSOR-FREE.md", "docs/BLOQUEOS.md",
    "docs/FUENTES.md", "docs/COMPARAR-STACKS.md",
    "herramientas/preflight.py", "herramientas/validar_repo.py",
    "herramientas/tests/test_validacion.py", ".github/workflows/materiales.yml",
)


def safe_path(root: Path, relative: str) -> Path:
    """No permite que un enlace o manifiesto salga del repositorio."""
    target = (root / relative).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f"Ruta fuera del repositorio: {relative}")
    return target


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def frontmatter(text: str) -> dict[str, object]:
    """Lee el subconjunto plano de YAML usado aquí, sin dependencias externas.

    No es un parser YAML general. Se rechazan campos multilínea o estructuras
    complejas para que los metadatos del material sigan siendo fáciles de revisar.
    """
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("Falta frontmatter inicial")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("Frontmatter sin cierre") from exc
    values: dict[str, object] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([a-zA-Z][\w-]*):\s*(.+)", line)
        if not match:
            raise ValueError("Frontmatter no plano o campo sin valor")
        key, value = match.groups()
        if key in values:
            raise ValueError(f"Campo duplicado: {key}")
        if value in {"true", "false"}:
            values[key] = value == "true"
        elif value.startswith('"'):
            values[key] = json.loads(value)
        elif value.startswith("'") and value.endswith("'"):
            values[key] = value[1:-1].replace("''", "'")
        elif value.startswith(("[", "{", "|", ">")):
            raise ValueError("Usar metadatos escalares planos en este material")
        else:
            values[key] = value
    return values


def local_link_errors(root: Path, document: Path) -> list[str]:
    errors = []
    text = document.read_text(encoding="utf-8")
    # No interpretar los ejemplos de código como enlaces del documento.
    text = re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", text)
    for target in re.findall(r"!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", text):
        target = target.strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        try:
            relative = str(document.parent.relative_to(root) / unquote(parsed.path))
            resolved = safe_path(root, relative)
            if not resolved.exists():
                errors.append(f"{document.relative_to(root)}: enlace roto → {target}")
        except ValueError:
            errors.append(f"{document.relative_to(root)}: enlace fuera de raíz → {target}")
    return errors


def schedule_errors(config: dict) -> list[str]:
    errors = []
    expected_ids = ["producto", "stack", "diseno", "arquitectura", "desarrollo", "auditoria"]
    stages = config.get("etapas", [])
    if [stage.get("id") for stage in stages] != expected_ids:
        errors.append("Las etapas deben ser producto, stack, diseno, arquitectura, desarrollo y auditoria")
    previous = 0
    for stage in stages:
        start, end = stage.get("inicio"), stage.get("fin")
        if type(start) is not int or type(end) is not int or start != previous or end <= start:
            errors.append(f"Tiempo discontinuo o inválido en etapa {stage.get('id')}")
        previous = end
    if previous != 60 or config.get("trabajo_minutos") != 60:
        errors.append("El trabajo debe sumar 60 minutos")
    if config.get("exposiciones_fuera_del_trabajo") is not True:
        errors.append("Las exposiciones deben quedar fuera de los 60 minutos")
    if (config.get("estudiantes"), config.get("equipos"), config.get("personas_por_equipo")) != (16, 4, 4):
        errors.append("El taller requiere 16 estudiantes en 4 equipos de 4")
    if config.get("stack_inicial") is not None or config.get("requiere_api_key") is not False:
        errors.append("La plantilla debe ser neutral y no requerir API key")
    if config.get("coste_servicios_mvp_eur") != 0:
        errors.append("El coste de servicios del MVP debe ser 0 €")
    return errors


def splitly_errors(data: dict) -> list[str]:
    """Comprueba invariantes de los resultados de referencia, no una app."""
    errors = []
    people = data["participantes"]
    if len(people) < 2 or len(set(people)) != len(people):
        return ["Splitly: participantes de referencia inválidos"]
    if {case["id"] for case in data["casos"]} != {"S1", "S2", "S3", "S9"}:
        errors.append("Splitly: faltan casos numéricos de referencia")
    for case in data["casos"]:
        prefix = f"Splitly {case['id']}"
        paid, shares = [0] * len(people), [0] * len(people)
        for expense in case["gastos"]:
            cents, parts = expense["centimos"], expense["partes"]
            if type(cents) is not int or cents <= 0:
                errors.append(f"{prefix}: importe de referencia inválido")
            if len(parts) != len(people) or any(type(p) is not int or p < 0 for p in parts):
                errors.append(f"{prefix}: partes inválidas")
                continue
            if sum(parts) != cents or max(parts) - min(parts) > 1 or parts != sorted(parts, reverse=True):
                errors.append(f"{prefix}: reparto pierde céntimos o incumple orden estable")
            paid[people.index(expense["pagador"])] += cents
            shares = [a + b for a, b in zip(shares, parts)]
        balances = [a - b for a, b in zip(paid, shares)]
        if case["pagado"] != paid or case["parte"] != shares or case["balance"] != balances or sum(balances) != 0:
            errors.append(f"{prefix}: pagado, partes o balances incoherentes")
        remaining = list(balances)
        for payment in case["liquidaciones"]:
            payer, receiver = people.index(payment["de"]), people.index(payment["a"])
            cents = payment["centimos"]
            if type(cents) is not int or cents <= 0 or payer == receiver:
                errors.append(f"{prefix}: liquidación inválida")
            remaining[payer] += cents
            remaining[receiver] -= cents
        if any(remaining):
            errors.append(f"{prefix}: las liquidaciones no dejan todos los balances a cero")
    return errors


def bookflow_errors(data: dict) -> list[str]:
    sequence = data["secuencia"]
    expected = [(0, True), (1, False), (1, False), (1, False), (0, True), (0, True), (0, True)]
    observed = [(s["reservas_activas"], s["disponible"]) for s in sequence]
    if observed != expected:
        return ["BookFlow: secuencia de reserva, duplicado, recarga o cancelación incoherente"]
    return []


def validate(root: Path, template: bool = False) -> list[str]:
    root = root.resolve()
    errors = []
    for relative in CORE:
        if not (root / relative).is_file():
            errors.append(f"Falta archivo obligatorio: {relative}")
    try:
        config = load_json(root / "taller.json")
        errors.extend(schedule_errors(config))
        for stage in config["etapas"]:
            path = safe_path(root, stage["archivo"])
            if not path.is_file():
                errors.append(f"Falta ejercicio: {stage['archivo']}")
            else:
                label = f"{stage['inicio']:02d}–{stage['fin']:02d}"
                if label not in path.read_text(encoding="utf-8").splitlines()[0]:
                    errors.append(f"Tiempo del ejercicio no coincide con taller.json: {stage['archivo']}")
            if stage.get("agente") is not None and stage["agente"] not in AGENTS:
                errors.append(f"Agente no documentado en etapa: {stage['id']}")
        for challenge in config["retos"]:
            path = safe_path(root, challenge["ficha"])
            text = path.read_text(encoding="utf-8")
            for number in range(1, 7):
                if f"{challenge['prefijo']}-{number:02d}" not in text:
                    errors.append(f"Falta requisito {challenge['prefijo']}-{number:02d}")
            cases = load_json(safe_path(root, challenge["casos"]))
            if challenge["id"] == "splitly":
                errors.extend(splitly_errors(cases))
            elif challenge["id"] == "bookflow":
                errors.extend(bookflow_errors(cases))
            else:
                errors.append(f"Reto desconocido: {challenge['id']}")
    except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
        errors.append(f"Manifiesto o casos inválidos: {exc}")

    groups = [
        (AGENTS, ".cursor/agents", ".md", "agent"),
        (RULES, ".cursor/rules", ".mdc", "rule"),
        (SKILLS, ".cursor/skills", "/SKILL.md", "skill"),
    ]
    for names, directory, suffix, kind in groups:
        for name in sorted(names):
            path = root / directory / f"{name}{suffix}"
            try:
                content = path.read_text(encoding="utf-8")
                meta = frontmatter(content)
                if not isinstance(meta.get("description"), str) or not str(meta["description"]).strip():
                    errors.append(f"{path.relative_to(root)}: falta descripción")
                if kind in {"agent", "skill"} and meta.get("name") != name:
                    errors.append(f"{path.relative_to(root)}: nombre inconsistente")
                if kind == "agent" and meta.get("model") != "inherit":
                    errors.append(f"{path.relative_to(root)}: debe heredar el modelo")
                if kind == "agent" and name == "auditor" and meta.get("readonly") is not True:
                    errors.append("El auditor nativo debe ser readonly")
                if kind == "rule" and meta.get("alwaysApply") is not True:
                    errors.append(f"{path.relative_to(root)}: la regla debe aplicarse siempre")
                if len(content.splitlines()) > 160:
                    errors.append(f"{path.relative_to(root)}: instrucciones demasiado largas para el taller")
            except (OSError, ValueError) as exc:
                errors.append(f"{path.relative_to(root)}: {exc}")

    # Solo documentos del material: no recorrer dependencias o archivos ajenos de una app.
    docs = list(root.glob("*.md"))
    for directory in ("docs", "ejercicios", "retos", "plantillas", "entregables", "profesor", ".cursor"):
        docs.extend((root / directory).rglob("*.md"))
        docs.extend((root / directory).rglob("*.mdc"))
    for document in sorted(set(docs)):
        try:
            errors.extend(local_link_errors(root, document))
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"No se puede leer {document.relative_to(root)}: {exc}")
    if template:
        markers = (
            "package.json", "package-lock.json", "pyproject.toml", "requirements.txt",
            "Dockerfile", "render.yaml", "vite.config.js", "vite.config.ts",
            "next.config.js", "next.config.ts", "next.config.mjs", "app.py", "index.html",
        )
        for marker in markers:
            if (root / marker).exists():
                errors.append(f"Plantilla con stack o app preseleccionados: {marker}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raiz", type=Path, default=ROOT, help="Raíz del repositorio a comprobar")
    parser.add_argument("--plantilla", action="store_true", help="Comprobar además neutralidad inicial")
    args = parser.parse_args()
    errors = validate(args.raiz, args.plantilla)
    if errors:
        print(f"FAIL: {len(errors)} problema(s) en el material")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: estructura, enlaces locales, tiempos, metadatos y casos de referencia")
    if args.plantilla:
        print("PASS: neutralidad inicial de la plantilla")
    print("Alcance: material educativo. No certifica apps, funcionamiento en Cursor ni cuota Free.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
