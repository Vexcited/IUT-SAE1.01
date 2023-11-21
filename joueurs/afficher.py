from joueurs.session import lire_bdd, RacineBDD

def nom_joueur (id: int) -> str:
    """
    Fonction qui permet d'afficher le nom de l'utilisateur du joueur {id} à la
    place d'afficher seulement "Joueur {id} : ...". 
    """
    contenu_bdd : RacineBDD
    contenu_bdd = lire_bdd()

    nom_utilisateur_joueur : str
    nom_utilisateur_joueur = ""

    if contenu_bdd["session_actuelle"] is not None:
        if id == 1:
            nom_utilisateur_joueur = contenu_bdd["session_actuelle"]["joueur1"]
        else:
            if id == 2:
                nom_utilisateur_joueur = contenu_bdd["session_actuelle"]["joueur2"]

    return nom_utilisateur_joueur