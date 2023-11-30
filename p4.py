from utils.afficher_tour import afficher_tour
from utils.centrer import centrer
from utils.titre import centrer_couleur

def afficher_p4(jeu:list[list[str]])->None:
    """
    Procédure qui permet d'afficher proprement le jeu
        entrée : le jeu dans un tableau de tableau de chaîne de caractères
    """
    i : int
    j : int
    ligne : str

    print(centrer("\u256D\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u256E"))
    for i in range(6):
        ligne = "\u2502 "

        for j in range(0, 7):
            ligne += jeu[i][j] + " "

        ligne += "\u2502 "

        print(centrer_couleur(ligne))
    print(centrer("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518"))


def tour(joueur: str, couleur : str, jeu: list[list[str]], ligne_en_jeu:list[int], en_cours:bool)->bool:
    """
    
    """
    i : int
    j : int
    choix : int

    # test si le jeu est plein 
    if ligne_en_jeu == []:
        print("égalité")
        en_cours = False
        return en_cours

    # Choix du joueur 1
    choix = int(input(couleur + joueur + "\033[0m" + " veuillez choisir une ligne entre " + str(ligne_en_jeu) + ": "))

    while choix not in ligne_en_jeu :
        choix = int(input(couleur + joueur + "\033[0m" + " veuillez choisir une ligne entre " + str(ligne_en_jeu) + ": "))

    # Test pour savoir a quel endroit de la colonne choisie le pion dois se mettre
    if jeu[5][choix-1] == '.':
        jeu[5][choix-1] = couleur + "O\033[0m"
    else:
        i = 0
        while i >= 0 and jeu[5-i][choix-1] != ".":
            i += 1
        jeu[5-i][choix-1] = couleur + "O\033[0m"

    # test si la colonne est pleine
    if jeu[0][choix-1] != ".":
        ligne_en_jeu.remove(choix)

    # Vérification si le joueur a gagné

    ## Test ligne gagnante
    for i in range(0, 3):
        for j in range(0, 6):
            if jeu[i][j] == jeu[i+1][j] and jeu[i+2][j] == jeu[i+3][j] and jeu[i][j] == jeu[i+3][j] and jeu[i][j] != ".":
                # le joueur qui viens de jouer a gagné
                # ajout des scores
                print(joueur, "a gagné")
                en_cours = False
                return en_cours

    ## Test colonne gagnante
    for i in range(0, 6):
        for j in range(0, 3):
            if jeu[i][j] == jeu[i][j+1] and jeu[i][j+2] == jeu[i][j+3] and jeu[i][j] == jeu[i][j+3] and jeu[i][j] != ".":
                # le joueur qui viens de jouer a gagné
                # ajout des scores
                print(joueur, "a gagné")
                en_cours = False
                return en_cours

    ## Test diagonales gagnantes
    ### diagonale : haut de droite -> bas a gauche
    for i in range(0, 3):
        for j in range(0, 4):
            if jeu[i][j] == jeu[i+1][j+1] and jeu[i+2][j+2] == jeu[i+3][j+3] and jeu[i][j] == jeu[i+3][j+3] and jeu[i][j] != ".":
                # le joueur qui viens de jouer a gagné
                # ajout des scores
                print(joueur, "a gagné")
                en_cours = False
                return en_cours

    ### diagonale : haut a gauche -> bas a droite
    for i in range(0, 3):
        for j in range(0, 4):
            if jeu[i+3][j] == jeu[i+2][j+1] and jeu[i+1][j+2] == jeu[i][j+3] and jeu[i+3][j] == jeu[i][j+3] and jeu[i+3][j] != ".":
                # le joueur qui viens de jouer a gagné
                # ajout des scores
                print(joueur, "a gagné")
                en_cours = False
                return en_cours
            
    return en_cours

def main_p4(joueur1 : str, joueur2 : str)->None:
    """Procédure de point d'entrée pour le jeu de puissance 4"""

    jeu : list[list[str]]
    en_cours : bool
    nb_tour : int
    ligne_en_jeu : list[int]

    jeu = [[".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", "."]]
    
    en_cours = True
    nb_tour = 1
    ligne_en_jeu = [i for i in range(1, 8)]

    while en_cours:
        afficher_tour(nb_tour)

        afficher_p4(jeu)

        if nb_tour % 2 == 1:
            en_cours = tour(joueur1, "\033[1;33m", jeu, ligne_en_jeu, en_cours)
        else:
            en_cours = tour(joueur2, "\033[1;31m", jeu, ligne_en_jeu, en_cours)

        nb_tour += 1

    afficher_p4(jeu)


if __name__ == "__main__":
    main_p4("Maxime", "Mikkel")