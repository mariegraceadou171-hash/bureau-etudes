"""Tests du module de prédimensionnement (valeurs de contrôle de la slide)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from predimensionnement import cote_semelle, section_poteau


def test_semelles():
    assert cote_semelle(122.1) == 0.85
    assert cote_semelle(230.1) == 1.15
    assert cote_semelle(446.1) == 1.55


def test_poteaux():
    assert section_poteau(168.4) == (0.017, 13, 20)
    assert section_poteau(317.8) == (0.032, 18, 20)
    assert section_poteau(616.6) == (0.062, 25, 25)


def test_charge_invalide():
    try:
        cote_semelle(-5)
    except ValueError:
        return
    raise AssertionError("Une charge négative aurait dû lever une erreur.")


if __name__ == "__main__":
    test_semelles()
    test_poteaux()
    test_charge_invalide()
    print("Tous les tests passent.")