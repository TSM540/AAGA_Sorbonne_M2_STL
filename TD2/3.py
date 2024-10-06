import os


class ArbreBinaire:
    def __init__(self, gauche=None, droit=None):
        """
        Initialise un arbre binaire.
        
        :param gauche: Sous-arbre gauche (instance d'ArbreBinaire ou None)
        :param droit: Sous-arbre droit (instance d'ArbreBinaire ou None)
        """
        self.gauche = gauche
        self.droit = droit

    def est_feuille(self):
        """
        Vérifie si l'arbre est une feuille.
        
        :return: True si l'arbre est une feuille, False sinon
        """
        return self.gauche is None and self.droit is None

    def __repr__(self):
        if self.est_feuille():
            return "()"
        return f"({self.gauche} {self.droit})"


def arbre2str(arbre, nom_fichier):
    """
    Encode un arbre binaire sous forme d'une expression bien parenthésée et écrit dans un fichier.

    :param arbre: Instance d'ArbreBinaire à encoder
    :param nom_fichier: Nom du fichier (sans extension) où écrire l'encodage
    """
    def encoder(arbre):
        if arbre.est_feuille():
            return "()"
        gauche_enc = encoder(arbre.gauche)
        droit_enc = encoder(arbre.droit)
        return f"({gauche_enc}{droit_enc})"

    chaine = encoder(arbre)
    chemin_fichier = os.path.join(os.getcwd(), f"{nom_fichier}.txt")
    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        fichier.write(chaine)

    print(f"Fichier généré : {chemin_fichier}")
# Création d'un arbre binaire : ( () ( () () ) )
arbre = ArbreBinaire(
    gauche=ArbreBinaire(),
    droit=ArbreBinaire(
        gauche=ArbreBinaire(),
        droit=ArbreBinaire()
    )
)
arbre2str(arbre, "arbre")

