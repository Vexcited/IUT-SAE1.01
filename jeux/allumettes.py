from utils.afficher_tour import afficher_tour
from utils.centrer import centrer

def afficher_allumettes(nb_allumettes : int)->None:
    """Procédure qui permet d'afficher le nombre d'allumettes restant en jeu
        entrée : nb_allumettes, un entier
        sortie : rien
    """
    print("")
    print(centrer("O " * nb_allumettes))
    print(centrer("| " * nb_allumettes))
    print(centrer("| " * nb_allumettes))
    print(centrer("| " * nb_allumettes))

def tour(nb_tour: int, joueur: int, nb_allumettes: int)->int:
    """Fonction qui déroule le tour d'un joueur
        entrée :    nb_tour, un entier: le nombre du tour actuel
                    joueur, un entier: le numéros du joueur
                    nb_allumettes, un entier: le nombre d'allumettes encore en jeu
        sortie :    nb_allumettes, un entier: le nombre d'allumettes encore en jeu
    """
    choix_allumettes : int
    
    # Séparateurs
    afficher_tour(nb_tour)

    afficher_allumettes(nb_allumettes)

    choix_allumettes = int(input("\nJoueur " + str(joueur) + " : Combien d'allumettes voulez vous retirer du jeu ? (1, 2 ou 3) : "))

    if choix_allumettes >= nb_allumettes:
        print("\nJoueur", joueur, "a perdu !")

        # signal de fin de jeu
        return -1

    while choix_allumettes not in (1, 2, 3):
        choix_allumettes = int(input("\nJoueur " + str(joueur) + " : Le nombre d'allumettes à retirer du jeu dois être 1, 2 ou 3 ! : "))


    return nb_allumettes - choix_allumettes



def main_allumettes()->None:
    """Procédure de point d'entrée pour le jeu d'allumettes"""

    en_cours : bool
    nb_allumettes : int
    nb_tour : int

    en_cours = True
    nb_tour = 1

    # Nombre d'allumettes au début du jeu
    nb_allumettes = 20

    while en_cours:
        # TOUR DU JOUEUR 

        nb_allumettes = tour(nb_tour, ((nb_tour+1) % 2)+1, nb_allumettes)

        if nb_allumettes == -1:
            en_cours = False
            #ajouter les scores au joueur

        # fin de tour
        nb_tour += 1

if __name__ == "__main__":
    main_allumettes()