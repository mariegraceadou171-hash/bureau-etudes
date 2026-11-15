"""Menu console du bureau d'études."""
from predimensionnement import cote_semelle, section_poteau


def saisir_nombre(message):
    """Demande un nombre positif à l'utilisateur, jusqu'à saisie valide."""
    while True:
        try:
            valeur = float(input(message).replace(",", "."))
            if valeur > 0:
                return valeur
            print("La valeur doit être positive.")
        except ValueError:
            print("Saisie invalide : entrez un nombre.")


def menu_semelle():
    g_plus_q = saisir_nombre("Charge G+Q en pied (kN) : ")
    print("Côté minimal de la semelle :", cote_semelle(g_plus_q), "m")


def menu_poteau():
    n_elu = saisir_nombre("Effort N_ELU (kN) : ")
    a_min, calcule, retenu = section_poteau(n_elu)
    print("A_min =", a_min, "m² | côté calculé =", calcule,
          "cm | côté retenu =", retenu, "cm")


def main():
    while True:
        print("\n--- Bureau d'études ---")
        print("1. Prédimensionner une semelle")
        print("2. Prédimensionner un poteau")
        print("0. Quitter")
        choix = input("Votre choix : ").strip()
        if choix == "1":
            menu_semelle()
        elif choix == "2":
            menu_poteau()
        elif choix == "0":
            print("Au revoir.")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()