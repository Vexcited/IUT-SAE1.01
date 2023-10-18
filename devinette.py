from getpass import getpass

def main_devinette()->None:
    """Procédure de point d'entrée pour le jeu de devinette"""
    nombre_mystere : int
    en_cours : bool
    proposition : int
    limite : int
    min : int

    min = 1
    limite = 100
    en_cours = True

    # Le joueur 2 doit trouver le nombre qui se trouve entre min et limite
    nombre_mystere = int(getpass("Joueur 1 : Choisissez le nombre à trouver pour le jeu : "))


    while en_cours :
        proposition = int(input("Joueur 2 : Veuillez choisir un nombre entre " + str(min) + "et " + str(limite) + " : "))
        while not proposition <= limite :
            proposition = int(input("Joueur 2 : Votre proposition dois être entre " + str(min) + "et " + str(limite) + " : "))
        
        reponse = input("\nJoueur 1 : Votre réponse (trop petit, trop grand ou c'est gagné) : ")
        
        # ANTI CHEAT
        if reponse == "trop petit" and not proposition < nombre_mystere :
            print("Joueur 1 : Vous avez triché !")
            #terminer le jeu et ajouter les scores au joueur 2

        elif reponse == "trop grand" and not proposition > nombre_mystere :
            print("Joueur 1 : Vous avez triché !")
            #terminer le jeu et ajouter les scores au joueur 2

        elif reponse == "c'est gagné" and not proposition == nombre_mystere :
            print("Joueur 1 : Vous avez triché !")
            #terminer le jeu et ajouter les scores au joueur 2

        else :
            if reponse == "trop petit":
                min = proposition
            if reponse == "trop grand":
                limite = proposition
            if reponse == "c'est gagné":
                #terminer le jeu et ajouter les scores au joueur 2

if __name__ == "__main__":
    main_devinette()