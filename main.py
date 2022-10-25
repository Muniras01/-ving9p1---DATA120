import datetime
#Oppgave d
class Avtale:
    def __init__(self, title, sted, starttidspunkt, varighet, kategori):
         self.tittel= title
         self.sted= sted
         self.starttidspunkt = starttidspunkt
         self.varighet= varighet
         self.kategori= kategori
#oppgave e
    def __str__(self):
        return f"Møte: tittel:{self.tittel} ,sted:{self.sted},tidspunkt:{self.starttidspunkt}, varighet:{self.varighet}min,kategori:{self.kategori})"
#oppgave f

def avtale():
    title= input("Skriv inn tittelen:")
    sted= input("Skriv inn et sted:")
    starttidspunkt= datetime.datetime.fromisoformat(input("Skriv inn starttidspunktet:"))
    varighet= int(input("Skriv inn varigheten i minutter:"))
    kategori= input("Skriv inn kategorien:")
    return Avtale(title, sted, starttidspunkt, varighet, kategori)
#min_avtale = avtale()
#print(min_avtale)

#Oppgave g
dummy_liste_med_møter = []
dummy_liste_med_møter.append(Avtale("møte1", "Stavanger", "2022-09-16 13:15:00", "45", "finans"))
dummy_liste_med_møter.append(Avtale("møte2", "Oslo", "2022-09-15 12:15:00", "60", "politikk"))
def list_opp_avtaler(liste_med_avtaler, overskrift="ikke satt"):
    if overskrift != "ikke satt":
        print(overskrift)
    for index, avtale in enumerate(liste_med_avtaler):
        print(index)
        print(avtale.tittel)
list_opp_avtaler(dummy_liste_med_møter)

         
