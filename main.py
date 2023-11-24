from utils.effacer_ecran import effacer_ecran
from utils.lanceur import préJeu
from utils.titre import faire_titre

if __name__ == "__main__":
    sélection: str
    sélection = ""

    while (sélection != "Q"):
        effacer_ecran()

        faire_titre("Bienvenue, dans la sélection de mini-jeux !"
                    + "\nChoisissez un jeu parmi les suivants.")

        print("\t", "1 │ Devinette")
        print("\t", "2 │ Allumettes")
        print("\t", "3 │ Morpion")
        print("\t", "4 │ Puissance 4")

        print("\n\t", "Q │ Quitter")

        sélection = input("\n\n-> Sélection(1,2,3,4,Q) : ").strip().upper()

        if sélection == "1":
            préJeu("devinette")
        elif sélection == "2":
            préJeu("allumettes")
        elif sélection == "3":
            préJeu("morpion")
        elif sélection == "4":
            préJeu("puissance_4")

    # On efface l'écran pour avoir un terminal
    # propre lors de la fermeture du programme.
    effacer_ecran()
