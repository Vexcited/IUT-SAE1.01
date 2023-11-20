from utils.centrer import centrer
from utils.effacer_ecran import effacer_ecran
from joueurs.session import initialiser_session, supprimer_session

if __name__ == "__main__":
    sélection: str
    sélection = ""

    # On initialise la session de jeu avant
    # de commencer le programme.
    initialiser_session()
    while (sélection.upper() != "Q"):
        effacer_ecran()

        print(centrer("Bienvenue, dans la sélection de mini-jeux !"))
        print("")  # Saut de ligne

        print(centrer("1: Devinette"))
        print(centrer("2: Allumettes"))
        print(centrer("3: Morpion"))
        print("")  # Saut de ligne

        print(centrer("Q: Sortir"))
        print("")  # Saut de ligne

        sélection = input("Sélection(1,2,3,Q) : ")

    # On efface les utilisateurs de la
    # session de jeu avant de quitter.
    supprimer_session()

    # On efface l'écran pour avoir un terminal
    # propre lors de la fermeture du programme.
    effacer_ecran()
