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
            print("La valeur renseignée n'est pas valide, essaie encore.")
            continue  
        
        clef, valeur = index_case_selectioné(choix_case,monDico)
        monDico[clef][valeur] = symbole

#impression de liste myDico modifée
        grille_de_jeux()
        
        liste.remove(choix_case)
        
        return choix_victoire(joueur)

#Fonction de jeux
def morpion():
    try:
        while True:

            if tour(f"{rouge}Joueur 1 : X{base}", f"{rouge}X{base}"):
                break
            if tour(f"{vert}Joueur 2 : O{base}", f"{vert}O{base}"):
                break
    except KeyboardInterrupt:
        exit()

#Fonction déterminant les conditions de victoire
def choix_victoire(joueur):
    
    for ligne in monDico:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != " ":
            print(f"{joueur},{jaune}vous avez gagné !! l'autre joueur paye l'apero.{base} ")
            return True
    
    for colonne in range(3):
        if monDico[0][colonne] == monDico[1][colonne] == monDico[2][colonne] and monDico[0][colonne] != " ":
            print(f"{joueur},{jaune}vous avez gagné !! l'autre joueur paye l'apero. {base}")
            return True
        
    if (monDico[0][0] == monDico[1][1] == monDico[2][2] and monDico[0][0] != " ") or (monDico[0][2] == monDico[1][1] == monDico[2][0] and monDico[0][2] != " "):
        print(f"{joueur},{jaune}vous avez gagné !! l'autre joueur paye l'apero. {base}")
        return True
    
    if len(liste)== 0:
        print(f"{jaune} Egalité !!!{base}")
        return True

#Affichage travaillé de la grille de jeux:
def grille_de_jeux():
    print("                ")
    print(f"  {vert}Tic{base}{rouge}Tac{base}{jaune}Toe{base}")
    print("+---+---+---+")
    print("| "+monDico[0][0]+" |"+" "+monDico[0][1]+" |"+" "+monDico[0][2]+" |")
    print("+---+---+---+")
    print("| "+monDico[1][0]+" |"+" "+monDico[1][1]+" |"+" "+monDico[1][2]+" |")
    print("+---+---+---+")
    print("| "+monDico[2][0]+" |"+" "+monDico[2][1]+" |"+" "+monDico[2][2]+" |")
    print("+---+---+---+")
  
#Codes couleurs
rouge = "\033[91m"
vert = "\033[92m"
jaune = "\033[93m"
base = "\033[0m"

#Nos listes:
monDico = [["1","2","3"],["4","5","6"],["7","8","9"]]
liste = ["1","2","3","4","5","6","7","8","9"]

grille_de_jeux()

morpion()

#Boucle de redemarage
while True:
    
    monDico = [["1","2","3"],["4","5","6"],["7","8","9"]]
    liste = ["1","2","3","4","5","6","7","8","9"]
    
    demande_relancer_partie=input(f"Nouvelle partie ? ({vert}O{base} ou {rouge}N{base}) :")
    relancer_partie = demande_relancer_partie.upper()
    
    if relancer_partie == "N":
        print("A bientot !")
        break
    elif relancer_partie == "O":
        grille_de_jeux()
        morpion()
    else: 
        print("Je ne vous ai pas compris.")
        continue

print(liste)