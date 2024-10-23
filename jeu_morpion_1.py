# Notre matrice
def convertion_joueur_1():
   a = input("Joueur 1, dans quelle case ?")
   if a =='1':
       N[0].insert(0, 1)
       M[0][0]= 'X'
   elif a =='2':
       N[0].insert(1, 1)
       M[0][1]= 'X'
       return 'X'
   elif a =='3':
       N[0].insert(2, 1)
       M[0][2]= 'X'
       return 'X'
   elif a =='4':
       N[1].insert(0, 1)
       M[1][0]= 'X'
       
   elif a =='5':
       N[1].insert(1, 1)
       M[1][1]= 'X'
       return 'X'
   elif a =='6':
       N[1].insert(2, 1)
       M[1][2]= 'X'
       return 'X'
   elif a =='7':
       N[2].insert(0, 1)
       M[2][0]= 'X'
   elif a =='8':
       N[2].insert(1, 1)
       M[2][1]= 'X'
   elif a =='9':
       N[2].insert(2, 1)
       M[2][2]= 'X'


      
def convertion_joueur_2():
   a = input("Joueur 2, dans quelle case ?")
   if a =='1':
       N[0].insert(0, 2)
       M[0][0]= 'O'
   elif a =='2':
       N[0].insert(1, 2)
       M[0][1]= 'O'
   elif a =='3':
       N[0].insert(2, 2)
       M[0][2]= 'O'
   elif a =='4':
       N[1].insert(0, 2)
       M[1][0]= 'O'
       
   elif a =='5':
       N[1].insert(1, 2)
       M[1][1]= 'O'
   elif a =='6':
       N[1].insert(2, 2)
       M[1][2]= 'O'

   elif a =='7':
       N[2].insert(0, 2)
       M[2][0]= 'O'
   elif a =='8':
       N[2].insert(1, 2)
       M[2][1]= 'O'
   elif a =='9':
       N[2].insert(2, 2)
       M[2][2]= 'O'
def index_case_selectioné(valeur,matrice):
    for x, ligne in enumerate(matrice):
        for y,element in enumerate(ligne):
            if element == valeur:
                return (x,y)

M = [ ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'] ]
N = [[0,0,0],[0,0,0],[0,0,0]]

positions ={"1": (0,0), "2":(0,1), '3': (0,2),
                "4": (1,0), "5":(1,1), '6': (1,2),
                "7": (2,0), "8":(2,1), '9': (2,2),
                }
def convertion(joueur, symbole):
     a = input(f"{joueur} donne un numéro de case:")
  
     if a in positions:
        x,y = positions[a]
     
        M[x][y]= symbole
        if symbole == "X":
         N[x][y]= 1
        else:
          N[x][y]= 2 
     else:
        print("Votre entrée n'est pas valide, voulez-vous rejouer?")
    
     for i in M:
            print(i)

    
        

tour=0
for tour in range (5):
 convertion("Joueur 1", "X")
 convertion("Joueur 2", "O")
 tour+=1

for i in M:
    print(i)
print(N)










