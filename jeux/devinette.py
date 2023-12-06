from utils.afficher_tour import afficher_tour
from utils.input import demanderEntier
from scores.entrée import EntréeScore
from scores.fichier import écrireScore
from utils.effacer_ecran import effacer_ecran
from utils.couleurs import gris_foncé_re, jaune_re, rouge_clair_re
from utils.titre import centrer_couleur, séparateur_avec_titre

def calcul_points(nombre_tour : int) -> int:
    """
    Fonction qui calcule les points du joueur 2 en fonction du nombre de tours.

    ## Entrée :
    - `nombre_tour`, un entier, qui représente le nombre de tours que le joueur 2 a mis pour gagner.

    ## Sortie :
    Un entier qui représente le nombre de points que le joueur 2 a gagné.
    """

    points : int
    points = int(1000 // (nombre_tour ** 2))
    
    return points


def main_devinette(joueur1: str, joueur2: str) -> None:
    """
    Procédure qui sert de point d'entrée pour le lanceur.
    C'est la procédure principale du jeu devinette.

    ## Entrées :

    - `joueur1`, une chaîne, qui représente le nom d'utilisateur du joueur 1.
    - `joueur2`, une chaîne, qui représente le nom d'utilisateur du joueur 2.
    """

    nombre_mystère : int
    proposition : int
    réponse : str
    min : int
    max : int
    nombre_tour : int
    jeu_en_cours : bool
    triche: bool
    score : EntréeScore

    min = 1
    max = 100 # On défini la limite du nombre mystère
    nombre_tour = 0 # Par défaut, on veut continuer le jeu.
    réponse = ""
    jeu_en_cours = True
    triche = False
    score = EntréeScore()
    score.perdant = joueur1 # Dans ce jeu, le joueur 1 est **toujours** le perdant.
    score.vainqueur = joueur2 # Dans ce jeu, le joueur 2 est **toujours** le vainqueur.
    score.type_jeu = "devinette"

    # On demande au joueur 1 de sélectionner le nombre mystère
    # que le joueur 2 devra trouver entre 1 et 100
    nombre_mystère = demanderEntier(jaune_re(joueur1) + ", choisissez le nombre mystère (entre 1 et 100) que " + joueur2 + " devra trouver : " + gris_foncé_re("(caché) "), True)

    while not (1 <= nombre_mystère <= 100):
        nombre_mystère = demanderEntier(jaune_re(joueur1) + ", le nombre mystère doit être entre 1 et 100, réessayez : " + gris_foncé_re("(caché) "), True)

    while jeu_en_cours:
        nombre_tour += 1

        effacer_ecran()
        afficher_tour(nombre_tour)

        # Proposition
        proposition = demanderEntier("\n" + rouge_clair_re(joueur2) + ", veuillez choisir un nombre entre " + str(min) + " et " + str(max) + " : ")
        # Si on donne une proposition en dehors des limites, on redemande une proposition.
        while not (proposition <= max and proposition >= min):
            proposition = demanderEntier("\n" + rouge_clair_re(joueur2) + ", votre proposition doit être entre " + str(min) + " et " + str(max) + " : ")
        
        while réponse != "trop petit" and réponse != "trop grand" and réponse != "c'est gagné":
            # On utilise .strip pour enlever les espaces avant et après la réponse.
            réponse = input("\n" + jaune_re(joueur1) + ", votre réponse (répondez par 'trop petit', 'trop grand' ou 'c'est gagné') : ").strip().lower()
        
        # ANTI-CHEAT
        if réponse == "trop petit" and not proposition < nombre_mystère :
            triche = True
            jeu_en_cours = False

        elif réponse == "trop grand" and not proposition > nombre_mystère :
            triche = True
            jeu_en_cours = False

        elif réponse == "c'est gagné" and not proposition == nombre_mystère :
            triche = True
            jeu_en_cours = False

        else:
            if réponse == "trop petit":
                min = proposition + 1
            if réponse == "trop grand":
                max = proposition - 1
            if réponse == "c'est gagné":
                jeu_en_cours = False
        
        réponse = ""

    if not triche:
        # On remplie le score.
        score.points    = calcul_points(nombre_tour)
        # On ajoute le score dans le fichier binaire.
        écrireScore(score)

        # On affiche la fin de jeu.
        print("\n" + séparateur_avec_titre("FIN") + "\n")
        print(centrer_couleur(rouge_clair_re(joueur2) + " a gagné en " + str(nombre_tour) + " tour(s) et remporte " + str(score.points) + " points !"))
    # S'il y a eu triche...
    else:
        # On affiche la fin de jeu.
        print("\n" + séparateur_avec_titre("TRICHE") + "\n")
        print(rouge_clair_re(joueur2) + ", vous avez gagné mais aucun point ne vous est attribué.")
        print(centrer_couleur("Aucun point n'est attribué."))

    # Permet d'éviter de revenir directement au lanceur.
    input("\nAppuyez sur Entrée pour continuer...")