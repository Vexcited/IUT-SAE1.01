def afficher_p4(jeu:list[list[str]])->None:
    i : int
    j : int

    print("-----------------")
    for i in range(0, 6):
        print("|", end = "")
        print(" ", end = "")

        for j in range(0, 7):
            print(jeu[i][j], end = "")
            print(" ", end = "")

        print("|", end = "")
        print("")
    print("-----------------")

def main_p4()->None:
    """Procedure de point d'entrée pour le jeu de puissance 4"""
    jeu : list[list[str]]

    jeu = [["."] * 7] * 6

    afficher_p4(jeu)


if __name__ == "__main__":
    main_p4()