# Laget egen fil - Anniken

# Oppgave k, a
from main import Avtale

def søk_etter_streng(ei_liste_avtaler, en_streng):
    liste_ut = []
    for object in ei_liste_avtaler:
        if en_streng.lower() in object.tittel.lower():
            liste_ut.append(object)
    return liste_ut


# Oppgave l
def menysystem():
    print("\nMenysystem for avtaler")
    print("1: Les inn avtale(r) fra fil")
    print("2: Skriv avtale(r) til fil")
    print("3: Skriv inn ny avtale")
    print("4: Skriv ut alle avtaler")
    print("5: Exit")

    while True:
        try:    
            tall = float(input("\nSkriv inn tallet til funskjonene du ønsker å utføre: "))

            #if tall == 1:
                #les_avtale_fil()

            #if tall == 2:
                

            #if tall == 3:
            #   lagre_liste_m_avtaler()

            #if tall == 4:
                #list_opp_avtaler()

            if tall == 5:
                print("Avsluttet")
                break
            
            else:
                print("Dette er ikke ett gyldig tall")
        
        except ValueError:
            print("Du må skrive tallet til funksjonen") 

if __name__=="__main__":

    dummy_liste_med_møter = []
    dummy_liste_med_møter.append(Avtale("møte på uni", "Stavanger", "2022-09-16 13:15:00", "45", "finans"))
    dummy_liste_med_møter.append(Avtale("møte med Erlend", "Oslo", "2022-09-15 12:15:00", "60", "politikk"))
    dummy_liste_med_møter.append(Avtale("Erlend sin bursdag", "Oslo", "2022-09-15 12:15:00", "60", "politikk"))

   #for avtaler in søk_etter_streng(dummy_liste_med_møter, "Erlend"):
    #    print(avtaler)
    menysystem()
