#boucle déterminant les conditions de victoire
def choix_victoire(joueur):
    if len(liste) ==0:
        print("match null")
        return True

    for ligne in myDico:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != " ":#ligne[0]= [1.2.3], ligne[1] = [4.5.6] et ligne[2] = [7.8.9]
            print(f"{joueur},vous avez gagné !! l'autre joueur paye l'apero. ")
            return True
        
    
    for colonne in range(3):
        if myDico[0][colonne] == myDico[1][colonne] == myDico[2][colonne] and myDico[0][colonne] != " ":
            print(f"{joueur},vous avez gagné !! l'autre joueur paye l'apero. ")
            return True
        
        
    if (myDico[0][0] == myDico[1][1] == myDico[2][2] and myDico[0][0] != " ") or (myDico[0][2] == myDico[1][1] == myDico[2][0] and myDico[0][2] != " "):
        print(f"{joueur},vous avez gagné !! l'autre joueur paye l'apero. ")
        return True
            

       