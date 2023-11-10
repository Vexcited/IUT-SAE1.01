from utils.afficher_tour import afficher_tour
from utils.centrer import centrer

def afficher_morpion(morpion : list[list[str]])->None:
    """procedure qui affiche proprement le morpion
        entrée : le morpion
    """
    i : int

    # Pour la lisibilité 
    print("")

    for i in range(0,2):

        # affichage de la ligne i
        print(centrer(morpion[i][0] + " | " + morpion[i][1] + " | " + morpion[i][2]))

        # séparateur entre 2 lignes
        print(centrer("-----------"))

    # affichage de la dernière ligne
    print(centrer(morpion[2][0] + " | " + morpion[2][1] + " | " + morpion[2][2]))

def main_morpion()->None:
    """Procédure de point d'entrée pour le jeu de morpion"""
    nb_tour : int
    en_cours : bool
    morpion : list[list[str]]
    choix : int

    nb_tour = 1
    en_cours = True
    morpion =  [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]

    print("")

    print(centrer("TUTO"))

    afficher_morpion([["0","1","2"],
                      ["3","4","5"],
                      ["6","7","8"]])
    
    print("")
    
    print("A chaque case correspond un chiffre qu'il faut rentrer dans les choix pour choisir une case")

    while en_cours:
        afficher_tour(nb_tour)

        choix = int(input("Joueur " + str(((nb_tour+1) % 2)+1) + " : Veuillez choisir une case : "))

        while morpion[choix//3][choix%3] != " ":
            choix = int(input("Joueur " + str(((nb_tour+1) % 2)+1) + " : Veuillez choisir une case : "))

        if ((nb_tour+1) % 2)+1 == 1:
            morpion[choix//3][choix%3] = "O"

        if ((nb_tour+1) % 2)+1 == 2:
            morpion[choix//3][choix%3] = "X"

        afficher_morpion(morpion)
        
        # vérification de victoire
        if morpion[0][0] == morpion[1][1] == morpion[2][2] != " ":
            print("Joueur", ((nb_tour+1) % 2)+1, ":", "vous avez gagné !")
            # ajout des scores

        if morpion[0][2] == morpion[1][1] == morpion[2][0] != " ":
            print("Joueur", ((nb_tour+1) % 2)+1, ":", "vous avez gagné !")
            # ajout des scores

        for i in range(0,2):
            if morpion[i][0] == morpion[i][1] == morpion[i][2] != " ":
                print("Joueur", ((nb_tour+1) % 2)+1, ":", "vous avez gagné !")
                # ajout des scores

        for i in range(0,2):
            if morpion[0][i] == morpion[1][i] == morpion[2][i] != " ":
                print("Joueur", ((nb_tour+1) % 2)+1, ":", "vous avez gagné !")
                # ajout des scores

        nb_tour += 1

if __name__ == "__main__":
    main_morpion()