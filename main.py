liczba_prac=int(input())

class Pracownik:
    def __init__(self, imie, wynagrodzenie_brutto):
        self.imie=imie
        self.wynagrodzenie_brutto=int(wynagrodzenie_brutto)
        self.koszt_przychodu=112.25

    def policz_skladki(self):
        emerytalna=round(self.wynagrodzenie_brutto*0.0976,2)
        rentowa=round(self.wynagrodzenie_brutto*0.0150,2)
        chorobowa=round(self.wynagrodzenie_brutto*0.0245,2)
        wynagrodzenie_pomniejszone=round(self.wynagrodzenie_brutto - (emerytalna+rentowa+chorobowa),2)
        skladka_zdrowotna = round(wynagrodzenie_pomniejszone *0.09 , 2)
        podstawa_podatku_dochodowego=round(((wynagrodzenie_pomniejszone-self.koszt_przychodu)*0.18 -46.33),2)
        skladka_zdrowotna_do_odliczenia=round(wynagrodzenie_pomniejszone*0.0775,2)
        podatek_dochodowy=round((podstawa_podatku_dochodowego-skladka_zdrowotna_do_odliczenia),0)
        wynagrodzenie_netto=round(wynagrodzenie_pomniejszone-skladka_zdrowotna-podatek_dochodowy,2)
        x=round(self.wynagrodzenie_brutto*0.065,2)
        fgsp=round(self.wynagrodzenie_brutto*0.001,2)
        wypadkowa=round(self.wynagrodzenie_brutto*0.0193,2)

        skladki_pracodawcy=round(emerytalna+x+wypadkowa+chorobowa+fgsp,2)
        koszt_pracodawcy=round(skladki_pracodawcy+self.wynagrodzenie_brutto,2)
        self.laczny_koszt=round(self.wynagrodzenie_brutto+skladki_pracodawcy,2)
        #wynagrodzenie_netto="{:.2f}".format(wynagrodzenie_netto)
        #skladki_pracodawcy="{:.2f}".format(skladki_pracodawcy)
        return(self.imie+ " {:.2f} {:.2f} {:.2f}").format(wynagrodzenie_netto, skladki_pracodawcy, koszt_pracodawcy)
    def zwroc_laczny_koszt(self):
        return self.laczny_koszt
      

lista=[]
laczny_koszt=0.00
for i in range(liczba_prac):
    dane_pracownika=input().split(" ")
    pracownik=Pracownik(dane_pracownika[0], dane_pracownika[1])
    lista.append(pracownik.policz_skladki())
    laczny_koszt+=pracownik.zwroc_laczny_koszt()
for wynik in lista:
    print(wynik)

print(("{:.2f}").format(laczny_koszt))
