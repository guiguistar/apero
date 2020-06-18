# coding: utf-8
#
# ------------------------------------------------------------------------------
# Info sur les auteur.e.s
# ------------------------------------------------------------------------------
#  abbrev. | Nom Complet            |  Rôle Princpal               |  Joker
# ------------------------------------------------------------------------------
#    sB    | Soufiane Benlhajlahsen | Alibi                        |   5
#    gR    | Guillaume Roux         |                              |   5
#    fmV   | Filipe Vasconcelos     | 80col. et commentaires freak |   4
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Commande git à connaitre pour démarrer (pour sB surtout):
# ------------------------------------------------------------------------------
#   git clone
#   git add
#   git commit -m "message du commit"
#   git pull
#   git push origin master
#   git log ( ça devient essentiel à plusieurs )
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Premières régles (à discuter/compléter) :
# ------------------------------------------------------------------------------
#   gR  :
#       - pas plus de 5 lignes par commit ( compliqué ? )
#       - pas 2 push d'affilé (fmV : ça peut etre fun )
#
#   fmV :
#       - peut être pas plus d'une fonction/taches par commit  gR: ça me va
#       - pas plus d'une classe (module) par push gR: ça me va aussi
#       - il faut des jokers 5 ? (gR en a parlé non ?) 
#       - pas de caractères d'espaces en fin de ligne (freak privilege) gR: \t ?
#       - le 5 lignes me parait impossible je vais griller tous mes joker gR: +
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# C'est quoi le projet ? (à compléter)
# ------------------------------------------------------------------------------
#   fmV :
#       - un truc qui clac en ligne de commande et/ou graphique;
#       - avec des belles maths et de l'output avec;
#         du 1.1545621528E+02 en veux tu en voilà !
#       - des librairies de compète : fftw, lapack de l'algèbre linéaire;
#       - du multilangage/multiniveau pour aller chercher de la performance;
#       - du benchmark de temps d'éxécution;
#       - des tests de précision numérique.
#
#       - ou alors on fait un morpion (-_-')
# ------------------------------------------------------------------------------



# ------------------------------------------------------------------------------
class ExceptionDeTypeBiereVide(Exception):
    pass

# ------------------------------------------------------------------------------
class Biere:

    def __init__(self,vol=500):
        self.verre=vol #fmv: vol en mL

    def boire(self,gorgee):
        if self.verre >= gorgee:
            self.verre-=gorgee
        else:
            raise ExceptionDeTypeBiereVide()
        
# ------------------------------------------------------------------------------
if __name__=="__main__":

    sB=Biere(125) #fmv: galopin hihi
    fmV=Biere()
    gR=Biere()

    print("Santé!")
    print("Saude!")
    print("C'est quoi le projet ?")

    sB.boire(10)
    fmV.boire(10)
    gR.boire(500) #gR: 500 :D

    gorgeeDeTrop = 50
    try:
        gR.boire(gorgeeDeTrop)
    except ExceptionDeTypeBiereVide:
        print("Aïe")
