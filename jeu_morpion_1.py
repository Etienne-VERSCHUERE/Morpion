
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
symbol = "X"
symbol = "O"









