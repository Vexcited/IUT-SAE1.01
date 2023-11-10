import os

def afficher_tour(numero:int)->None:
    """procedure qui affiche proprement le numero du tour 
        entrée : le numéro du tour
    """
    print("\n"+"-"*((os.get_terminal_size().columns//2)-4), "TOUR", numero, "-"*((os.get_terminal_size().columns//2)-4))