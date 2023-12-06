from os import get_terminal_size

def enlever_ansi_codes(texte: str) -> str:
    """
    Fonction qui enlève les codes ANSI d'une chaîne de caractères.

    ## Entrée :
    - `texte` avec des couleurs ANSI.
    
    ## Sortie :
    `texte` mais sans couleurs ANSI.
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
    """
    Fonction qui centre le texte donné en paramètre,
    mais contrairement à `str.center`, cette fonction prend en compte les codes ANSI de couleur.

    ## Entrée :
    - `texte` avec des couleurs ANSI.

    ## Sortie :
    `texte` centré en gardant les codes ANSI de couleur, sans décalage dans l'interface.
    """

    # Chaîne **sans** les couleurs pour ensuite récupérer la longueur de la ligne.
    raw_texte : str
    # `pad` et `lpad` sont les espacements à gauche pour centrer le jeu en fonction de `raw_ligne`.
    pad : int
    lpad : int
    # On récupère la largeur du terminal pour centrer le jeu.
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
    et ajoute "│" au début et à la fin de la ligne.

    ## Entrée :
    - `texte` avec des couleurs ANSI.

    ## Sortie :
    `texte` centré en gardant les codes ANSI de couleur, sans décalage dans l'interface,
    avec une bordure de chaque côté/extrémité.
    """
    return "│" + centrer_couleur(texte)[1:-1] + "│"

def centrer_avec_bordures(texte: str) -> str:
    """
    Fonction qui centre le texte,
    et ajoute "│" au début et à la fin de la ligne.

    ## Entrée :
    - `texte` **sans** couleurs ANSI.

    ## Sortie :
    `texte` centré sans couleurs ANSI avec une bordure de chaque côté/extrémité.
    """
    largeur: int
    largeur = get_terminal_size().columns - 2
    return "│" + str.center(texte, largeur) + "│"

def séparateur_avec_bordures_vers_haut() -> str:
    """
    Fonction qui retourne une ligne de séparation
    avec des bordures de chaque côté qui sont inclinées vers le haut.

    ## Sortie :
    Une chaîne de caractères qui représente une ligne de séparation avec
    des bordures de chaque côté qui sont inclinées vers le haut.
    """
    largeur: int
    largeur = get_terminal_size().columns - 2
    return "╰" + ("─" * largeur) + "╯"

def séparateur_avec_titre(texte: str) -> str:
    """
    Fonction qui retourne une ligne de séparation
    avec un titre au milieu.

    ## Entrée :
    - `texte` **sans** couleurs ANSI.

    ## Sortie :
    Une chaîne de caractères qui représente une ligne de séparation avec
    un titre au milieu.
    """
    largeur: int
    largeur = get_terminal_size().columns
    return str.center(" " + texte + " ", largeur, "─")

def faire_titre(titre: str, bas_arrondis : bool = True) -> None:
    """
    Procédure qui affiche un titre centré avec des bordures tout autour.

    ## Entrée :
    - `titre` **sans** couleurs ANSI.
    - `bas_arrondis` (bool): Si `True`, le bas du titre sera arrondi, sinon, il sera plat.
    """
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
        # On utilise cela pour avoir, par exemple, plusieurs sous titres.
        print("├", "─" * largeur, "┤", sep="")

def séparer_avec_bordures_plates() -> None:
    """
    Procédure qui affiche une ligne de séparation avec des bordures plates.
    """
    largeur_ecran: int
    largeur_ecran = get_terminal_size().columns

    print("\n", "─" * largeur_ecran, "\n", sep="")