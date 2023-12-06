# Pour ce fichier, nous nous sommes basés sur la table ANSI.
# Nous avons utilisé le gist suivant : <https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007#file-colors-py>

def réinitialisation_couleur(texte: str) -> str:
    """
    Fonction qui retourne le texte en paramètre
    mais avec un code ANSI de réinitialisation de couleur à la fin.

    ## Entrée :
    - `texte`, une chaîne qui va être retournée.

    ## Sortie :
    Une chaîne de caractères qui représente le texte avec un code ANSI de réinitialisation de couleur à la fin.
    """
    return texte + "\033[0m"

def gris_foncé_re(texte: str) -> str:
    """
    Fonction qui retourne le texte en paramètre
    mais avec un code ANSI pour la couleur "gris foncé" au début
    et un code ANSI de réinitialisation de couleur à la fin.
    
    ## Entrée :
    - `texte`, une chaîne, qui représente le texte
    
    ## Sortie :
    Une chaîne de caractères qui représente le texte avec un code ANSI pour la couleur "gris foncé" au début.
    """

    return réinitialisation_couleur("\033[1;30m" + texte)

def jaune(texte: str) -> str:
    """
    Fonction qui retourne le texte en paramètre
    mais avec un code ANSI pour la couleur "jaune" au début.
    
    ## Entrée :
    - `texte`, une chaîne, qui représente le texte
    
    ## Sortie :
    Une chaîne de caractères qui représente le texte avec un code ANSI pour la couleur "jaune" au début.
    """
    return "\033[1;33m" + texte

def jaune_re(texte: str) -> str:
    """
    Fonction qui retourne le texte en paramètre
    mais avec un code ANSI pour la couleur "jaune" au début
    et un code ANSI de réinitialisation de couleur à la fin.
    
    ## Entrée :
    - `texte`, une chaîne, qui représente le texte
    
    ## Sortie :
    Une chaîne de caractères qui représente le texte avec un code ANSI pour la couleur "jaune" au début et un code ANSI de réinitialisation de couleur à la fin.
    """
    return réinitialisation_couleur(jaune(texte))

def rouge_clair(texte: str) -> str:
    """
    Fonction qui retourne le texte en paramètre
    mais avec un code ANSI pour la couleur "rouge clair" au début.
    
    ## Entrée :
    - `texte`, une chaîne, qui représente le texte
    
    ## Sortie :
    Une chaîne de caractères qui représente le texte avec un code ANSI pour la couleur "rouge clair" au début.
    """
    return "\033[1;31m" + texte

def rouge_clair_re(texte: str) -> str:
    """
    Fonction qui retourne le texte en paramètre
    mais avec un code ANSI pour la couleur "rouge clair" au début
    et un code ANSI de réinitialisation de couleur à la fin.
    
    ## Entrée :
    - `texte`, une chaîne, qui représente le texte
    
    ## Sortie :
    Une chaîne de caractères qui représente le texte avec un code ANSI pour la couleur "rouge clair" au début et un code ANSI de réinitialisation de couleur à la fin.
    """
    return réinitialisation_couleur(rouge_clair(texte))

def couleur_joueur(joueur_actuel: str, joueur1: str, joueur2: str) -> str:
    """
    On colorise le nom du joueur en fonction
    du joueur actuel.

    Utilisé dans l'affichage du nom du joueur
    actuel dans les jeux.

    # Entrées :
    - `joueur_actuel`, une chaîne, qui représente le nom du joueur actuel.
    - `joueur1`, une chaîne, qui représente le nom du joueur 1.
    - `joueur2`, une chaîne, qui représente le nom du joueur 2.

    # Sortie :
    Une chaîne de caractères qui représente le nom du joueur actuel colorisé.
    Si le joueur actuel est aucun des deux joueurs, on le retourne sans couleur.
    """

    if joueur1 == joueur_actuel:
        return jaune_re(joueur_actuel)
    elif joueur2 == joueur_actuel:
        return rouge_clair_re(joueur_actuel)
    else:
        return joueur_actuel