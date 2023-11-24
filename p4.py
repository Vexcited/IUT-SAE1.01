from utils.afficher_tour import afficher_tour

def afficher_p4(jeu:list[list[str]])->None:
    i : int
    j : int

    print("\u256D\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u254C\u256E")
    for i in range(0, 6):
        print("\u2502", end = "")
        print(" ", end = "")

        for j in range(0, 7):
            print(jeu[i][j], end = "")
            print(" ", end = "")

        print("\u2502", end = "")
        print("")
    print("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518")

def main_p4(joueur1 : str, joueur2 : str)->None:
    """Procedure de point d'entrée pour le jeu de puissance 4"""

    jeu : list[list[str]]
    en_cours : bool
    nb_tour : int
    ligne_en_jeu : list[int]
    i : int
    choix : int

    jeu = [["."] * 7] * 6
    en_cours = True
    nb_tour = 1
    ligne_en_jeu = [i for i in range(1, 8)]

    while en_cours:
        afficher_tour(nb_tour)

        afficher_p4(jeu)

        # Choix du joueur 1
        choix = int(input("\033[1;33m" + joueur1 + "\033[0m" + " veuillez choisir une ligne entre " + str(ligne_en_jeu) + ": "))

        while choix not in ligne_en_jeu :
            choix = int(input("\033[1;33m" + joueur1 + "\033[0m" + " veuillez choisir une ligne entre " + str(ligne_en_jeu) + ": "))

        # Test pour savoir a quel endroit de la colonne choisie le pion dois se mettre
        for i in range(0, 7):
            if jeu[i][choix-1] == ".":
                jeu[i][choix-1] = "\033[1;33mO\033[0m"

        nb_tour += 1

        # ----------------------------------------------------------

        afficher_tour(nb_tour)

        afficher_p4(jeu)

        choix = int(input("\033[1;31m" + joueur2 + "\033[0m" + " veuillez choisir une ligne entre " + str(ligne_en_jeu) + ": "))

        while choix not in ligne_en_jeu :
            choix = int(input("\033[1;31m" + joueur2 + "\033[0m" + " veuillez choisir une ligne entre " + str(ligne_en_jeu) + ": "))

        for i in range(0, 7):
            if jeu[i][choix-1] == ".":
                jeu[i][choix-1] = "\033[1;31mO\033[0m"

        nb_tour += 1

        # en_cours = False


if __name__ == "__main__":
    main_p4("Maxime", "Mikkel")