import openpyxl
import os
from datetime import date

class Product:
    lista = []

    def __init__(self, sifra, naziv, opis, cena, stanje):
        self.sifra = sifra
        self.naziv = naziv
        self.opis = opis
        self.cena = float(cena)
        self.stanje = stanje
        self.kolicina = ""

    def __str__(self):
        return f"Šifra proizvoda : {self.sifra}\n" \
               f"Naziv proizvoda : {self.naziv}\n" \
               f"Opis proizvoda : {self.opis}\n" \
               f"Cena : {self.cena}\n" \
               f"Na stanju : {self.stanje}\n-----------"

    def ucitaj_proizvode(self):
        wb = openpyxl.load_workbook("Bookstore.xlsx")
        sheet = wb['Sheet1']
        proizvodi = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            sifra = row[0]
            naziv = row[2]
            opis = row[1]
            cena = float(row[3])
            stanje = row[4]
            p = Product(sifra, naziv, opis, cena, stanje)
            proizvodi.append(p)
        self.lista = proizvodi

    def pretraga_proizvoda_po_imenu(self, naziv):
        for i in self.lista:
            if i.naziv.lower() == naziv.lower():
                return f"Naziv proizvoda : {i.naziv}\n" \
                       f"Opis proizvoda : {i.opis}\n" \
                       f"Cena : {i.cena}\n" \
                       f"Na stanju : {i.stanje}\n-----------"

        else:
            return 'Nije pronađen nijedan proizvod pod tim nazivom'


class Korpa:
    def __init__(self):
        self.lista_proizvoda = []
        self.ukupna_cena = 0
        self.date = date.today()

    def dodaj_proizvod(self, proizvod, kolicina):
       proizvod.kolicina = kolicina
       self.lista_proizvoda.append(proizvod)
       return "Dodat proizvod u korpu"

    def ukloni_proizvod(self, proizvod):
        if proizvod in self.lista_proizvoda:
            self.lista_proizvoda.remove(proizvod)
            return "Proizvod je uklonjen iz korpe."
        else:
            return "Proizvod nije u korpi."

    def pregled_korpe(self):
        if len(self.lista_proizvoda) == 0:
            return "/"
        else:
            korpa = []
            for proizvod in self.lista_proizvoda:
                korpa.append(proizvod.naziv)
            return korpa

    def racun(self):
        racun = 0
        box=""
        if len(self.lista_proizvoda) == 0:
            return f"Nemate proizvode u korpi, vaš racun je {racun}"
        else:
            for proizvod in self.lista_proizvoda:
                racun += proizvod.cena * float(proizvod.kolicina)
                box=box + proizvod.naziv+ " " +"x"+ " "+ proizvod.kolicina+" "+ "kom" +"\n" 
            return f"{box}\n-------\nVas racun iznsi {racun} din"

    def stampaj_racun(self):
        a = open("racun.txt","w")
        a.close()
        a = open("racun.txt","a")
        print(f"Datum izvestaja '{self.date}'",file = a)
        for i in self.lista_proizvoda:
            staro_stanje = i.stanje
            novo_stanje=staro_stanje-int(i.kolicina)
            for p in P.lista:
                if p.sifra == i.sifra:
                    p.stanje = novo_stanje
                    break
            print(f"Sifra proizvoda:{i.sifra}\nKolicina:{i.kolicina}\n Naziv:{i.naziv}\n------\n{K.racun()}", file = a)
        a.close()


P = Product("","","",0.0,"")
P.ucitaj_proizvode()
K= Korpa()