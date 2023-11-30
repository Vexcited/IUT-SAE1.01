from getpass import getpass

def demanderEntier(message: str, estCaché: bool = False) -> int:
    """
    Demande un entier à l'utilisateur et le renvoie.

    ## Entrée:
        message (str): Message à afficher à l'utilisateur.
        estCaché (bool): Si `True`, le message sera caché à l'utilisateur, en utilisant "getpass".
        
    ## Sortie:
        int: Entier saisi par l'utilisateur.
        Si l'utilisateur ne saisit pas un entier, la fonction retourne `-1`.
    """

    valeur : int

    try:
        if (estCaché):
            valeur = int(getpass(message))
        else:
            valeur = int(input(message))        
    except ValueError:
        valeur = -1

    return valeur
    