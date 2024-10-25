M = [["1","2","3"],["4","5","6"],["7","8","9"]]
N = [[0,0,0],[0,0,0],[0,0,0]]
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
M[clef][valeur] = symbol
print(M[0])
print(M[1])
print(M[2])




              




