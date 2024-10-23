# Notre matrice
M = [ ["A1", "A2", "A3"],["B1","B2","B3"],["C1", "C2", "C3"] ]

def choix_victoire(M):
    # Vérifier les éléments de lignes s'ils sont égaux et non vide
    for ligne in M:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != " ":
            print("Victoire")
            return True

    # Vérifier les colonnes trois fois
    for colone in range(3):
        if M[0][colonne] == M[1][colonne] == M[2][colonne] and M[0][colonne] != " ":
            print("Victoire")
            return True

    # Vérifier les deux  diagonales
    if (Matrice[0][0] == Matrice[1][1] == Matrice[2][2] and Matrice[0][0] != " ") or (Matrice[0][2] == Matrice[1][1] == Matrice[2][0] and Matrice[0][2] != " "):
        print("Victoire")
        return True
    print("math nul")
    return False
