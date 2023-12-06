from utils.afficher_tour import afficher_tour
from utils.effacer_ecran import effacer_ecran
from utils.input import demanderEntier
from utils.couleurs import gris_foncé_re, jaune_re, rouge_clair_re, couleur_joueur
from utils.titre import centrer_couleur, séparateur_avec_titre
from scores.entrée import EntréeScore
from scores.fichier import écrireScore

def afficher_morpion(morpion : list[list[str]]) -> None:
    """
    Procédure qui affiche proprement le morpionx.
    
    ## Entrée :
    - `morpion`, une liste de listes de chaînes de caractères, qui représente le morpion.
    """
    ligne_index : int
    case_index : int
    ligne: str
    case_actuelle: str

    # On ajout un saut de ligne avant le morpion. 
    print("")

    for ligne_index in range(3):
        ligne = " "

        for case_index in range(3):
            case_actuelle = morpion[ligne_index][case_index]

            # Si la case ne contient pas "X" ou "O",
            # alors on ne l'a pas rempli.
            # On va alors la griser pour montrer qu'elle peut être
            # sélectionné avec le nombre qu'elle contient.
            if (case_actuelle != "X" and case_actuelle != "O"):
                ligne += gris_foncé_re(case_actuelle)
            # O: Joueur 1
            elif (case_actuelle == "O"):
                ligne += jaune_re(case_actuelle)
            # X: Joueur 2
            elif (case_actuelle == "X"):
                ligne += rouge_clair_re(case_actuelle)

            # On n'ajoute pas le séparateur à la fin.
            if case_index != 2:
                ligne += " │ "

        ligne += " "
        print(centrer_couleur(ligne))

        # On n'affiche pas le séparateur à la fin.
        if ligne_index != 2:
            print(centrer_couleur("───┼───┼───"))

    # On ajout un saut de ligne après le morpion. 
    print("")

def estRemplie(char: str) -> bool:
    """
    Fonction qui informe si une case est remplie ou non.
    Une case est dite remplie lorsque son contenu est "X" ou "O".

    ## Entrée :
    - `char`, une chaîne de caractères, qui représente le contenu de la case.

    ## Sortie :
    Un booléen qui vaut `True` si la case est remplie, `False` sinon.
    """
    return char in ["X", "O"]

def main_morpion(joueur1: str, joueur2: str) -> None:
    """
    Procédure qui sert de point d'entrée pour le lanceur.
    C'est la procédure principale du jeu morpion.

    * Le joueur 1 jouera avec "O".
    * Le joueur 2 jouera avec "X".

    ## Entrée :

    - `joueur1`, une chaîne, qui représente le nom d'utilisateur du joueur 1.
    - `joueur2`, une chaîne, qui représente le nom d'utilisateur du joueur 2.
    """

    jeu_en_cours : bool
    égalité : bool
    nb_tour : int
    morpion : list[list[str]]
    choix : int
    joueur_actuel     : str
    adversaire_actuel : str
    # Variables utilisés dans les boucles.
    ligne_index : int
    case_index  : int

    jeu_en_cours = True
    égalité      = False
    # On commence réellement au tour 1.
    # Voir la boucle `while` en dessous.
    nb_tour = 0
    # La grille initiale quand on commence le jeu.
    morpion =  [["0","1","2"],
                ["3","4","5"],
                ["6","7","8"]]
    score = EntréeScore()
    score.type_jeu = "morpion"

    # Au début du jeu, on est au tour 1.
    joueur_actuel     = joueur1
    adversaire_actuel = joueur2

    while jeu_en_cours:
        nb_tour += 1

        # On récupère le nom du joueur qui doit jouer.
        if nb_tour % 2 == 1:
            joueur_actuel     = joueur1
            adversaire_actuel = joueur2
        else:
            joueur_actuel     = joueur2
            adversaire_actuel = joueur1

        effacer_ecran()
        afficher_tour(nb_tour)
        afficher_morpion(morpion)

        choix = demanderEntier(couleur_joueur(joueur_actuel, joueur1, joueur2) + ", veuillez choisir une case : ")

        # Si la case n'est pas dans la grille, on redemande.
        while choix < 0 or choix > 8:
            choix = demanderEntier(couleur_joueur(joueur_actuel, joueur1, joueur2) + ", veuillez choisir une case dans la grille : ")

        # Si la case choisie est déjà remplie, on redemande.
        while estRemplie(morpion[choix // 3][choix % 3]):
            choix = demanderEntier(couleur_joueur(joueur_actuel, joueur1, joueur2) + ", veuillez choisir une case non vide : ")

        if joueur_actuel == joueur1:
            morpion[choix // 3][choix % 3] = "O"
        elif joueur_actuel == joueur2:
            morpion[choix // 3][choix % 3] = "X"

        # On vérifie l'égalité.
        # Pour faire cela, on itère tout les éléments
        # et si un élément n'est pas rempli, on est sûr de ne
        # pas avoir d'égalité.
        égalité = True
        for ligne_index in range(3):
            for case_index in range(3):
                if (not estRemplie(morpion[ligne_index][case_index])):
                    égalité = False
        
        if (égalité):
            jeu_en_cours = False
        else:
            # On vérifie la diagonale de haut-gauche à bas-droite.
            if morpion[0][0] == morpion[1][1] and morpion[0][0] == morpion[2][2] and estRemplie(morpion[0][0]):
                jeu_en_cours = False

            # On vérifie la diagonale de haut-droite à bas-gauche.
            if morpion[0][2] == morpion[1][1] and morpion[0][2] == morpion[2][0] and estRemplie(morpion[0][2]):
                jeu_en_cours = False

            # On vérifie les lignes.
            for ligne_index in range(3):
                if morpion[ligne_index][0] == morpion[ligne_index][1] and morpion[ligne_index][0] == morpion[ligne_index][2] and estRemplie(morpion[ligne_index][0]):
                    jeu_en_cours = False

            # On vérifie les colonnes.
            for ligne_index in range(3):
                if morpion[0][ligne_index] == morpion[1][ligne_index] and morpion[0][ligne_index] == morpion[2][ligne_index] and estRemplie(morpion[0][ligne_index]):
                    jeu_en_cours = False

    # On affiche la nouvelle grille avant d'afficher le résultat.
    effacer_ecran()
    afficher_tour(nb_tour)
    afficher_morpion(morpion)

    if (not égalité):
        # On remplie le score.
        score.vainqueur = joueur_actuel
        score.perdant   = adversaire_actuel
        score.points    = 50
        # On ajoute le score dans le fichier binaire.
        écrireScore(score)

        # On affiche la fin de jeu.
        print(séparateur_avec_titre("FIN") + "\n")
        print(centrer_couleur(couleur_joueur(joueur_actuel, joueur1, joueur2) + " a gagné en " + str(nb_tour) + " tours et remporte " + str(score.points) + " points !"))
        print(centrer_couleur(couleur_joueur(adversaire_actuel, joueur1, joueur2) + " a perdu."))
    else:
        # On affiche la fin de jeu.
        print(séparateur_avec_titre("ÉGALITÉ") + "\n")
        print(centrer_couleur("Aucun point n'est attribué."))

    # Permet d'éviter de revenir directement au lanceur.
    input("\nAppuyez sur Entrée pour continuer...")
