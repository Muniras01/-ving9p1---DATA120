import datetime
#Oppgave d
class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet, kategorier):
         self.tittel= tittel
         self.sted= sted
         self.starttidspunkt = starttidspunkt
         self.varighet= varighet
         self.kategorier= []
#oppgave e
    def __str__(self):
        return f"Møte: tittel:{self.tittel} ,sted:{self.sted},tidspunkt:{self.starttidspunkt}, varighet:{self.varighet}min,kategori:{self.kategori}"
#oppgave f

# a1 = Avtale(1,2,3,4)
# a1.kategorier.append()
#oppgave f
def ny_avtale():
    tittel= input("Skriv inn tittelen:")
    sted= input("Skriv inn et sted:")
    starttidspunkt= datetime.datetime.fromisoformat(input("Skriv inn starttidspunktet:"))
    varighet= int(input("Skriv inn varigheten i minutter:"))
    kategori= input("Skriv inn kategorien:")
    return Avtale(tittel, sted, starttidspunkt, varighet, kategori)
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
    with open ("Avtale.txt","w",encoding="UTF-8") as fila:
        for linje in liste:
            fila.write(f"{linje.tittel};{linje.sted};{linje.starttidspunkt};{linje.varighet};{linje.kategori}")
            
            
#oppgave i
def les_avtale_fil(filnavn):
    avtale_liste= []
    with open (filnavn, "r", encoding="UTF-8") as fila:
        for linje in fila:
            title, sted, starttidspunkt, varighet, kategori = linje.split(";")
            starttidspunkt = datetime.datetime.fromisoformat(starttidspunkt)
            #make kategory into kategory object
            varighet = int(varighet)
            
            avtale = Avtale(title, sted, starttidspunkt, varighet, kategori)
            avtale_liste.append(avtale)
    return avtale_liste
    
#oppgave j
def dato_i_avtale (avtale_liste,dato):
    dato_avtale= []
    for avtale in avtale_liste:
        if dato == avtale.starttidspunkt.dato():
            dato_avtale.append(avtale)
        return dato_avtale

#oppgave k 
def søk_etter_streng(ei_liste_avtaler, en_streng):
    liste_ut = []
    for object in ei_liste_avtaler:
        if en_streng.lower() in object.tittel.lower():
            liste_ut.append(object)
    return liste_ut


#a function to change certain things -oppgave n
def redigere(avtalen):
    n =  int(input("1which deal do ya wanna change yo "))
    options=["1 Tittel","2 Sted","3 Dato","4 Tid","5 Varighet"]
    
    for option in options: 
        print (option)
    
    attribute=input("What attribute do you want to change?")
    
    if attribute in options[0]:
        dummy_liste_med_møter[n].tittle=input("New tititel: " )
    
    if attribute in options[1]:
        dummy_liste_med_møter[n].sted=input("New Sted: " )
    
    if attribute in options[2]:
        dummy_liste_med_møter[n].dato=input("New Dato: " )
    
    if attribute in options[3]:
        dummy_liste_med_møter[n].tid=input("New Tid: " )
    
    if attribute in options[4]:
        dummy_liste_med_møter[n].varighet=input("New Varighet: " )
#oppgave L       
def meny(): 
    ei_liste_avtaler = [ ]
    if (len(ei_liste_avtaler)== 0): 
        print("havent done any: ")
    else: lagre_liste_m_avtaler(ei_liste_avtaler)
    while True:
        valg = int(input("1. Skrive inn en ny avtale\n 2. lese inn avtaler fra fil \n 3. Skriv ut alle avtalene\n 4. skriv avtalene til fil \n 5. Delete \n 6. Make changes \n 7.Avslutt  \n Enter your choice: "))
        if valg == 1: 
            avtale = ny_avtale()
            ei_liste_avtaler.append(avtale) 
        elif valg == 2: 
            lese_avtale = les_avtale_fil("Avtale.txt")
            for avtale in lese_avtale: 
                print(avtale)
        elif valg == 3: 
            if not ei_liste_avtaler: 
                print("tomt liste")
            else:
                for avtale in ei_liste_avtaler:
                    print(avtale)
                
        elif valg ==4: 
            lagre_liste_m_avtaler(ei_liste_avtaler)
        elif valg == 5: 
            list_opp_avtaler(ei_liste_avtaler)
            y = int(input("which one do you wanna delete?:")) #opppgave m
            if input("Are you sure [y/n]")=="y":
                del ei_liste_avtaler[y]
            
        elif valg == 6: 
            redigere(les_avtale_fil)
            
        elif valg == 7: 
             print("avslutt") 
             break
     
