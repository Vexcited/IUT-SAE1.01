from utils.titre import séparateur_avec_titre

def afficher_tour(tour: int) -> None:
    """
    Procédure qui affiche le numéro du tour donné en paramètre.
    
    ## Entrée :
    - tour : entier qui représente le numéro du tour à afficher.
    """
    print(séparateur_avec_titre("Tour " + str(tour)))