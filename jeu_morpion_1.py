# Notre matrice
M = [ ['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'] ]
N = [[],[],[]]

for i in M:
    print(i)


def convertion_joueur_1():
   a = input("Joueur 1, dans quelle case ?")
   if a =='A1':
       N[0].insert(0, 1)
       M[0][0]= 'X'
   elif a =='A2':
       N[0].insert(1, 1)
       M[0][1]= 'X'
       return 'X'
   elif a =='A3':
       N[0].insert(2, 1)
       M[0][2]= 'X'
       return 'X'
   elif a =='B1':
       N[1].insert(0, 1)
       M[1][0]= 'X'
       
   elif a =='B2':
       N[1].insert(1, 1)
       M[1][1]= 'X'
       return 'X'
   elif a =='B3':
       N[1].insert(2, 1)
       M[1][2]= 'X'
       return 'X'
   elif a =='C1':
       N[2].insert(0, 1)
       M[2][0]= 'X'
   elif a =='C2':
       N[2].insert(1, 1)
       M[2][1]= 'X'
   elif a =='C3':
       N[2].insert(2, 1)
       M[2][2]= 'X'
      
def convertion_joueur_2():
   a = input("Joueur 2, dans quelle case ?")
   if a =='A1':
       N[0].insert(0, 2)
       M[0][0]= 'O'
   elif a =='A2':
       N[0].insert(1, 2)
       M[0][1]= 'O'
   elif a =='A3':
       N[0].insert(2, 2)
       M[0][2]= 'O'
   elif a =='B1':
       N[1].insert(0, 2)
       M[1][0]= 'O'
       
   elif a =='B2':
       N[1].insert(1, 2)
       M[1][1]= 'O'
   elif a =='B3':
       N[1].insert(2, 2)
       M[1][2]= 'O'

   elif a =='C1':
       N[2].insert(0, 2)
       M[2][0]= 'O'
   elif a =='C2':
       N[2].insert(1, 2)
       M[2][1]= 'O'
   elif a =='C3':
       N[2].insert(2, 2)
       M[2][2]= 'O'

# La première colonne.
convertion_joueur_1()
convertion_joueur_2() 
convertion_joueur_1()
convertion_joueur_2()
convertion_joueur_1()
convertion_joueur_2() 
convertion_joueur_1()
convertion_joueur_2()
convertion_joueur_1() 


for i in M:
    print(i)

print(M)
print(N)










