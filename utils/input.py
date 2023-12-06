from getpass import getpass

def demanderEntier(message: str, estCaché: bool = False) -> int:
    """
    Demander un entier à l'utilisateur et le renvoie.
    Renvoie `-1` si l'utilisateur ne saisit pas un entier.

    ## Entrées :
    - message (str): Message à afficher à l'utilisateur.
    - estCaché (bool): Si `True`, le message sera caché à l'utilisateur, en utilisant "getpass".
        
    ## Sortie :
    L'entier saisi par l'utilisateur.
    Si l'utilisateur ne saisit pas un entier, la fonction retourne `-1`.
    La valeur `-1` est donc à traiter comme une erreur, pour ensuite redemander l'entier à l'utilisateur.
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
    