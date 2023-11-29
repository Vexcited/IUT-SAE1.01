from getpass import getpass
from utils.afficher_tour import afficher_tour
from scores.entrée import EntréeScore
from scores.fichier import écrireScore

def calcul_score(nombre_tour : int) -> int:
    """
    Calcule le score du joueur 2 en fonction du nombre de tours.
    """

    score : int
    score = int(1000 // (nombre_tour ** 2))
    
    return score


def main_devinette(joueur1: str, joueur2: str) -> None:
    """
    Procédure de point d'entrée pour le jeu de devinette.
    """

    nombre_mystère : int
    proposition : int
    réponse : str
    min : int
    max : int
    nombre_tour : int
    jeu_en_cours : bool
    triche: bool
    score : EntréeScore

    min = 1
    max = 100 # On défini la limite du nombre mystère
    nombre_tour = 1
    réponse = ""
    jeu_en_cours = True
    triche = False
    score = EntréeScore()
    score.perdant = joueur1
    score.vainqueur = joueur2
    score.type_jeu = "devinette"

    # On demande au joueur 1 de sélectionner le nombre mystère
    # que le joueur 2 devra trouver entre 1 et 100
    nombre_mystère = int(getpass(joueur1 + ", choisissez le nombre mystère (entre 1 et 100) que " + joueur2 + " devra trouver: "))

    while jeu_en_cours:
        afficher_tour(nombre_tour)

        # Proposition
        proposition = int(input("\n" + joueur2 + ", veuillez choisir un nombre entre " + str(min) + " et " + str(max) + " : "))
        # Si on donne une proposition en dehors des limites, on redemande une proposition.
        while not proposition <= max and proposition >= min:
            proposition = int(input("\n" + joueur2 + ", votre proposition dois être entre " + str(min) + " et " + str(max) + " : "))
        
        while réponse != "trop petit" and réponse != "trop grand" and réponse != "c'est gagné":
            # On utilise .strip pour enlever les espaces avant et après la réponse.
            réponse = input("\n" + joueur1 + ", votre réponse (répondez par 'trop petit', 'trop grand' ou 'c'est gagné') : ").strip().lower()
        
        # ANTI-CHEAT
        if réponse == "trop petit" and not proposition < nombre_mystère :
            triche = True
            jeu_en_cours = False

        elif réponse == "trop grand" and not proposition > nombre_mystère :
            triche = True
            jeu_en_cours = False

        elif réponse == "c'est gagné" and not proposition == nombre_mystère :
            triche = True
            jeu_en_cours = False

        else:
            if réponse == "trop petit":
                min = proposition + 1
            if réponse == "trop grand":
                max = proposition - 1
            if réponse == "c'est gagné":
                # ajouter les scores au joueur 2
                jeu_en_cours = False
        
        nombre_tour += 1
        réponse = ""

    if (triche):
        print("\n" + joueur1 + ", vous avez triché !")
        print(joueur2 + ", vous avez gagné mais aucun point ne vous est attribué.")
    else:
        score.points = calcul_score(nombre_tour)
        écrireScore(score)

        print("\n" + joueur2 + ", vous avez trouvé le nombre mystère en " + str(nombre_tour) + " tours !")
        print("Votre score est de " + str(score.points) + " points !")

    input("\nAppuyez sur Entrée pour continuer...") 

if __name__ == "__main__":
    main_devinette("Joueur1", "Joueur2")
