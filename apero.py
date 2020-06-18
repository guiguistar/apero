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
# commande git à connaitre pour démarrer (pour sB surtout):
# ------------------------------------------------------------------------------
#   git clone
#   git add
#   git commit -m "message du commit"
#   git pull
#   git push origin master
#   git log ( ça devient essentiel à plusieurs )
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# première régles (à discuter) :
# ------------------------------------------------------------------------------
# gR
#       - pas plus de 5 lignes par commit ( compliqué ? )
#       - pas 2 push d'affilé (fmV : ça peut etre fun )
#
# fmV
#       - peut être pas plus d'une fonction/taches par commit
#       - pas plus d'une classe (module) par push
#       - il faut des jokers 5 ? (gR en a parlé non ?)
#       - pas de caractères d'espaces en fin de ligne (freak privilege)
#       - le 5 lignes me parait impossible je vais griller tout mes joker 
#       

class Biere:

    #vol : volume (mL)
    def __init__(self,vol=500):
        self.verre=vol

    def boire(self,gorgee):
        if self.verre >= gorgee:
            self.verre-=gorgee
        else:
            raise ExceptionDeTypeBiereVide()

class ExceptionDeTypeBiereVide(Exception):
    pass
        
if __name__=="__main__":

    sB=Biere(125) #galopin hihi
    fmV=Biere()
    gR=Biere()

    print("Santé!")
    print("Saude!")
    print("C'est quoi le projet ? ")

    sB.boire(10)
    fmV.boire(10)
    gR.boire(500) # gR: 500 :D

    gorgeeDeTrop = 50
    try:
        gR.boire(gorgeeDeTrop)
    except ExceptionDeTypeBiereVide:
        print("Aïe")
