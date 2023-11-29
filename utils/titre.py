from os import get_terminal_size

def enlever_ansi_codes(texte: str) -> str:
    """
    Fonction qui enlève les codes ANSI d'une chaîne de caractères.

    Entrée: texte avec des couleurs ANSI.
    Sortie: texte sans couleurs ANSI.
    """
    i: int
    texte_sans_ansi: str

    i = 0
    texte_sans_ansi = ""

    while i < len(texte):
        if texte[i] == "\033": # ESC
            while texte[i] != "m":
                i += 1
        else:
            texte_sans_ansi += texte[i]
        i += 1
    
    return texte_sans_ansi

def centrer_couleur(texte: str) -> str:
    # On crée une chaîne SANS les couleurs pour calculer la taille de la ligne.
    raw_texte : str
    # `pad` et `lpad` sont les espacements à gauche pour centrer le jeu en fonction de `raw_ligne`.
    pad : int
    lpad : int
    # On récupère la taille du terminal pour centrer le jeu.
    terminal_colonne: int

    raw_texte = enlever_ansi_codes(texte)
    terminal_colonne = get_terminal_size().columns
    # On calcule manuellement l'espacement pour centrer le jeu
    pad = max(0, terminal_colonne - len(raw_texte))
    lpad = (pad + 1) // 2
    rpad = pad - lpad

    return lpad * " " + texte + rpad * " "

def centrer_couleur_avec_bordures(texte: str) -> str:
    """
    Fonction qui centre le texte,
    et ajoute "│" au début et à la fin de la ligne
    """
    return "│" + centrer_couleur(texte)[1:-1] + "│"

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