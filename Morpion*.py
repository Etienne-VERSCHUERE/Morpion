M = [["A1","A2","A3"],["B1","B2","B3"],["C1","C2","C3"]]
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
# def fonc(index_case_selectioné,matrice):
#     # index_case_selectioné = index
#     # index = index_case_selectioné
#     # i,j = index_case_selectioné
#     print(index_case_selectioné(),'coucou')
#     matrice[i][j]="X"
#     return matrice
# # print(fonc(index,M))
# fonc(index_case_selectioné, M)  
#   
N[clef][valeur] = symbol
print(N[0])
print(N[1])
print(N[2])




              


# symbol = "X"
# isEnded = False

# array = {
# "A1": "",
# "A2": "",
# "A3": ""
# }


# while isEnded == False:
#     coordoonnée = input("entrez une coordonnée: ")
#     array[coordoonnée] = symbol
#     print(array)
#     for  i, ligne in enumerate(array):
#         print(array[ligne])
