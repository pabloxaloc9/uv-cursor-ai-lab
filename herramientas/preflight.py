#!/usr/bin/env python3
"""Inventario opcional y de solo lectura. No instala ni modifica nada."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def command_version(command: str, arguments: list[str]) -> dict:
    executable = shutil.which(command)
    if not executable:
        return {"disponible": False, "version": "No encontrado"}
    try:
        result = subprocess.run(
            [executable, *arguments], capture_output=True, text=True,
            timeout=8, check=False, encoding="utf-8", errors="replace",
        )
        output = (result.stdout or result.stderr).strip().splitlines()
        return {"disponible": result.returncode == 0, "version": output[0] if output else "Sin versión legible"}
    except (OSError, subprocess.TimeoutExpired):
        return {"disponible": False, "version": "No se pudo comprobar"}


def inspect_environment(root: Path) -> dict:
    return {
        "raiz": str(root.resolve()),
        "material": {name: (root / name).exists() for name in ("README.md", "AGENTS.md", ".cursor/rules", ".cursor/agents", ".cursor/skills", "taller.json")},
        "herramientas": {
            "git": command_version("git", ["--version"]),
            "node_opcional": command_version("node", ["--version"]),
            "npm_opcional": command_version("npm", ["--version"]),
            "python_para_este_script": {"disponible": True, "version": sys.version.split()[0]},
            "cursor_cli_opcional": {"disponible": shutil.which("cursor") is not None, "version": "Presencia en PATH; no comprueba la aplicación abierta"},
        },
        "comprobaciones_manuales": [
            "Cursor abierto y autenticado con cuenta propia que figure realmente como Free, no trial",
            "Modelo disponible y Agent responde; comprobar cuota cerca de la fecha de clase",
            "Lectura efectiva de AGENTS.md y reglas; adjuntar rol si no carga nativamente",
            "Adjuntos de capturas y skills; ruta alternativa si no están disponibles",
            "Copia propia GitHub, navegador y entorno del stack que se decida",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Salida estructurada para el profesor")
    parser.add_argument("--raiz", type=Path, default=ROOT)
    args = parser.parse_args()
    data = inspect_environment(args.raiz)
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print("Inventario local del taller; no valida la cuenta ni cuota de Cursor.")
        for name, present in data["material"].items():
            print(f"{'OK' if present else 'FALTA'} material: {name}")
        for name, result in data["herramientas"].items():
            print(f"{'DISPONIBLE' if result['disponible'] else 'NO DETECTADO'} {name}: {result['version']}")
        print("Node/npm y la CLI de Cursor son opcionales; su ausencia no impone otro stack.")
        print("Comprobar manualmente:")
        for item in data["comprobaciones_manuales"]:
            print(f"- {item}")
    return 0 if all(data["material"].values()) else 1


if __name__ == "__main__":
    sys.exit(main())
