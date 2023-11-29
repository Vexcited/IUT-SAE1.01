class EntréeScore:
    type_jeu: str
    """
    Le type du jeu auquel correspond cette entrée.
    Peut être `"devinette"`, `"allumettes"`, `"morpion"` ou `"puissance_4"`.
    """
    vainqueur: str
    """Le nom d'utilisateur du vainqueur."""
    perdant: str
    """Le nom d'utilisateur du perdant."""
    points: int
    """Le nombre de points gagnés par le vainqueur."""

class EntréePointsUtilisateur:
    nom_utilisateur: str
    """Le nom d'utilisateur de l'utilisateur."""
    points: int
    """Le nombre de points de l'utilisateur cumulés."""
    nombre_parties: int
    """Le nombre de parties jouées par l'utilisateur."""
