from getpass import getpass
from utils.afficher_tour import afficher_tour
from joueurs.afficher import nom_joueur

def calcul_score(nombre_tour : int) -> int:
    """
    Calcule le score du joueur 2 en fonction du nombre de tours.
    Si 
    """

    score : int

    # Vu que l'on peut avoir un nombre de tour de 1 à 100,
    # on peut calculer le score en soustrayant le nombre de
    # tour au nombre 100.
    score = 100 - nombre_tour
    return score


def main_devinette() -> None:
    """
    Procédure de point d'entrée pour le jeu de devinette.
    """

    nombre_mystère : int
    proposition : int
    réponse : str
    min : int
    max : int
    nombre_tour : int
    jeu_en_cours : bool

    min = 1
    max = 100 # On défini la limite du nombre mystère
    nombre_tour = 1
    jeu_en_cours = True

    # On demande au joueur 1 de sélectionner le nombre mystère
    # que le joueur 2 devra trouver entre 1 et 100
    nombre_mystère = int(getpass(nom_joueur(1) + ", choisissez le nombre mystère (entre 1 et 100) que " + nom_joueur(2) + " devra trouver: "))

    while jeu_en_cours:
        afficher_tour(nombre_tour)

        # Proposition
        proposition = int(input("\n" + nom_joueur(2) + ", veuillez choisir un nombre entre " + str(min) + " et " + str(max) + " : "))
        # Si on donne une proposition en dehors des limites, on redemande une proposition.
        while not proposition <= max and proposition >= min:
            proposition = int(input("\n" + nom_joueur(2) + ", votre proposition dois être entre " + str(min) + " et " + str(max) + " : "))
        
        # On utilise .strip pour enlever les espaces avant et après la réponse.
        réponse = input("\n" + nom_joueur(1) + ", votre réponse (répondez par 'trop petit', 'trop grand' ou 'c'est gagné') : ").strip().lower()
        
        # ANTI-CHEAT
        if réponse == "trop petit" and not proposition < nombre_mystère :
            print(nom_joueur(1) + ", vous avez triché !")
            #terminer le jeu et ajouter les scores au joueur 2
            jeu_en_cours = False

        elif réponse == "trop grand" and not proposition > nombre_mystère :
            print(nom_joueur(1) + ", vous avez triché !")
            #terminer le jeu et ajouter les scores au joueur 2
            jeu_en_cours = False

        elif réponse == "c'est gagné" and not proposition == nombre_mystère :
            print(nom_joueur(1) + ", vous avez triché !")
            #terminer le jeu et ajouter les scores au joueur 2
            jeu_en_cours = False

        else :
            if réponse == "trop petit":
                min = proposition + 1
            if réponse == "trop grand":
                max = proposition - 1
            if réponse == "c'est gagné":
                # ajouter les scores au joueur 2
                jeu_en_cours = False
        
        nombre_tour += 1
                

if __name__ == "__main__":
    main_devinette()