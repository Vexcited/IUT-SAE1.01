from utils.effacer_ecran import effacer_ecran
from utils.centrer import centrer


def définir_nom_joueur(index: int) -> str:
    """
    Fonction permettant de choisir un nom pour l'utilisateur {index}.
    Affiche l'utilisation en interne de ce nom d'utilisateur.

    Entrée : `index` ne peut être que `1` ou `2` (Joueur 1 ou Joueur 2)
    """

    nom_utilisateur: str

    effacer_ecran()
    print(centrer("Sélection du nom d'utilisateur du joueur " + str(index)))
    print("\nCe nom d'utilisateur est utilisé pour les scores.")
    print("C'est un nom d'utilisateur unique et sensible à la casse.\n")

    nom_utilisateur = input("-> Joueur " + str(index) + " : ")
    return nom_utilisateur
