from typing import TypedDict, Optional  # Pour le typage
import json
import os

from joueurs.selection import définir_nom_joueur


class JoueurBDD(TypedDict):
    score: int


class PartieBDD(TypedDict):
    joueur1: str
    """
    Nom du joueur 1. Le nom correspond à la clé du dictionnaire `joueurs`
    dans la racine de la base de données, `RacineBDD`.
    """

    joueur2: str
    """
    Nom du joueur 2. Le nom correspond à la clé du dictionnaire `joueurs`
    dans la racine de la base de données, `RacineBDD`.
    """

    score1: int
    """
    Score du joueur 1 dans cette partie.
    """
    score2: int
    """
    Score du joueur 2 dans cette partie.
    """


class SessionBDD(TypedDict):
    joueur1: str
    """
    Nom du joueur 1. Le nom correspond à la clé du dictionnaire `joueurs`
    dans la racine de la base de données, `RacineBDD`.
    """

    joueur2: str
    """
    Nom du joueur 2. Le nom correspond à la clé du dictionnaire `joueurs`
    dans la racine de la base de données, `RacineBDD`.
    """


class RacineBDD(TypedDict):
    joueurs: dict[str, JoueurBDD]
    parties: list[PartieBDD]
    session_actuelle: Optional[SessionBDD]
    """
    Si la session n'a pas encore été initialisée, alors cette propriété
    vaut `None`. Sinon, elle contient un dictionnaire avec les clés
    `joueur1` et `joueur2` qui contiennent les noms des joueurs.
    """


def lire_bdd() -> RacineBDD:
    # Le contenu de la base de données en format chaîne de caractères.
    contenu_chaîne: str
    # Le contenu de la base de données en format JSON.
    contenu: RacineBDD
    # Le chemin relatif vers la base de données.
    chemin_bdd: str

    chemin_bdd = "./db.json"

    # on vérifie si le fichier existe
    if not os.path.isfile(chemin_bdd):
        # sinon, on initialize le fichier
        with open(chemin_bdd, "w") as f:
            # le json contient deux propriétés: joueurs et parties,
            # on les initialise à vide
            f.write('{ "joueurs": {}, "parties": [], "session_actuelle": null }')

    # on ouvre le fichier en lecture
    with open(chemin_bdd, "r") as f:
        # on charge le contenu du fichier dans une variable
        contenu_chaîne = f.read()

    contenu = json.loads(contenu_chaîne)
    return contenu


def écrire_bdd(contenu: RacineBDD) -> None:
    """
    Procédure qui permet d'écrire le contenu de la base de données
    dans le fichier JSON.
    """

    # Le chemin relatif vers la base de données.
    chemin_bdd: str
    chemin_bdd = "./db.json"

    # on ouvre le fichier en écriture
    with open(chemin_bdd, "w") as f:
        # on écrit le contenu dans le fichier
        f.write(json.dumps(contenu))


def initialiser_session() -> None:
    """
    Procédure qui permet d'initialiser la session.
    Elle permet d'initialiser la propriété `session_actuelle`
    du fichier JSON.
    """

    contenu_bdd: RacineBDD
    contenu_bdd = lire_bdd()

    nom_utilisateur_joueur1: str
    nom_utilisateur_joueur2: str

    # on vérifie si la session n'est pas initialisée
    if contenu_bdd["session_actuelle"] is None:
        nom_utilisateur_joueur1 = définir_nom_joueur(1)
        nom_utilisateur_joueur2 = définir_nom_joueur(2)

        # on édite le contenu récupéré de la bdd
        contenu_bdd["session_actuelle"] = {
            "joueur1": nom_utilisateur_joueur1,
            "joueur2": nom_utilisateur_joueur2
        }

        # on écrit le contenu dans le fichier
        écrire_bdd(contenu_bdd)


def supprimer_session() -> None:
    """
    Procédure qui permet de supprimer la session.
    Elle permet de supprimer la propriété `session_actuelle`
    du fichier JSON.
    """

    contenu_bdd: RacineBDD
    contenu_bdd = lire_bdd()

    # on vérifie si la session est initialisée
    if "session_actuelle" in contenu_bdd:
        # on édite le contenu récupéré de la bdd
        contenu_bdd["session_actuelle"] = None

        # on écrit le contenu dans le fichier
        écrire_bdd(contenu_bdd)
