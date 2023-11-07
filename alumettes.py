import os

from utils.centrer import centrer

def affichier_alumettes(nb_alumettes : int)->None:
    """Procédure qui permet d'afficher le nombre d'alumettes restant en jeu
        entrée : nb_alumettes, un entier
        sortie : rien
    """
    print("")
    print(centrer("O " * nb_alumettes))
    print(centrer("| " * nb_alumettes))
    print(centrer("| " * nb_alumettes))
    print(centrer("| " * nb_alumettes))



def tour(nb_tour: int, joueur: int, nb_alumettes: int)->int:
    """Fonction qui déroule le tour d'un joueur
        entrée :    nb_tour, un entier: le nombre du tour actuel
                    joueur, un entier: le numéros du joueur
                    nb_alumettes, un entier: le nombre d'alumettes encore en jeu
        sortie :    nb_alumettes, un entier: le nombre d'alumettes encore en jeu
    """
    choix_alumettes : int
    
    # Separateurs
    print("\n"+"-"*((os.get_terminal_size().columns//2)-4), "TOUR", nb_tour, "-"*((os.get_terminal_size().columns//2)-4))

    affichier_alumettes(nb_alumettes)

    choix_alumettes = int(input("\nJoueur " + str(joueur) + " : Combien d'alumettes voulez vous retirer du jeu ? (1, 2 ou 3) : "))

    if choix_alumettes >= nb_alumettes:
        print("\nJoueur", joueur, "a perdu !")

        # signal de fin de jeu
        return -1

    while choix_alumettes not in (1, 2, 3):
        choix_alumettes = int(input("\nJoueur " + str(joueur) + " : Le nombre d'alumettes à retirer du jeu dois être 1, 2 ou 3 ! : "))


    return nb_alumettes - choix_alumettes



def main_alumettes()->None:
    """Procédure de point d'entrée pour le jeu d'alumettes"""

    en_cours : bool
    nb_alumettes : int
    nb_tour : int

    en_cours = True
    nb_tour = 1


    # Nombre d'alumettes au début du jeu
    nb_alumettes = 20

    while en_cours:
        # TOUR DU JOUEUR 

        nb_alumettes = tour(nb_tour, ((nb_tour+1) % 2)+1, nb_alumettes)

        if nb_alumettes == -1:
            en_cours = False
            #ajouter les scores au joueur

        # fin de tour
        nb_tour += 1

if __name__ == "__main__":
    main_alumettes()