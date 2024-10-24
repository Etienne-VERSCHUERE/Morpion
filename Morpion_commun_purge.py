#Fonction de recherche d'index
def index_case_selectioné(valeur,matrice):
    
    for x, ligne in enumerate(matrice):
        for y,element in enumerate(ligne):
            if element == valeur:
                return (x,y)
#Fonction pour les tours de jeu
def tour (joueur,symbole):

    while True:  
        choix_case = input(f"{joueur} donne un numéro de case : ")
        
        
        if choix_case not in liste:
            print("La valeur renseignée n'est pas valide, try again.")
            continue  

        clef, valeur = index_case_selectioné(choix_case,myDico)
        
        myDico[clef][valeur] = symbole

#impression de liste myDico modifée
        for i in myDico:
            print(i)
        
        liste.remove(choix_case)
        
        return choix_victoire(joueur)
#Fonction de jeux
def morpion():
   while True:
        

        if tour("Joueur 1", "X"):
            break
        if tour("Joueur 2", "O"):
            break
#Fonction déterminant les conditions de victoire
def choix_victoire(joueur):

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

#variables
myDico = [["1","2","3"],["4","5","6"],["7","8","9"]]
liste=["1","2","3","4","5","6","7","8","9"]


morpion()
#Boucle de redemarage
while True:
    relancer_partie=input("nouvelle partie ? :")
    myDico = [["1","2","3"],["4","5","6"],["7","8","9"]]
    liste=["1","2","3","4","5","6","7","8","9"]
    if relancer_partie == "N":
        print("A bientot !")
        break
    else:

        morpion()
        
    








              




