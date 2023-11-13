import json
import os
from typing import TypedDict, Union


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
    session_actuelle: Union[SessionBDD, None]
    """
    Si la session n'a pas encore été initialisée, alors cette propriété
    vaut `None`. Sinon, elle contient un dictionnaire avec les clés
    `joueur1` et `joueur2` qui contiennent les noms des joueurs.
    """


def bdd() -> RacineBDD:
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
            f.write('{ "joueurs": {}, "parties": [] }')

    # on ouvre le fichier en lecture
    with open(chemin_bdd, "r") as f:
        # on charge le contenu du fichier dans une variable
        contenu_chaîne = f.read()

    contenu = json.loads(contenu_chaîne)
    return contenu
