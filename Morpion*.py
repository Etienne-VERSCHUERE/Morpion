M = [["A1","A2","A3"],["B1","B2","B3"],["C1","C2","C3"]]
def case(valeur,matrice):
    for i, ligne in enumerate(matrice):
        for j,element in enumerate(ligne):
            if element == valeur:
                return f"trouvé({i},{j})"

choix=input("choisi une case")
print(case(choix,M))               
