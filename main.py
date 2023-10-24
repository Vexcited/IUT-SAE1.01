from utils.centrer import centrer
from utils.effacer_ecran import effacer_ecran

if __name__ == "__main__":
  effacer_ecran()

  print(centrer("Bienvenue!"))
  print("")
  print(centrer("1: Devinette"))
  print(centrer("2: Allumettes"))
  print(centrer("3: Morpion"))
  print("")
  print(centrer("Q: Sortir"))
  print("")
  input("Séléction(1,2,3,Q) : ")
