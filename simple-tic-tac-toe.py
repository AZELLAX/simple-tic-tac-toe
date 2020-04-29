import random
import time 
import datetime
import os
import inputimeout
from inputimeout import inputimeout, TimeoutOccurred

grille = [[' ']*3 for i in range(3)]  

def affichage() :
    """Affiche la grille de morpion actuelle dans la console """
    
    print("-"*13)
    for ligne in grille : 
        print("|", end="")
        for case in ligne : 
            print(" " + case + " ", end='|')
        print()
        print("-"*13)
        
    print()
        
def jeu(joueur) :
    """ Renvoie les coordonnées (x, y) choisies aléatoirement par l'ordinateur ou par le joueur """
    
    if joueur == "ordi" :
        print("Tour de l'ordinateur [🌀] : ")
        
    elif joueur == "joueur" :
        print("Tour du joueur 1 [X] :")   
        
    elif joueur == "joueur2" :
        print("Tour du joueur 2 [O] :")   
        
    while True :
        
        if joueur == "ordi" :
            x = random.randrange(3)
            y = random.randrange(3)
            
        elif joueur == "joueur" :
            x = y = -1
            while x < 0 or x > 2 or y < 0 or y > 2:
                try:
                    x = int(inputimeout(prompt='(Joueur 1) : Quelle colonne (0, 1 ou 2) ? Tu as 10 secondes pour choisir.\n', timeout=10))
                except TimeoutOccurred:
                    x = random.randrange(3)
                    print("Tu as été trop lent, une ligne aléatoire a été attribuée")
                    
                try:
                    y = int(inputimeout(prompt='(Joueur 1) : Quelle ligne (0, 1 ou 2) ? Tu as 10 secondes pour choisir.\n', timeout=10))
                except TimeoutOccurred:
                    y = random.randrange(3)
                    print("Tu as été trop lent, une colonne aléatoire a été attribuée")            
                    
        elif joueur == "joueur2":
            x = y = -1
            
            while x < 0 or x > 2 or y < 0 or y > 2:
                
                    try:
                        x = int(inputimeout(prompt='(Joueur 2) : Quelle colonne (0, 1 ou 2) ? Tu as 10 secondes pour choisir.\n', timeout=10))
                    except TimeoutOccurred:
                        while x < 0 or x > 2 or y < 0 or y > 2:
                            x = random.randrange(3)
                            print("Tu as été trop lent, une ligne aléatoire a été attribuée")
                            
                    try:
                        y = int(inputimeout(prompt='(Joueur 2) : Quelle ligne (0, 1 ou 2) ? Tu as 10 secondes pour choisir.\n', timeout=10))
                    except TimeoutOccurred:
                        while x < 0 or x > 2 or y < 0 or y > 2:
                            y = random.randrange(3)
                            print("Tu as été trop lent, une colonne aléatoire a été attribuée") 
                        
        if grille[y][x] == ' ' :
            return (x, y)                    
               
def endgame(tour) :
    """Renvoie un booléen True s'il y a alignement de symboles ou si le nombre de tours écoulés vaut 10, 
    ce qui entrainera la fin de la partie. Dans le cas contraire, renvoie False """
    
    if grille[0][0] == grille[1][1] == grille[2][2] == "🌀" or grille[0][2] == grille[1][1] == grille[2][0] == "🌀":
        print("L'ordinateur à gagné !")
        return True
    
    elif grille[0][0] == grille[1][1] == grille[2][2] == "X" or grille[0][2] == grille[1][1] == grille[2][0] == "X":
        print("Le joueur 1 à gagné !")    
        return True
    
    elif grille[0][0] == grille[1][1] == grille[2][2] == "O" or grille[0][2] == grille[1][1] == grille[2][0] == "O":
        print("Le joueur 2 à gagné !")
        return True
    
    for i in range(3) :
        
        if grille[i][0] == grille[i][1] == grille[i][2] == "🌀":
            print("L'ordinateur à gagné !")
            return True
        
        elif grille[i][0] == grille[i][1] == grille[i][2] == "X":
            print("Le joueur 1 à gagné !")
            return True
        
        elif grille[i][0] == grille[i][1] == grille[i][2] == "⭕":
            print("Le joueur 2 à gagné !")
            return True
        
    for j in range(3) :
        
        if grille[0][j] == grille[1][j] == grille[2][j] == "🌀":
            print("L'ordinateur à gagné !")
            return True
        
        elif grille[0][j] == grille[1][j] == grille[2][j] == "X":
            print("Le joueur 1 à gagné !")
            return True
        
        elif grille[0][j] == grille[1][j] == grille[2][j] == "O" :
            print("Le joueur 2 à gagné !")
            return True
        
    if tour == 10 :
        print("Égalité !")
        return True


def main() :
    """Fonction principale à exécuter pour lancer le jeu"""
    
    gamemode = int(input("Voulez vous jouez contre l'ordinateur ou à 2 joueurs ? Si vous voulez jouer contre l'ordinateur, tapez 1, sinon tapez 2.\n"))
    while gamemode != 1 and gamemode != 2:
        gamemode = int(input("Voulez vous jouez contre l'ordinateur ou à 2 joueurs ? Si vous voulez jouer contre l'ordinateur, tapez 1, sinon tapez 2.\n"))

    currenthour = datetime.datetime.now().strftime("%H:%M:%S")
    currentday = datetime.date.today()
    filename = f"morpion-{currentday}-{currenthour}"
    file = open(filename, 'w+')
    
    if gamemode == 1:
            
        start = time.time()
        i = 0
        tour = 1
        
        while not(endgame(tour)) :
            affichage()
            if i == 0 :
                x, y = jeu("ordi")
                file.write(f"Tour {tour} : Le joueur 1 a joué en x : {x} et y : {y}\n") 
                grille[y][x] = '🌀'

            else :
                x, y = jeu("joueur")
                file.write(f"Tour {tour} : Le joueur 1 a joué en x : {x} et y : {y}\n") 
                grille[y][x] = 'X'
                
            i = (i + 1)%2
            tour = tour + 1
            
    elif gamemode == 2:
        start = time.time()
        i = 0
        tour = 1
        
        while not(endgame(tour)) :
            affichage()
            if i == 0 :
                x, y = jeu("joueur")
                grille[y][x] = "X"
                
            else :
                x, y = jeu("joueur2")
                grille[y][x] = "O"
            
            i = (i + 1)%2
            tour = tour + 1
        
    print(f"Partie terminée ! (Tours : {tour-1}, Durée de la partie : {round(time.time() - start)} secondes)")
    file.write(f"Nombre de tours : {tour-1}, durée de la partie : {round(time.time() - start)} secondes") 

    save = input("Voulez vous garder une trace de la partie ? Répondez par oui si vous voulez la garder ou par non si vous ne voulez pas :\n").lower()
    
    while save != "non" and save != "oui":
        save = input("Voulez vous garder une trace de la partie ? Répondez par oui si vous voulez la garder ou par non si vous ne voulez pas :\n").lower()

    if save == "oui":
        file.close()
        
    else:
        file.close()
        os.remove(filename)
        
    affichage()

main()
    
 
