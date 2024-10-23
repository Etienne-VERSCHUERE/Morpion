myDico = {'matrice1': ["1 ","2 ","3 "],
          'matrice2': ["4 ","5 ","6 "],
          'matrice3': ["7 ","8 ","9 "] }

print(myDico)


def choix_victoire():
    # colonne 
    colonne = position
    if colonne :
        position = myDico[0][0], myDico[1][0],myDico[2][0]#(1er colonne)
        position = myDico[0][1], myDico[1][1],myDico[2][1]#(2e colonne)
        position = myDico[2][0], myDico[1][2],myDico[2][2]#(3e colonne)

    # ligne
    for ligne in myDico:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != " ":#ligne[0]= [1.2.3], ligne[1] = [4.5.6] et ligne[2] = [7.8.9]
            print("Victoire")
            return True
    
    for colonne in range(3):
        if myDico[0][colonne] == myDico[1][colonne] == myDico[2][colonne] and myDico[0][colonne] != " ":
            print("Victoire")
            return True
        
    if (myDico[0][0] == myDico[1][1] == myDico[2][2] and myDico[0][0] != " ") or (myDico[0][2] == myDico[1][1] == myDico[2][0] and myDico[0][2] != " "):
        print("Victoire")
        return True


def choix_défaite():
    # colonne 
    colonne = position
    if colonne :
        position = myDico[0][0], myDico[1][0],myDico[2][0]#(1er colonne)
        position = myDico[0][1], myDico[1][1],myDico[2][1]#(2e colonne)
        position = myDico[2][0], myDico[1][2],myDico[2][2]#(3e colonne)

    #ligne
    for ligne in myDico:
        if ligne[0] == ligne[1] != ligne[2] and ligne[0] != " ": #ligne[0]= [1.2.3], ligne[1] = [4.5.6] et ligne[2] = [7.8.9]
            print("Match nul")
            return False
        
    for colonne in range(3):
        if myDico[0][colonne] != myDico[1][colonne] == myDico[2][colonne] and myDico[0][colonne] != " ":
            print("Match nul")
            return False
    
    if (myDico[0][0] == myDico[1][1] != myDico[2][2] and myDico[0][0] != " ") or (myDico[0][2] = myDico[1][1] != myDico[2][0] and myDico[0][2] != " "):
        print("Match nul")
        return True