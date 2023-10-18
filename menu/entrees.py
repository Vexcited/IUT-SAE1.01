class EntréeMenu:
  """
  Structure d'une entrée dans le menu.
  """

  text : str
  """
  Texte affiché dans le menu d'accueil.
  """
  
  selection : bool
  """
  Permet de savoir si cet élément peut être sélectionné
  ou non dans le menu d'accueil.
  """

def entrées() -> list[EntréeMenu] :
  """
  Fonction permettant de récupérer la liste des entrées
  disponibles dans le menu d'accueil.

  Entrée : Rien
  Sortie : Liste des entrées dans l'ordre où ils doivent être affichés.
  """
  accueil: EntréeMenu
  description: EntréeMenu
  saut_de_ligne: EntréeMenu
  jeu_devinette: EntréeMenu
  jeu_allumettes: EntréeMenu
  jeu_morpion: EntréeMenu

  accueil = EntréeMenu()
  accueil.text = "Bienvenue !"
  accueil.selection = False

  description = EntréeMenu()
  description.text = "SAÉ1.01"
  description.selection = False

  # Vu qu'on saute une ligne sur chaque entrée,
  # faire une entrée vide ramène à faire un simple saut à la ligne.
  # On le définit qu'une fois pour s'en ren-servir plus tard.
  saut_de_ligne = EntréeMenu()
  saut_de_ligne.text = ""
  saut_de_ligne.selection = False

  jeu_devinette = EntréeMenu()
  jeu_devinette.text = "Devinette"
  jeu_devinette.selection = True

  jeu_allumettes = EntréeMenu()
  jeu_allumettes.text = "Allumettes"
  jeu_allumettes.selection = True
  
  jeu_morpion = EntréeMenu()
  jeu_morpion.text = "Morpion"
  jeu_morpion.selection = True

  return [
    accueil,
    description,
    saut_de_ligne,
    jeu_devinette,
    saut_de_ligne,
    jeu_allumettes,
    saut_de_ligne,
    jeu_morpion
  ]

