from os import get_terminal_size

def centrer (text : str) -> str:
  """
    Fonction qui prend une chaine de caractères en entrée
    et donne une chaine de caractère centrée en fonction du terminal en sortie.

    Entrée : chaine de caractère
    Sortie : chaine de caractère centré
  """

  largeur : int
  largeur = get_terminal_size().columns

  return str.center(text, largeur)