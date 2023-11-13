from utils.effacer_ecran import effacer_ecran


def définir_nom_joueur(index: int) -> None:
    """
    Procédure permettant de choisir un nom pour l'utilisateur {index}.
    Entrée : `index` ne peut être que `1` ou `2` (Joueur 1 ou Joueur 2)
    """

    nom_utilisateur: str

    effacer_ecran()
    nom_utilisateur = input("Joueur " + str(index) +
                            " veuillez choisir un nom : ")
