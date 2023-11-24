from utils.effacer_ecran import effacer_ecran
from utils.centrer import centrer
from utils.titre import faire_titre

def définir_nom_joueur(index: int) -> str:
    """
    Fonction permettant de choisir un nom pour l'utilisateur {index}
    pour un jeu donné.
    On vérifie que le nom d'utilisateur ne contient pas de `;` ce
    qui pourrait poser problème lors de l'écriture dans le fichier
    des scores : `scores.dat`.

    Entrée : `index` ne peut être que `1` ou `2` (Joueur 1 ou Joueur 2)
    """

    nom_utilisateur: str
    nom_utilisateur = ""

    # Tant que l'utilisateur n'a pas entré de nom d'utilisateur
    # ou que le nom d'utilisateur contient un `;`, on redemande
    # un nom d'utilisateur.
    while nom_utilisateur == "" or ";" in nom_utilisateur:
        effacer_ecran()
        faire_titre("Nom d'utilisateur du Joueur : " + str(index))
        
        # Si l'utilisateur avait précédemment entré un nom d'utilisateur
        # contenant un `;`, on affiche un message d'avertissement.
        if ";" in nom_utilisateur:
            print(centrer("Le nom d'utilisateur ne peut pas contenir de `;` !"))

        nom_utilisateur = input("-> Joueur " + str(index) + " : ")
    
    return nom_utilisateur
