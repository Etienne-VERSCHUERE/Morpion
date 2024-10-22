M = [["A1","A2","A3"],["B1","B2","B3"],["C1","C2","C3"]]
N = [["","",""],["","",""],["","",""]]
#fonction pour trouver l'index correspondant a input dans la matrice: M
def index_case_selectioné(valeur,matrice):
    for i, ligne in enumerate(matrice):
        for j,element in enumerate(ligne):
            if element == valeur:
                return (i,j)


choix_case = input() 

              
def fonc(index_case_selectioné,matrice):
    index_case_selectioné = index
    matrice[i][j]="X"
    return matrice
index = index_case_selectioné
print(fonc(index,M))

