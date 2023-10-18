from getpass import getpass
import os

def main_devinette()->None:
    """Procédure de point d'entrée pour le jeu de devinette"""
    nombre_mystere : int
    en_cours : bool
    proposition : int
    limite : int
    min : int
    nb_tour : int

    min = 1
    limite = 100
    nb_tour = 1
    en_cours = True

    # Le joueur 2 doit trouver le nombre qui se trouve entre min et limite
    nombre_mystere = int(getpass("Joueur 1 : Choisissez le nombre à trouver pour le jeu : "))


    while en_cours :
        # Separateurs
        print("\n"+"-"*((os.get_terminal_size().columns//2)-4), "TOUR", nb_tour, "-"*((os.get_terminal_size().columns//2)-4))

        # Proposition
        proposition = int(input("\nJoueur 2 : Veuillez choisir un nombre entre " + str(min) + " et " + str(limite) + " : "))
        while not proposition <= limite and proposition >= min:
            proposition = int(input("\nJoueur 2 : Votre proposition dois être entre " + str(min) + " et " + str(limite) + " : "))
        
        reponse = input("\nJoueur 1 : Votre réponse (trop petit, trop grand ou c'est gagné) : ").strip()
        
        # ANTI CHEAT
        if reponse == "trop petit" and not proposition < nombre_mystere :
            print("Joueur 1 : Vous avez triché !")
            #terminer le jeu et ajouter les scores au joueur 2
            en_cours = False

        elif reponse == "trop grand" and not proposition > nombre_mystere :
            print("Joueur 1 : Vous avez triché !")
            #terminer le jeu et ajouter les scores au joueur 2
            en_cours = False

        elif reponse == "c'est gagné" and not proposition == nombre_mystere :
            print("Joueur 1 : Vous avez triché !")
            #terminer le jeu et ajouter les scores au joueur 2
            en_cours = False

        else :
            if reponse == "trop petit":
                min = proposition
            if reponse == "trop grand":
                limite = proposition
            if reponse == "c'est gagné":
                # ajouter les scores au joueur 2
                en_cours = False
        
        nb_tour += 1
                

if __name__ == "__main__":
    main_devinette()