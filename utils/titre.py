from os import get_terminal_size

def centrer_avec_bordures(texte: str) -> str:
    """
    Fonction qui centre le texte,
    et ajoute "│" au début et à la fin de la ligne
    """
    largeur: int
    largeur = get_terminal_size().columns - 2
    return "│" + str.center(texte, largeur) + "│"

def séparateur_avec_bordures_vers_haut() -> str:
    largeur: int
    largeur = get_terminal_size().columns - 2
    return "╰" + ("─" * largeur) + "╯"

def séparateur_avec_titre(texte: str) -> str:
    largeur: int
    largeur = get_terminal_size().columns
    return str.center(" " + texte + " ", largeur, "─")

def faire_titre(titre: str, bas_arrondis : bool = True) -> None:
    largeur: int
    lignes: list[str]
    ligne: str

    largeur = get_terminal_size().columns - 2

    print("╭", "─" * largeur, "╮", sep="")

    lignes = titre.split("\n")
    for ligne in lignes:
        print(centrer_avec_bordures(ligne))
        
    if bas_arrondis:
        print(séparateur_avec_bordures_vers_haut(), end="\n\n")
    else:
        print("├", "─" * largeur, "┤", sep="")

def séparer_avec_bordures_plates() -> None:
    largeur_ecran: int
    largeur_ecran = get_terminal_size().columns

    print("\n", "─" * largeur_ecran, "\n", sep="")