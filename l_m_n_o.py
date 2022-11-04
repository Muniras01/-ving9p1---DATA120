#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 21:33:53 2022

@author: muniraseedow
"""
from main import *
from k_l import *

# def endreAvtale(): 

def redigere(avtalen):
     n =  int(input("1. tittel \n 2.sted \n 3.dato \n 4.tid \n 5.varighet \n Enter whihch one you want to change: "))
     for i in range(n):
         if n == 1: 
             dummy_liste_med_møter[i].tittle=input("New tititel: " )
         elif n == 2:
             dummy_liste_med_møter[i].sted=input("New place: ")
         elif n == 3: 
             dummy_liste_med_møter[i].date=input("New dato: ")
         elif n == 4:
             dummy_liste_med_møter[i].tid=input("New tid: ")
         elif n ==5:
             dummy_liste_med_møter[i].varighet=input("New varighet: ")  

    
      
def meny(): 
    ei_liste_avtaler = [ ]
    if (len(ei_liste_avtaler)== 0): 
        print("havent done any: ")
    else: lagre_liste_m_avtaler(ei_liste_avtaler)
    while True:
        valg = int(input("1. Skrive inn en ny avtale\n 2. lese inn avtaler fra fil \n 3. Skriv ut alle avtalene\n 4. skriv avtalene til fil \n 5. Delete \n 6. Make changes \n 7.Avslutt  \n Enter your choice: "))
        if valg == 1: 
            ny_avtale = avtale()
            ei_liste_avtaler.append(ny_avtale) 
        elif valg == 2: 
            lese_avtale = søk_etter_streng()
            if lese_avtale in ei_liste_avtaler: 
                print(lese_avtale, "is in the leset",  ei_liste_avtaler[lese_avtale])
            else: 
                print(lese_avtale, "isnt in the list ")
        elif valg == 3: 
            if not ei_liste_avtaler: 
                print("tomt liste")
        elif valg ==4: 
            lagre_liste_m_avtaler(ei_liste_avtaler)
        elif valg == 5: 
            list_opp_avtaler(ei_liste_avtaler)
            y = int(input("which one do you wanna delete?:"))
            if input("Are you sure [y/n]")=="y":
                del ei_liste_avtaler[y]
            
        elif valg == 6: 
            redigere(ei_liste_avtaler)
            
        elif valg == 7: 
             print("avslutt") 
             break
if __name__=="__main__":
    meny()   
