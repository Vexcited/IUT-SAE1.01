from utils.effacer_ecran import effacer_ecran
from utils.titre import faire_titre

def définir_nom_joueur(index: int) -> str:
    """
    Fonction permettant de choisir un nom pour l'utilisateur {index}
    pour un jeu donné.

    Entrée : `index` ne peut être que `1` ou `2` (Joueur 1 ou Joueur 2)
    """

    nom_utilisateur: str
    nom_utilisateur = ""

    # Tant que l'utilisateur n'a pas entré de nom d'utilisateur,
    # on redemande un nom d'utilisateur.
    while nom_utilisateur == "":
        effacer_ecran()
        faire_titre("Nom d'utilisateur du Joueur : " + str(index))

        nom_utilisateur = input("-> Joueur " + str(index) + " : ")
    
    return nom_utilisateur
