# Laget egen fil - Anniken

# Oppgave k
from main import Avtale

def søk_etter_streng(ei_liste_avtaler, en_streng):
    liste_ut = []
    for object in ei_liste_avtaler:
        if en_streng.lower() in object.tittel.lower():
            liste_ut.append(object)
    return liste_ut





if __name__=="__main__":

    dummy_liste_med_møter = []
    dummy_liste_med_møter.append(Avtale("møte på uni", "Stavanger", "2022-09-16 13:15:00", "45", "finans"))
    dummy_liste_med_møter.append(Avtale("møte med Erlend", "Oslo", "2022-09-15 12:15:00", "60", "politikk"))
    dummy_liste_med_møter.append(Avtale("Erlend sin bursdag", "Oslo", "2022-09-15 12:15:00", "60", "politikk"))

    for avtaler in søk_etter_streng(dummy_liste_med_møter, "Erlend"):
        print(avtaler)

