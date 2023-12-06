from os import get_terminal_size

def centrer (text : str) -> str:
  """
    Fonction qui prend une chaine de caractères en entrée
    et donne une chaine de caractère centrée en fonction du terminal en sortie.

    ## Entrée :
    - `text`, chaîne de caractères qui correspond au texte que l'on veut centrer

    ## Sortie :
    La chaîne de caractères `text` centré par rapport à l'écran du terminal.
  """

  largeur : int
  largeur = get_terminal_size().columns

  return str.center(text, largeur)