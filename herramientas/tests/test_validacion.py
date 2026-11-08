"""Pruebas de fallos relevantes del validador y los datos de aceptación."""

from __future__ import annotations

import copy
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import preflight
import validar_repo as validator

ROOT = Path(__file__).resolve().parents[2]


class ValidationTests(unittest.TestCase):
    def test_repository_material_is_valid(self):
        # Las copias estudiantiles pueden tener ya un stack elegido.
        self.assertEqual(validator.validate(ROOT), [])

    def test_missing_core_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "repo"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__", "node_modules", ".venv"))
            (root / "AGENTS.md").unlink()
            self.assertTrue(any("Falta archivo obligatorio: AGENTS.md" in e for e in validator.validate(root)))

    def test_template_rejects_preselected_stack_but_student_copy_allows_it(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "package.json").write_text("{}", encoding="utf-8")
            template = validator.validate(root, template=True)
            normal = validator.validate(root)
            self.assertTrue(any("stack o app preseleccionados" in e for e in template))
            self.assertFalse(any("stack o app preseleccionados" in e for e in normal))

    def test_broken_local_link_is_rejected_and_external_link_is_skipped(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            document = root / "README.md"
            document.write_text("[web](https://example.com/)\n[roto](falta.md)\n", encoding="utf-8")
            errors = validator.local_link_errors(root, document)
            self.assertEqual(len(errors), 1)
            self.assertIn("falta.md", errors[0])

    def test_parent_link_inside_root_is_valid_and_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "docs").mkdir()
            (root / "README.md").write_text("# Hola", encoding="utf-8")
            document = root / "docs" / "a.md"
            document.write_text("[ok](../README.md)\n[escape](../../otro.md)", encoding="utf-8")
            errors = validator.local_link_errors(root, document)
            self.assertEqual(len(errors), 1)
            self.assertIn("fuera de raíz", errors[0])

    def test_frontmatter_requires_complete_metadata(self):
        with self.assertRaises(ValueError):
            validator.frontmatter("# sin frontmatter")
        with self.assertRaises(ValueError):
            validator.frontmatter("---\nname: ejemplo\n")
        with self.assertRaises(ValueError):
            validator.frontmatter("---\nname: a\nname: b\n---\n")
        self.assertEqual(validator.frontmatter("---\nreadonly: true\nmodel: inherit\n---\n"), {"readonly": True, "model": "inherit"})

    def test_schedule_rejects_gap_and_presentations_inside_work(self):
        config = validator.load_json(ROOT / "taller.json")
        self.assertEqual(validator.schedule_errors(config), [])
        broken = copy.deepcopy(config)
        broken["etapas"][2]["inicio"] += 1
        self.assertTrue(any("discontinuo" in e for e in validator.schedule_errors(broken)))
        broken = copy.deepcopy(config)
        broken["exposiciones_fuera_del_trabajo"] = False
        self.assertTrue(any("exposiciones" in e for e in validator.schedule_errors(broken)))

    def test_splitly_reference_balances_and_settlements_are_consistent(self):
        data = validator.load_json(ROOT / "retos/casos/splitly.json")
        self.assertEqual(validator.splitly_errors(data), [])

    def test_splitly_rejects_lost_cent_and_invalid_settlement(self):
        data = validator.load_json(ROOT / "retos/casos/splitly.json")
        lost = copy.deepcopy(data)
        lost["casos"][2]["gastos"][0]["partes"][0] -= 1
        self.assertTrue(any("reparto pierde céntimos" in e for e in validator.splitly_errors(lost)))
        wrong_payment = copy.deepcopy(data)
        wrong_payment["casos"][0]["liquidaciones"][0]["centimos"] = 999
        self.assertTrue(any("no dejan todos los balances a cero" in e for e in validator.splitly_errors(wrong_payment)))

    def test_bookflow_rejects_duplicate_reservation_and_failed_release(self):
        data = validator.load_json(ROOT / "retos/casos/bookflow.json")
        self.assertEqual(validator.bookflow_errors(data), [])
        duplicate = copy.deepcopy(data)
        duplicate["secuencia"][2]["reservas_activas"] = 2
        self.assertTrue(validator.bookflow_errors(duplicate))
        not_released = copy.deepcopy(data)
        not_released["secuencia"][-1]["disponible"] = False
        self.assertTrue(validator.bookflow_errors(not_released))

    def test_preflight_missing_optional_tools_does_not_claim_free_is_verified(self):
        with patch.object(preflight, "command_version", return_value={"disponible": False, "version": "No encontrado"}):
            data = preflight.inspect_environment(ROOT)
        self.assertTrue(all(data["material"].values()))
        self.assertFalse(data["herramientas"]["node_opcional"]["disponible"])
        self.assertTrue(any("cuota" in item for item in data["comprobaciones_manuales"]))


if __name__ == "__main__":
    unittest.main()
