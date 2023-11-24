from os import system, name

def effacer_ecran() -> None:
  """
  Procédure qui permet "d'effacer" le contenu du terminal.
  Inspiré de [cette réponse sur StackOverflow](https://stackoverflow.com/a/44740224).
  """

  # On est sur Unix, Linux, macOS, BSD, etc...
  if name == "posix":
    # Voir <https://fr.wikipedia.org/wiki/Clear_(Unix)>
    system("clear")
  # On part du principe qu'on est sur Windows.
  else:
    # L'alternative de `clear` de Unix sur Windows.
    # Voir <https://fr.wikipedia.org/wiki/Cls_(commande)#Windows_NT>
    # et <https://fr.wikipedia.org/wiki/Cls_(commande)#Windows_PowerShell>.
    system("cls")
