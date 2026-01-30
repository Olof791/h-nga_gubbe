ord = input("SKriv ett ord")
ord = ord.lower()
gissningar = 8
gissade = []
rätta = []

import os
ord = ord.lower()
os.system('cls' if os.name == 'nt' else 'clear')
# använde ai för att kunna ta bort ordet från skärmen




while gissningar > 0:
   
    visning = ""
    for bokstav in ord:
        if bokstav in rätta:
            visning += bokstav + " "
        else:
            visning += "_ "
    print(f"Ord: {visning}")
    
    
    if all(b in rätta for b in ord):
        print("Du vann!")
        break
    
   
    gissning = input("Gissa en bokstav: ").lower()
    
    if gissning in gissade:
        print("Redan gissat!\n")
        continue
    
    gissade.append(gissning)
    
 
    if gissning in ord:
        rätta.append(gissning)
        print("Rätt!\n")
    else:
        gissningar -= 1
        print(f"Fel! Gissningar kvar: {gissningar}\n")

if gissningar == 0:
    print(f"Du förlorade. Ordet var: {ord}")
