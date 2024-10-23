def choix_victoire(joueur):
   

    # ligne
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



myDico = [["1","2","3"],["4","5","6"],["7","8","9"]]
N = [[0,0,0],[0,0,0],[0,0,0]]


#fonction pour trouver l'index correspondant a input dans la matrice: myDico
def index_case_selectioné(valeur,matrice):
    for x, ligne in enumerate(matrice):
        for y,element in enumerate(ligne):
            if element == valeur:
                return (x,y)

#boucle pour les tours de jeu
def tour (joueur,symbole):
  choix_case = input(f"{joueur} donne un numéro de case:") 

  clef, valeur = index_case_selectioné(choix_case,myDico)
  myDico[clef][valeur] = symbole
  choix_victoire(joueur)
  for i in myDico:
      print(i)
      if choix_victoire(joueur):
                    break

     
   
     

for i in myDico:
      print(i)

for r in range(5):
 tour("Joueur 1", "X")

 tour("Joueur 2", "O")






              




