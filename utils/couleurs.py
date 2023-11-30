# Pour ce fichier, nous nous sommes basés sur la table ANSI.
# Nous avons utilisé le gist suivant : <https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007#file-colors-py>

def réinitialisation_couleur(texte: str) -> str:
    return texte + "\033[0m"

def gris_foncé(texte: str) -> str:
    """
    Fonction qui retourne le texte en paramètre
    mais avec un code ANSI au début.
    
    ## Entrée :
    - `texte`, une chaîne, qui représente le texte
    """

    return réinitialisation_couleur("\033[1;30m" + texte)

def jaune(texte: str) -> str:
    return réinitialisation_couleur("\033[1;33m" + texte)

def rouge_clair(texte: str) -> str:
    return réinitialisation_couleur("\033[1;31m" + texte)

def couleur_joueur(joueur_actuel: str, joueur1: str, joueur2: str) -> str:
    """
    On colorise le nom du joueur en fonction
    du joueur actuel.

    Utilisé dans l'affichage du nom du joueur
    actuel dans les jeux.
    """

    if joueur1 == joueur_actuel:
        return jaune(joueur_actuel)
    elif joueur2 == joueur_actuel:
        return rouge_clair(joueur_actuel)
    else:
        return joueur_actuel