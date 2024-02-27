#!/usr/bin/python
# -*- coding: latin-1 -*-


haut_gauche = haut_millieux = haut_droit = millieux_gauche = millieux_millieux = millieux_droite = bas_gauche = bas_millieux = bas_droite = joueur1 = joueur2 = victoire = cout_global = 0
plateau = [[haut_gauche, haut_millieux, haut_droit],
    [millieux_gauche, millieux_millieux, millieux_droite], 
    [bas_gauche, bas_millieux, bas_droite]]
cout_joueur1 = 0
cout_joueur2 = 0
victoire = 0
fin = 0
collone = 0
ligne = 0
joueur = 0
t = 0
cout_joueur_e = 0
cout_joueur_l = 0
true_end = False

# fonction qui permet de demander quelle case jouer
def question(joueur):
    global cout_joueur_l
    global cout_joueur_e    
    end2 = False 
    while end2 == False:
        print(
            "Joueur {} qu'elle ligne voulez-vous jouer :".format(joueur))
        try:
            cout_joueur_l = int(input())
        except ValueError:
            print("La valeur que vous avez rentrer n'est pas un nombre.")
            print( )
            continue
        if cout_joueur_l == 1 or cout_joueur_l == 2 or cout_joueur_l == 3:
            end2 = True
            print( )
        else:
            print("Cette ligne n'existe pas. Il n'y a que 3 lignes.")
            print( )
    end2 = False
    
    while end2 == False:
        print(
            "Joueur {} qu'elle emplacement de la ligne {} voulez-vous jouer :".format(joueur, cout_joueur_l))
        try:
            cout_joueur_e = int(input())
        except ValueError:
            print("La valeur que vous avez rentrer n'est pas un nombre.")
            print( )
            continue
        if cout_joueur_e == 1 or cout_joueur_e == 2 or cout_joueur_e == 3:
            end2 = True
            print( )
        else:
            print("Cette emplacement n'existe pas. Il n'y a que 3 collones.")
            print( )
    end2 = False

# Fonction qui permet de déterminé si la partie est terminé
def resultat(plateau):
    global victoire
    global t
    nb = 0
    ligne = 0
    ligne2 = 2
    collone = int(0)
    fin = 0
    victoire = 0
    while fin == False:
        # commence les lignes
        while nb == False:
            if plateau[ligne][collone] == t:    # si (x;y) = t    t est le numero du joueur
                collone += 1
                if plateau[ligne][collone] == t:        # voir la collone suivante
                    collone += 1
                    # si la troisiemme valeur est = au nombre du joueur
                    if plateau[ligne][collone] == t:
                        print("Bravo tu as gagner !")           # si arriver ici alors c'est la victoire 
                        victoire = True
            ligne += 1
            collone = 0
            if ligne == 3:
                    nb = True
            collone = 0
        nb = False

        ligne = 0
        collone = 0
        while nb == False:
            # commence les collones
            if plateau [ligne] [collone] == t:
                ligne += 1
                if plateau [ligne] [collone] == t:
                    ligne += 1
                    if plateau  [ligne] [collone] == t:
                        print("Bravo tu as gagner !")
                        victoire = True
            collone += 1 
            ligne = 0
            if collone == 3:
                nb = True
        nb = False

        ligne = 0
        collone = 0

        # les diagonals
        if plateau [ligne] [ligne] == t:        #diagonal de droite a gauche
            ligne += 1
            if plateau [ligne] [ligne] == t:
                ligne += 1
                if plateau [ligne] [ligne] == t:
                    print("Bravo tu as gagner !")
                    victoire = True
                    nb = True
        ligne2 = 2
        ligne = 0
        if plateau [ligne] [ligne2] == t:          #diagonal de gauche a droite erreur la
            ligne2 -= 1
            ligne += 1
            if plateau [ligne] [ligne2] == t:
                ligne2 -= 1
                ligne += 1
                if plateau [ligne] [ligne2] == t:
                    print("Bravo tu as gagner !")
                    victoire = True

        fin = True

# Fonction qui permet d'afficher le plateau de jeu
def display(plateau):
    for x in plateau:
        count = 1
        for y in x:
            count+=1
            if (count < 4):
                print(" {}".format(y), end='')
            else:
                print(" {}".format(y), end='\n')
    print( )

#tronc du programme
while true_end == False:        
    while victoire == False:
        nb = 0
        
        # joueur 1
        joueur = 1
        ok = False
        question(joueur)
        t= 1

        x = cout_joueur_l - 1
        y = cout_joueur_e - 1

        encienne_rep = plateau [x] [y]
        plateau [x] [y] = 1

        while ok == False :         
            if encienne_rep != 0 :
                plateau [x] [y] = encienne_rep
                print("La case ({};{}) est deja remplie.".format(cout_joueur_l, cout_joueur_e))
                print()
                question (joueur)
                x = cout_joueur_l 
                y = cout_joueur_e 
                x -= 1
                y -= 1
                encienne_rep = plateau [x] [y]
                plateau [x] [y] = 1
            else :
                ok = True
        t = 1
        
        display(plateau)
        resultat(plateau)
        cout_global += 1

        if cout_global == 9 and victoire == False:
            victoire = True
            print("Dommage vous etes a egaliter...")

        x = y = 0
        if victoire == True:
            break

        # joueur 2
        joueur = 2
        question(joueur)
        
        t= 2
        ok = False
        x = cout_joueur_l 
        y = cout_joueur_e 
        x = x - 1
        y = y - 1
        encienne_rep = plateau [x] [y]
        plateau [x] [y] = 2
        
        while ok == False :         #erreur ici 
            if encienne_rep != 0 :
                plateau [x] [y] = encienne_rep
                print("La case ({};{}) est deja remplie.".format(cout_joueur_l, cout_joueur_e))
                question(joueur)
                x = cout_joueur_l 
                y = cout_joueur_e 
                x -= 1
                y -= 1
                encienne_rep = plateau [x] [y]
                plateau [x] [y] = 2
            else :
                ok = True
        t = 2

        display(plateau)
        resultat(plateau) 
        cout_global += 1

        if cout_global == 9:
            victoire = True
            print("D'ommage vous etes a égaliter...")
        
        cout_joueur1 = 1
        cout_joueur2 = 1
    end = False
    while end == False:
        print()                                 #script savoir si end
        print("1. Autre partit")
        print("2. fin")
        toto = int(input())
        if toto == 1 or toto == 2:
            end = True
        else:
            print("Votre réponse n'existe pas ")
    end = True
    if toto == 2:
        true_end = True
    else:
        victoire = False
        collone = 0
        ligne = 0 
        while ligne < 3:      #remet a 0 le plateau
            while collone < 3:
                x = ligne
                y = collone
                plateau [x] [y] = 0
                collone += 1
            ligne += 1
            collone = 0
        print()