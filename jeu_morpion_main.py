myDico = {'matrice1': [" "," "," "],
          'matrice2': [" "," "," "],
          'matrice3': [" "," "," "] }

print(myDico)


def choix_victoire():
    # Vérifier les éléments de lignes s'ils sont égaux et non vide
    colonne = position
    if colone :
        position = myDico[0][0], myDico[1][0],myDico[2][0]
        position = myDico[0][1], myDico[1][1],myDico[2][1]
        position = myDico[2][0], myDico[1][2],myDico[2][2]
    
    for ligne in myDico:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != " ":
            print("Victoire")
            return True

    # Vérifier les colonnes trois fois
    for colone in range(3):
        if myDico[0][colonne] == myDico[1][colonne] == myDico[2][colonne] and myDico[0][colonne] != " ":
            print("Victoire")
            return True

    # Vérifier les deux  diagonales
    if (myDico[0][0] == myDico[1][1] == myDico[2][2] and myDico[0][0] != " ") or (myDico[0][2] == myDico[1][1] == myDico[2][0] and myDico[0][2] != " "):
        print("Victoire")
        return True

def choix_défaite():
    colonne = position
    if colone :
        position = myDico[0][0], myDico[1][0],myDico[2][0]
        position = myDico[0][1], myDico[1][1],myDico[2][1]
        position = myDico[2][0], myDico[1][2],myDico[2][2]
    
    for ligne in myDico:
        if ligne[0] == ligne[1] != ligne[2] and ligne[0] != " ":
            print("Match nul")
            return False
        
    for colone in range(3):
        if myDico[0][colonne] != myDico[1][colonne] == myDico[2][colonne] and myDico[0][colonne] != " ":
            print("Match nul")
            return False
    
    if (myDico[0][0] == myDico[1][1] != myDico[2][2] and myDico[0][0] != " ") or (myDico[0][2] != myDico[1][1] == myDico[2][0] and myDico[0][2] != " "):
        print("Match nul")
        return True