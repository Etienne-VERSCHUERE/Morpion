M = [["1","2","3"],["4","5","6"],["7","8","9"]]
N = [["","",""],["","",""],["","",""]]
symbol = "X"
symbol = "O"
#fonction pour trouver l'index correspondant a input dans la matrice: M
def index_case_selectioné(valeur,matrice):
    for x, ligne in enumerate(matrice):
        for y,element in enumerate(ligne):
            if element == valeur:
                return (x,y)

choix_case = input()  
clef, valeur = index_case_selectioné(choix_case,M)
N[clef][valeur] = symbol
print(N[0])
print(N[1])
print(N[2])




              




