from utils.centrer import centrer
from utils.effacer_ecran import effacer_ecran

if __name__ == "__main__":
    sélection: str
    sélection = ""

    while (sélection.upper() != "Q"):
        effacer_ecran()

        print(centrer("Bienvenue, dans la sélection de mini-jeu !"))
        print("")

        print(centrer("1: Devinette"))
        print(centrer("2: Allumettes"))
        print(centrer("3: Morpion"))
        print("")

        print(centrer("Q: Sortir"))
        print("")

        sélection = input("Sélection(1,2,3,Q) : ")
