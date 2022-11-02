import datetime
#Oppgave d
class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet, kategori):
         self.tittel= tittel
         self.sted= sted
         self.starttidspunkt = starttidspunkt
         self.varighet= varighet
         self.kategori= kategori
#oppgave e
    def __str__(self):
        return f"Møte: tittel:{self.tittel} ,sted:{self.sted},tidspunkt:{self.starttidspunkt}, varighet:{self.varighet}min,kategori:{self.kategori})"
#oppgave f

def avtale():
    tittel= input("Skriv inn tittelen:")
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

         


# oppgave h
def lagre_liste_m_avtaler(liste):
    with open ("avtale.txt","w",encoding="UTF-8") as fila:
        for linje in liste:
             fila.write(f"{linje.title}\n;{linje.sted}\n;{linje.starttidspunkt}\n;{linje.varighet}\n;{linje.kategori}\n")

#oppgave i
def les_avtale_fil(filnavn):
    avtale_liste= list()
    with open (filnavn,encoding="UTF-8") as fila:
        for linje in fila:
            avtale_liste.append(linje)
    
#oppgave j
def dato_i_avtale (avtale_liste,dato):
    dato_avtale= list()
    for avtale in avtale_liste:
        if dato == avtale.starttidspunkt.dato():
            dato_avtale.append(avtale)
        return dato_avtale
