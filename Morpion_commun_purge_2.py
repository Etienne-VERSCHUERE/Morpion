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
            continue  
        

#impression de liste myDico modifée
        grille_de_jeux()
        
        liste.remove(choix_case)
        
        return choix_victoire(joueur)

#Fonction de jeux
def morpion():
    try:
        while True:

            if tour("Joueur 1", "X"):
                break
            if tour("Joueur 2", "O"):
                break
    except KeyboardInterrupt:
        exit()

#Fonction déterminant les conditions de victoire
def choix_victoire(joueur):
    
    if len(liste)== 0:
        return True

        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != " ":
            print(f"{joueur},vous avez gagné !! l'autre joueur paye l'apero. ")
            return True
    
    for colonne in range(3):
            print(f"{joueur},vous avez gagné !! l'autre joueur paye l'apero. ")
            return True
        
        print(f"{joueur},vous avez gagné !! l'autre joueur paye l'apero. ")
        return True
    
#Affichage travaillé de la grille de jeux:
def grille_de_jeux():
    print("                ")
    print("  TicTacToe")
    print("+---+---+---+")
    print("+---+---+---+")
    print("+---+---+---+")
    print("+---+---+---+")
  

#Nos listes:
liste=["1","2","3","4","5","6","7","8","9"]

grille_de_jeux()

morpion()

#Boucle de redemarage
while True:
    
    liste=["1","2","3","4","5","6","7","8","9"]
    
    demande_relancer_partie=input("Nouvelle partie ? (Y ou N) :")
    relancer_partie = demande_relancer_partie.upper()
    
    if relancer_partie == "N":
        print("A bientot !")
        break
        grille_de_jeux()
        morpion()
    else: 
        print("Je ne vous ai pas compris.")
        continue

print(liste)