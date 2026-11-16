"""Éléments de la structure (poteaux, semelles)."""
from predimensionnement import cote_semelle, section_poteau


class Poteau:
    """Un poteau avec son effort normal à l'ELU (en kN)."""

    def __init__(self, nom, n_elu):
        self.nom = nom
        self.n_elu = n_elu

    def predimensionner(self):
        """Retourne (A_min en m², côté calculé en cm, côté retenu en cm)."""
        return section_poteau(self.n_elu)


class Semelle:
    """Une semelle sous un poteau, avec la charge G+Q en pied (en kN)."""

    def __init__(self, nom, g_plus_q):
        self.nom = nom
        self.g_plus_q = g_plus_q

    def predimensionner(self):
        """Retourne le côté minimal de la semelle (en m)."""
        return cote_semelle(self.g_plus_q)