#Del2
#c
class Kategori:
    def __init__(self,en_id,navn,prioritet):
        self.en_id=en_id
        self.navn=navn
        self.prioritet= prioritet
        return f"Kateogi:en_id:{self.en_id} ,navn:{self.navn},prioritet:{self.prioritet}"
    
#d
    def leser_fra_brukern():
        en_id=input("id: ")
        navn= input("Skriv in navn: ")
        prioritet= input("Skriv inn prioritet: ")
        return Kategori(en_id,navn,prioritet)
#g   
class Sted:
    def __init__(self,ID_sted,navn_sted,gateadress,postnummer,poststed): 
        self.ID_sted=ID_sted
        self.navn_sted=navn_sted
        self.gateadress=gateadress
        self.postnummer=postnummer
        self.poststed=poststed
        
    def __str__(self):
        return f"Sted: ID_sted:{self.ID_sted},navn_sted:{self.navn_sted},gateadress:{self.gateadress},postnummer:{self.postnummer},poststed:{self.poststed}"
    
#h
def nytt_sted():
    ID_sted= input("ID: ")
    navn_sted= input("Skriv in navn: ")
    gateadress= input("Skriv inn gateadress: ")
    postnummer=int(input("Skriv inn postnummer: "))
    poststed=input("Skriv inn poststed: ")
    return Sted(ID_sted,navn_sted,gateadress,postnummer,poststed)

#i
def lagre_sted(sted):
    with open("sted.txt","w",encoding="UTF-8") as fil:
        for linje in sted:
            fil.write(f"{linje.ID_sted};{linje.navn_sted};{linje.gateadress};{linje.postnummer};{linje.poststed}")
        
        
def les_sted():
    sted_liste=[]
    with open("sted.txt","r",encoding="UTF-8") as fila:
        for linje in fila:
            ID_sted,navn_sted,gateaddress,postnummer,poststed = linje.split(";")
            sted=Sted(ID_sted, navn_sted, gateadress, postnummer, poststed)
            sted_liste.append(sted)
    return sted_liste 

                
#j
def skriv_ut_sted(stedet):
    for sted in stedet:
        print(sted)
        
stedet=list(les_sted())
skriv_ut_sted(stedet)
    
    
    
    
if __name__=="__main__":
    meny() 
    
 #Oppgave k
    def legger_til_kategori(self, kategori):
        self.kategori.append(kategori)

#Oppgave l
def lagre_liste_m_avtaler(liste,filnavn="Avtale.txt"):
    with open (filnavn,"w",encoding="UTF-8") as fila:
        for linje in liste:
            kategori_navn= ""
            for kategori in linje.kategorier:
                kategori_navn += str(kategori)
            fila.write(f"{linje.tittel};{linje.sted};{linje.starttidspunkt};{linje.varighet};{kategori_navn}")

#Oppgvae m
kategori= list()
def meny():
    ei_liste_avtaler = [ ]
    ei_liste_avtaler.append(Avtale("møte2", "Oslo", "2022-09-15 12:15:00", "60", "politikk"))
    #if (len(ei_liste_avtaler)== 0):
     #   print("havent done any: ")
    #else: lagre_liste_m_avtaler(ei_liste_avtaler)
    while True:
        valg = int(input("1. Skrive inn en ny avtale\n 2. lese inn avtaler fra fil \n 3. Skriv ut alle avtalene\n 4. skriv avtalene til fil \n 5. Delete \n 6. Make changes \n 7.Legge til kategorier  \n 8.Legge til steder \n9.Avslutt  \n Enter your choice: "))
        if valg == 1:
            avtale = ny_avtale()
            ei_liste_avtaler.append(avtale)
        elif valg == 2:
            lese_avtale = les_avtale_fil("Avtale.txt")
            for avtale in lese_avtale:
                print(avtale)

        elif valg == 3:
            if  len(ei_liste_avtaler) == 0:
                print("tomt liste")
            else:
                for avtale in ei_liste_avtaler:
                    print(avtale)

        elif valg ==4:
            ei_liste_avtaler.append(Avtale("møte2", "Oslo", "2022-09-15 12:15:00", "60", ["politikk"]))
            lagre_liste_m_avtaler(ei_liste_avtaler)

        elif valg == 5:
            list_opp_avtaler(ei_liste_avtaler)
            y = int(input("which one do you wanna delete?:"))
            if input("Are you sure [y/n]")=="y":
                del ei_liste_avtaler[y]
        elif valg == 6:
            redigere(les_avtale_fil)

       elif valg == 7:
         nykategori()

        elif valg == 8:
        les_sted ()

        elif valg == 9:
             print("avslutt")
             break
