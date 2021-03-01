# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.

Bastien COUPARD & Ahmed MELLITI
"""

import numpy as np
from random import *
import matplotlib.pyplot as pyplot

matrice = np.zeros((10,10))
porte_avion = np.full((5),1)
croiseur = np.full((4),2)
contre_torpilleurs = np.full((3),3)
sous_marin=np.full((3),4)
torpilleur=np.full((2),5)



#print (porte_avions not calla, croiseur, contre_torpilleurs,sous_marin,torpilleur)
#position = [x,y]peut_placer(grille, bateau, position, direction)

def peut_placer(grille, bateau, position, direction):
    
    #"placement horizontal"
    if (direction==1):
        for i in range(0,10):
            for j in range(0,10):
                if ((i==position[0])and(j==position[1])):
                    if (j+len(bateau)<=10) :
                        for k in range(j,j+len(bateau)):
                            if (grille[i][k]!=0):
                                #print ("Position indisponible")
                                return False
                        return True
                    else : 
                        #print("Out of bounds")
                        return False
                    
    #"placement vertical"
    elif (direction==2) : 
        for i in range(0,10):
            for j in range(0,10):
                if ((i==position[0])and(j==position[1])):
                    if (i+len(bateau)<=10) :
                        for k in range(i,i+len(bateau)):
                            if (grille[k][j]!=0):
                                #print ("Position indisponible")
                                return False
                        return True
                    else : 
                        #print("Out of bounds")
                        return False
    #print("Invalid positions")
    return False



def place(grille, bateau, position, direction):
    matrice_return=grille
    if(peut_placer(grille,bateau,position,direction)==True):
        if (direction==1):
            for k in range(position[1],position[1]+len(bateau)):
                matrice_return[position[0]][k]=bateau[0]
        elif (direction==2):
            for k in range(position[0],position[0]+len(bateau)):
                matrice_return[k][position[1]]=bateau[0]
        else:
            print("DAAAAAAAAAAAMN")
            

    return matrice_return

def delete(grille, bateau, position, direction):
    matrice_return=grille
    if (direction==1):
        for k in range(position[1],position[1]+len(bateau)):
            matrice_return[position[0]][k]=0
    elif (direction==2):
        for k in range(position[0],position[0]+len(bateau)):
            matrice_return[k][position[1]]=0
    else:
            print("DAAAAAAAAAAAMN")
            

    return matrice_return


def place_alea(grille, bateau):
    coord=[randint(0,9),randint(0,9)]
    n=random()
    if (n < 0.5):
        direction=1
    else:
        direction=2
    while(peut_placer(grille, bateau, coord, direction)!=True):
        coord=[randint(0,9),randint(0,9)]
        n=random()
        if (n < 0,5):
            direction=1
        else:
            direction=2
    
    grille=place(grille, bateau, coord, direction)
    

def affiche(grille):
    print(grille)

def eq(grilleA, grilleB):
    return np.array_equal(grilleA, grilleB)

def genere_grille():
    mat_res=np.zeros((10,10))
    place_alea(mat_res,porte_avion)
    place_alea(mat_res,croiseur)
    place_alea(mat_res,sous_marin)
    place_alea(mat_res,contre_torpilleurs)
    place_alea(mat_res,torpilleur)
    
    #affiche(mat_res)
    return mat_res

#genere_grille()    

def compte_placement(grille,bateau):
    x=0
    for i in range(0,10):
        for j in range (0,10):
            if(peut_placer(grille, bateau, [i,j], 1) == True):
                x+=1
            if(peut_placer(grille, bateau,  [i,j], 2)==True):
                x+=1
    return x

def compte_placement2(grille,bateau):
    cpt=0
    for i in range(0,10):
        for j in range (0,10):
            grille_temp=np.copy(grille)
            if (peut_placer(grille, bateau[0], [i,j], 1)== True):
                place(grille_temp, bateau[0], [i,j], 1)
                for x in range(0,10):
                    for y in range(0,10):
                        if (peut_placer(grille_temp, bateau[1], [x,y], 1)== True):
                            cpt+=1
                        if (peut_placer(grille_temp, bateau[1], [x,y], 2)== True):
                            cpt+=1
            elif (peut_placer(grille_temp, bateau[0], [i,j], 2)== True):
                place(grille_temp, bateau[0], [i,j], 2)               
                for x in range(0,10):
                    for y in range(0,10):
                        if (peut_placer(grille_temp, bateau[1], [x,y], 1)== True):
                            cpt+=1
                        if(peut_placer(grille_temp, bateau[1], [x,y], 2)== True):
                            cpt+=1
    return cpt

def compte_placement3(grille,bateau):
    cpt=0
    b=0
    while(b<len(bateau)-1):
        for i in range(0,10):
            for j in range (0,10):
                grille_temp=np.copy(grille)
                if (peut_placer(grille, bateau[b], [i,j], 1)== True):
                    place(grille_temp, bateau[b], [i,j], 1)
                    for x in range(0,10):
                        for y in range(0,10):
                            if (peut_placer(grille_temp, bateau[b+1], [x,y], 1)== True):
                                cpt+=1
                            if (peut_placer(grille_temp, bateau[b+1], [x,y], 2)== True):
                                cpt+=1
                elif (peut_placer(grille_temp, bateau[b], [i,j], 2)== True):
                    place(grille_temp, bateau[b], [i,j], 2)               
                    for x in range(0,10):
                        for y in range(0,10):
                            if (peut_placer(grille_temp, bateau[b+1], [x,y], 1)== True):
                                cpt+=1
                            if (peut_placer(grille_temp, bateau[b+1], [x,y], 2)== True):
                                cpt+=1
        b+=1
    return cpt
      
def compte_placement4(grille,bateau):
    if(len(bateau)==0):
        return 1
    
    else:
        grille_tmp=np.copy(grille)
        cpt=0
        for i in range(0,10):
            for j in range(0,10):
                
                if (peut_placer(grille_tmp,bateau[0],[i,j],1)):
                    grille_tmp=place(grille_tmp,bateau[0],[i,j],1)
                    cpt+=compte_placement4(grille_tmp,bateau[1:])
                    grille_tmp=delete(grille_tmp,bateau[0],[i,j],1)
                    
                if (peut_placer(grille_tmp,bateau[0],[i,j],2)):
                    grille_tmp=place(grille_tmp,bateau[0],[i,j],2)
                    cpt+=compte_placement4(grille_tmp,bateau[1:])
                    grille_tmp=delete(grille_tmp,bateau[0],[i,j],2)
                    
    return cpt

def nb_tenta(grille):
    res=0
    grille_test=genere_grille()
    while(eq(grille,grille_test)!=True):
        grille_test=genere_grille()
        res+=1
        print(res)
    return res

class Bataille :
        def __init__(self):
            self.grille=genere_grille()
            #print(self.grille)
        

        
        def joue(self,position):
            
            if (self.grille[position[0]][position[1]] == 0):
                #print("Allo")
                return False
            elif (self.grille[position[0]][position[1]] == 404) :
                #print("already touched")
                return False
            else :
                #print(position)
                #print("Touche")
                self.grille[position[0]][position[1]]=404
                return True
        
        def victoire(self):
            
            for i in range (0,10):
                for j in range (0,10):
                    if (not((self.grille[i][j] == 0)or(self.grille[i][j] == 404))):
                        return False
            return True
        
        def reset(self):
            self.grille=genere_grille()
            
            
def Alea():
    l=[[]]
    bataille=Bataille()
    while(bataille.victoire()==False):
        alY=randint(0,9)
        alX=randint(0,9)
        while([alX,alY] in l):
            alY=randint(0,9)
            alX=randint(0,9)
        bataille.joue([alX,alY])
        l.append([alX,alY])
    #print(bataille.grille)
    #print("GG")
    #print(len(l)-1)
    return(len(l)-1)


def build_list():
    l=[[]]
    for i in range(0,10):
        for j in range(0,10):
            l.append([i,j])
    #print(l)
    return l


def enchainement(bataille,position,direction,sens,liste):
    cpt=0
    x=position[0]
    y=position[1]
    
    if (direction == 1):
        #print(bataille.grille)
        while(bataille.grille[x][y]!=0 and bataille.grille[x][y]!=404):
            if ([x,y] in liste):
                bataille.joue([x,y])
                liste.remove([x,y])
            if(x<=8):
                x+=sens
            else:
                return cpt
                
            cpt+=1
        return cpt
    
    elif (direction == 2) :
        #print(bataille.grille)
        while(bataille.grille[x][y]!=0 and bataille.grille[x][y]!=404):
            if ([x,y] in liste):
                bataille.joue([x,y])
                liste.remove([x,y])
            if (y<=8):
                y+=sens
            else: 
                return cpt
            cpt+=1
        return cpt
    else :
        print("Oh shit")

def heuristique():
    l=build_list()
    cpt=0
    bataille=Bataille()
    heuY=randint(0, 9)
    heuX=randint(0, 9)
    while(bataille.victoire()==False):
        if ([heuX,heuY] in l):        
            l.remove([heuX,heuY])
            cpt+=1
        if (bataille.joue([heuX,heuY]) == True):
            #l.remove([heuX,heuY])
            #cpt+=1
            if(heuX>=1):
                cpt+=enchainement(bataille,[heuX-1,heuY],1,-1,l)
            if(heuX<=8):
                cpt+=enchainement(bataille,[heuX+1,heuY],1,1,l)
            if(heuY>=1):
                cpt+=enchainement(bataille,[heuX,heuY-1],2,-1,l)
            if(heuY<=8):
                cpt+=enchainement(bataille, [heuX,heuY+1],2,1,l)
        
        N=choice(l)
        if (len(N)==2):
            heuX=N[0]
            heuY=N[1]
        #print([heuX,heuY])
        #heuX=randint(0,9)
        #heuY=randint(0,9)
        #while([heuX,heuY] not in l):
            #heuX=randint(0,9)
            #heuY=randint(0,9)
    #print(bataille.grille)
    #print(cpt)
    return cpt




#print(genere_grille())
#Alea()
#res=[]
#res2=[]
#for i in range (0,10000):
    #print(heuristique())
    #res2.append(Alea())    
    #res.append(heuristique())
#print(res)


#pyplot.hist(res2, range = (17, 100), bins = 83, color = 'blue',edgecolor = 'red')
#pyplot.xlabel('Nombre de coups joues')
#pyplot.ylabel('Nombre d ocurrence')
#pyplot.title('Bataille navale version aléatoire')
#matrice=genere_grille()
#print(nb_tenta(matrice))
#print(peut_placer(matrice,porte_avion,[0,9],2))
#print(compte_placement(matrice, [porte_avion])) 
#print(matrice)
#print(compte_placement4(matrice, [porte_avion, croiseur,contre_torpilleurs]))

#grille_temp=np.copy(matrice)
#print(grille_temp)
#grille_temp=np.delete(grille_temp,porte_avion)
#print(grille_temp)
    
#print(place(matrice, torpilleur, [1,0], 1))
#print(place(matrice, torpilleur, [0,1], 2))
#print(compte_placement(matrice, porte_avion))
#print(compte_placement(matrice, croiseur))
#print(compte_placement(matrice, contre_torpilleurs))
#print(compte_placement(matrice, sous_marin))
#print(compte_placement(matrice, torpilleur))


#Faire une boucle qui lance des générations de grille
#Incrémenter une variable quand on génère une grille non générer
#Comparaison de  matrice avec numpy
