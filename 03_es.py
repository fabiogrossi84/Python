""" 
Esercizio 3
Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
Un array “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese
La classe dovrà avere i seguenti metodi:
Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”. (il metodo__str__ che stampa le informazioni del 
prodotto è sempre da fare) 
Creare i metodi aumenta e diminuisco scarte per i prodotti. 
Creare il metodo applicaSconto(self, percentualeSconto) per i prodotti.
es applicaSconto(4) applicherà uno sconto al prezzo del prodotto del 4%.

es:
Costo magazzino è di 1€ per prodotto
Nel magazzino metto Palloni calcio, scorta 5
Palloni bascket socrta 15
Palloni PallaVole 10

Costo toate del meagazzino al mese è = (Scorta palloni calcio * costo Magazzino) + (Scorta palloni bascket * costo Magazzino) +
(Scorta palloni PallaVolo * costo Magazzino) => (5 * 1) + (15 * 1) + (10 * 1) = 30€ mensili

Creo Prodotto PalloneCalcio = "Adidas plus", 15, 10
se applico il metodo Sconto del 50% il nuovo prezzo sarà 7,5

"""
class GestoreMagazzino:
    costo_totale = 0
    
    def __init__(self, costo_magazzinaggio):
        self.prodotti = []
        self.costo_magazzinaggio = costo_magazzinaggio

    def aggiungi_prodotto(self, nome_prodotto):
        self.prodotti.append(nome_prodotto)

    def rimuovi_prodotto(self, nome_prodotto):
        if nome_prodotto in self.prodotti:
            self.prodotti.remove(nome_prodotto)
        else:
            print(f"Il prodotto {nome_prodotto} non è presente nel magazzino.")

    def calcola_costi_magazzinaggio(self):
        costo_totale = 0
        for prodotto in self.prodotti:
            costo_totale += prodotto.scorta * self.costo_magazzinaggio
        return costo_totale
    

class Prodotto:
    def __init__(self, nome, prezzo, scorta):
        self.nome = nome
        self.prezzo = prezzo
        self.scorta = scorta

    def aumenta_scorta(self, numero):
        self.scorta += numero

    def diminuisci_scorta(self, numero):
        if self.scorta - numero >= 0:
            self.scorta -= numero
        else:
            print("Scorta finita.")

    def applica_sconto(self, percentuale_sconto):
        self.prezzo -= (self.prezzo * percentuale_sconto / 100)

    def __str__(self):
        return f"Nome: {self.nome}, Prezzo: {self.prezzo}€, Scorta: {self.scorta}"

magazzino = GestoreMagazzino(1)

pallone_calcio = Prodotto("Pallone Calcio", 8, 5)
pallone_basket = Prodotto("Pallone Basket", 12, 15)
pallone_pallavolo = Prodotto("Pallone Pallavolo", 10, 10)

magazzino.aggiungi_prodotto(pallone_calcio)
magazzino.aggiungi_prodotto(pallone_basket)
magazzino.aggiungi_prodotto(pallone_pallavolo)


costo_mensile = magazzino.calcola_costi_magazzinaggio()
print(f"Il costo totale del magazzino al mese e' : {costo_mensile}€")

pallone_calcio.applica_sconto(50)
print(pallone_calcio)

pallone_calcio.diminuisci_scorta(3)
print(pallone_calcio)

print (magazzino) #Non so come fare il metodo STR per la class GestoreMagazzino