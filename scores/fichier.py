from typing import BinaryIO
import pickle
import os

from scores.entrée import EntréeScore

def lireScores() -> list[EntréeScore]:
    """
    Fonction qui lit les scores dans le fichier `scores.bin` et retourne la liste des
    scores contenus dans celui-ci.
  
    ## Sortie :
    Une liste des scores enregistrés (`list[EntréeScore]`) dans le fichier `scores.bin`.
    """
    fichier         : BinaryIO
    fdf             : bool
    entrée_actuelle : EntréeScore
    scores          : list[EntréeScore]

    # On vérifie que le fichier `scores.bin` existe.
    # Si le fichier n'existe pas, on le crée.
    if not os.path.exists("scores/scores.bin"):
        fichier = open("scores/scores.bin", "wb")
        fichier.close()
    
    # Ouvre le fichier `scores.bin` en lecture
    # dans le dossier `scores` à la racine du projet.
    fichier = open("scores/scores.bin", "rb")
    fdf = False

    # On initialise la liste des scores.
    scores = []
    
    while not fdf:
        try:
            # On rentre les valeurs dans une entrée de score.
            entrée_actuelle = pickle.load(fichier, encoding="utf-8")
            scores.append(entrée_actuelle)
        except EOFError:
            fdf = True

    fichier.close()
    return scores

def écrireScore(entrée: EntréeScore) -> None:
    """
    Procédure qui écrit une entrée de score dans le fichier `scores.bin`
    
    ## Entrée :
    - `entrée` une instance de la classe `EntréeScore` qui représente une entrée de score que l'on veut ajouter dans le fichier des scores.
    """
    fichier: BinaryIO

    # On ouvre le fichier `scores.bin` en mode ajout.
    fichier = open("scores/scores.bin", "ab")
    # On écrit l'entrée de score dans le fichier.
    pickle.dump(entrée, fichier)
    fichier.close()

def scoresPourJeu(type_jeu: str) -> list[EntréeScore]:
    """
    Fonction qui retourne une liste des scores enregistrés pour un jeu donné.

    ## Entrée :
    - `type_jeu` (str): Le type de jeu peut être `"devinette"`, `"allumettes"`, `"morpion"` ou `"puissance_4"`.
    """
    original_scores: list[EntréeScore]
    # Les scores qui nous intéressent vraiment.
    scores: list[EntréeScore]
    entrée: EntréeScore

    # On récupère tous les scores.
    original_scores = lireScores()

    scores = []
    for entrée in original_scores:
        # On ne garde que les scores du jeu demandé.
        if entrée.type_jeu == type_jeu:
            scores.append(entrée)

    return scores