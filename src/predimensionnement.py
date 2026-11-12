"""Prédimensionnement des poteaux et des semelles."""
import math

SIGMA_SOL = 200          # contrainte admissible du sol (kPa)
POIDS_SEMELLE = 12.5     # poids propre de la semelle (kN par m²)
CONTRAINTE_BETON = 10000 # contrainte retenue pour le béton (kPa) = 10 MPa
COTE_MIN_POTEAU = 20     # côté minimal d'un poteau (cm)


def cote_semelle(g_plus_q):
    """Retourne le côté minimal d'une semelle carrée (en m).

    g_plus_q : charge G+Q en pied de poteau (kN).
    B >= racine((G+Q) / (200 - 12,5)), arrondi au multiple de 0,05 m.
    """
    if g_plus_q <= 0:
        raise ValueError("La charge G+Q doit être positive.")
    b = math.sqrt(g_plus_q / (SIGMA_SOL - POIDS_SEMELLE))
    return round(math.ceil(b / 0.05) * 0.05, 2)


def section_poteau(n_elu):
    """Retourne (A_min en m², côté calculé en cm, côté retenu en cm).

    n_elu : effort normal à l'ELU (kN).
    """
    if n_elu <= 0:
        raise ValueError("N_ELU doit être positif.")
    a_min = n_elu / CONTRAINTE_BETON
    cote_calcule = round(math.sqrt(a_min) * 100)
    cote_retenu = max(COTE_MIN_POTEAU, math.ceil(cote_calcule / 5) * 5)
    return round(a_min, 3), cote_calcule, cote_retenu


if __name__ == "__main__":
    for g in (122.1, 230.1, 446.1):
        print("Semelle", g, "kN ->", cote_semelle(g), "m")
    for n in (168.4, 317.8, 616.6):
        print("Poteau", n, "kN ->", section_poteau(n))