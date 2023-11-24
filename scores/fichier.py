from typing import TextIO
import os

from scores.entrée import EntréeScore, entréeScoreEnChaîne

def lireScores() -> list[EntréeScore]:
    """Retourne une liste des scores enregistrés dans le fichier `scores.dat`."""
    fichier         : TextIO
    ligne           : str
    valeurs_ligne   : list[str]
    entrée_actuelle : EntréeScore
    scores          : list[EntréeScore]

    # On vérifie que le fichier `scores.dat` existe.
    # Si le fichier n'existe pas, on le crée.
    if not os.path.exists("scores/scores.dat"):
        fichier = open("scores/scores.dat", "w")
        fichier.close()
    
    # Ouvre le fichier `scores.dat` en lecture
    # dans le dossier `scores` à la racine du projet.
    fichier = open("scores/scores.dat", "r")
    # On lit la première ligne.
    ligne = fichier.readline()

    # On initialise la liste des scores.
    scores = []
    
    # Chaque ligne est constituée de 4 valeurs séparées par des points-virgules
    #   -> Raison pour laquelle l'utilisateur ne peut pas utiliser ce caractère dans son nom d'utilisateur.
    # La première valeur est le type de jeu joué.
    # La deuxième valeur est le nom d'utilisateur du vainqueur.
    # La troisième valeur est le nom d'utilisateur du perdant.
    # La quatrième valeur est le nombre de points gagnés par le vainqueur.
    while ligne != "":
        valeurs_ligne = ligne.split(";")
        
        # On rentre les valeurs dans une entrée de score.
        entrée_actuelle = EntréeScore()
        entrée_actuelle.type_jeu = valeurs_ligne[0]
        entrée_actuelle.vainqueur = valeurs_ligne[1]
        entrée_actuelle.perdant = valeurs_ligne[2]
        entrée_actuelle.points = int(valeurs_ligne[3])

        # On ajoute l'entrée de score à la liste des scores.
        scores.append(entrée_actuelle)

        # On lit la ligne suivante
        # afin de ne pas rester bloqué dans la boucle.
        ligne = fichier.readline()

    fichier.close()
    return scores

def écrireScore(entrée: EntréeScore):
    """Écrit l'entrée de score dans le fichier `scores.dat`"""
    fichier: TextIO

    # On ouvre le fichier `scores.dat` en mode ajout.
    fichier = open("scores/scores.dat", "a")
    # On écrit l'entrée de score dans le fichier.
    fichier.write(entréeScoreEnChaîne(entrée) + "\n")
    fichier.close()

def scoresPourJeu(type_jeu: str) -> list[EntréeScore]:
    """
    Retourne une liste des scores enregistrés pour un jeu donné.
    Le type de jeu peut être `"devinette"`, `"allumettes"`, `"morpion"` ou `"puissance_4"`.
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