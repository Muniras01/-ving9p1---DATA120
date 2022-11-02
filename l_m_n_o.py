#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 21:33:53 2022

@author: muniraseedow
"""

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
            y = int(input("which wanna delete?:"))
            if input("Are you sure [y/n]")=="y":
                del ei_liste_avtaler[y]
        elif valg == 6: 
            while True:  
                n = int(input(f"Tittel: {ei_liste_avtaler.tittel}",
                              f"Sted: {ei_liste_avtaler.sted}",
                              f"Dato: {ei_liste_avtaler.dato}",
                              f"Tid: {ei_liste_avtaler.tid}",
                              f"Varighet:{ei_liste_avtaler.varighet}, \n Which one do you want to change?: "))
                for i in n:
                    if n == 0: 
                        ei_liste_avtaler[i].tittle=input("New tititele")
                    elif n == 1:
                        ei_liste_avtaler[i].tittle=input("New place")
                    elif n == 2: 
                        ei_liste_avtaler[i].tittle=input("New dato")
                    elif n ==3:
                        ei_liste_avtaler[i].tittle=input("New tid")
                    elif n == 4:
                        ei_liste_avtaler[i].tittle=input("New varighet")          
        elif valg == 7: 
             print("avslutt") 
             break
   
meny()