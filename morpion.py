from utils.afficher_tour import afficher_tour

def afficher_morpion(jeu : list[list[str]]):
    """procedure """

def main_morpion()->None:
    """Procédure de point d'entrée pour le jeu de morpion"""
    nb_tour : int
    en_cours : bool
    jeu : list[list[str]]

    nb_tour = 1
    en_cours = True
    jeu =  [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

    while en_cours:
        afficher_tour(nb_tour)