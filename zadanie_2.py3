# Spekulacje ile uźytkownik moze zaoszczędzić przez rok

import matplotlib.pyplot as plt
import numpy as np

class miesięczny_dochód_i_wydatki:
    miesiące = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień','wrzesień', 'październik', 'listopad', ' grudzień' ]
    
    def pobierz_miesięczne_dochody(self):
        miesięczne_dochody = []
        for x in range(12):
            while True:
                try:
                    y = float(input("Podaj dochód z miesiąca " + self.miesiące[x] + ' '))
                except ValueError:
                    print("Wprowadź poprawną wartość")
                else:
                    if y >= 0:
                        miesięczne_dochody.append(y)
                        break
                    else:
                        print("Wprowadź wartość nieujemną")
                        
        return miesięczne_dochody
    def pobierz_miesięczne_wydatki(self):
        miesięczne_wydatki = []
        for x in range(12):
            while True:
                try:
                    y = float(input("Podaj wydatki z miesiąca " + self.miesiące[x] + ' '))
                except ValueError:
                    print("Wprowadź poprawną wartość!")
                else:
                    if y >= 0:
                        miesięczne_wydatki.append(y)
                        break
                    else:
                        print("Wprowadź wartość nieujemną")
                        
        return miesięczne_wydatki

class dzialania_na_danych:
    miesiące = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień','wrzesień', 'październik', 'listopad', ' grudzień' ]
    miesięczne_dochody = []
    miesięczne_wydatki = []
    suma_miesięczne_dochody = 0
    suma_miesięczne_wydatki = 0  
    średnia_miesięczne_dochody = 0
    średnia_miesięczne_wydatki = 0
    oszczędności = 0
    średnia_oszczędności = 0
    najmniejszy_dochód = 0
    najwiekszy_dochód = 0
    najmniejszy_wydatek = 0
    najwiekszy_wydatek = 0
    
    def __init__(self,miesięczne_dochody, miesięczne_wydatki):
        self.miesięczne_dochody = miesięczne_dochody
        self.miesięczne_wydatki = miesięczne_wydatki
    def get_miesięczne_dochody(self):
        return self.miesięczne_dochody
    def get_miesięczne_wydatki(self):
        return self.miesięczne_wydatki
    def get_suma_miesięczne_dochody(self):
        return self.suma_miesięczne_dochody
    def get_suma_miesięczne_wydatki(self):
        return self.suma_miesięczne_wydatki
    def get_średnia_miesięczne_dochody(self):
        return self.średnia_miesięczne_dochody
    def get_średnia_miesięczne_wydatki(self):
        return self.średnia_miesięczne_wydatki
    def get_oszczędności(self):
        return self.oszczędności
    def get_średnia_oszczędności(self):
        return self.średnia_oszczędności
    def get_najmniejszy_dochód(self):
        return self.najmniejszy_dochód
    def get_najwiekszy_dochód(self):
        return self.najwiekszy_dochód
    def get_najmniejszy_wydatek(self):
        return self.najmniejszy_wydatek
    def get_najwiekszy_wydatek(self):
        return self.najwiekszy_wydatek    
    def set_miesięczne_dochody(self, m_dochody):
        self.miesięczne_dochody = m_dochody
    def set_miesięczne_wydatki(self, m_wydatki):
        self.miesięczne_wydatki = m_wydatki
    
    def oblicz_statystki(self):
        self.suma_miesięczne_dochody = 0
        self.suma_miesięczne_wydatki = 0   
        for i in self.miesięczne_dochody:
                self.suma_miesięczne_dochody+= i
        for j in self.miesięczne_wydatki:
                self.suma_miesięczne_wydatki+= j

        print("Suma miesiecznych dochodów: ", self.suma_miesięczne_dochody)
        print("Suma miseięcznych wydatków: ", self.suma_miesięczne_wydatki)  

        self.średnia_miesięczne_dochody = self.suma_miesięczne_dochody / len(self.miesięczne_dochody)
        print("średnia miesięcznych dochodów", self.średnia_miesięczne_dochody)

        self.średnia_miesięczne_wydatki = self.suma_miesięczne_wydatki/ len(self.miesięczne_wydatki)
        print("średnia miesięcznych wydatków", self.średnia_miesięczne_wydatki)

        self.oszczędności = self.suma_miesięczne_dochody - self.suma_miesięczne_wydatki
        if self.oszczędności > 0: 
            print("Uzytkownik zaoszczędził: " + str(self.oszczędności))
        elif self.oszczędności == 0:
            print("Uzytkownik jest na zero")
        else:
            print("Uzytkownik jest na stracie: " + str(self.oszczędności))

        self.średnia_oszczędności = self.oszczędności/12
        if self.średnia_oszczędności > 0: 
            print("Uzytkownik średnio miesięcznie zaoszczędził: " + str(self.średnia_oszczędności))
        elif self.średnia_oszczędności == 0:
            print("Uzytkownik średnio miesięcznie nic nie zaoszczędził")
        else:
            print("Uzytkownik średnio miesięcznie stracił: " + str(self.średnia_oszczędności))

        self.najmniejszy_dochód = 0
        self.najwiekszy_dochód = 0
        for i in range(12):     
            if self.miesięczne_dochody[self.najmniejszy_dochód] > self.miesięczne_dochody[i]: 
                self.najmniejszy_dochód = i 
            if self.miesięczne_dochody[self.najwiekszy_dochód] < self.miesięczne_dochody[i]:
                self.najwiekszy_dochód = i

        print ("najmniejszy dochód:", self.miesiące[self.najmniejszy_dochód], self.miesięczne_dochody[self.najmniejszy_dochód])
        print ("największy dochód:", self.miesiące[self.najwiekszy_dochód], self.miesięczne_dochody[self.najwiekszy_dochód])

        self.najmniejszy_wydatek = 0
        self.najwiekszy_wydatek = 0
        for i in range(12):     
            if self.miesięczne_wydatki[self.najmniejszy_wydatek] > self.miesięczne_wydatki[i]: 
                self.najmniejszy_wydatek = i 
            if self.miesięczne_wydatki[self.najwiekszy_wydatek] < self.miesięczne_wydatki[i]:
                self.najwiekszy_wydatek = i

        print ("najmniejsze wydatki:", self.miesiące[self.najmniejszy_wydatek], self.miesięczne_wydatki[self.najmniejszy_wydatek])
        print ("największe wydatki:", self.miesiące[self.najwiekszy_wydatek], self.miesięczne_wydatki[self.najwiekszy_wydatek])
        
class wizualizacja_danych :
    miesiące = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień','wrzesień', 'październik', 'listopad', ' grudzień' ]
    miesięczne_dochody = []
    miesięczne_wydatki = []

    def wykres(self, miesięczne_dochody, miesięczne_wydatki, najmnieszy_dochód, najmniejszy_wydatek, najwiekszy_wydatek, najwiekszy_dochód,
               suma_miesięczne_dochody, suma_miesięczne_wydatki, oszczędności, średnia_miesięczne_dochody, średnia_miesięczne_wydatki ):
        x = self.miesiące
        y = miesięczne_wydatki
        z = miesięczne_dochody
        index = np.arange(len(x))
        width = 0.4
        plt.bar(index - width/2, y, width, label = "wydatki")
        plt.bar(index + width/2, z, width, label = "dochody")
        plt.xticks(index, x)
        plt.xlabel("Miesiące")
        plt.ylabel("Wysokość miesięcznego wydatku")
        plt.title("Miesięczne wydatki i dochody")
        plt.legend()
        plt.show()
        
        t = ["min dochód", "min wydatek", "max wydatek", "max dochód"]
        w = [miesięczne_dochody[najmnieszy_dochód], miesięczne_wydatki[najmniejszy_wydatek], miesięczne_wydatki[najwiekszy_wydatek], miesięczne_dochody[najwiekszy_dochód]]
        plt.bar(t, w)
        plt.ylabel("Kwota")
        plt.title("Najmniejsze i najwieksze miesięczne wydatki i dochody")
        plt.show()
        
        k = ["suma dochodów", "suma wydatków", "oszczednosci(róznica dochodów i wydatków)"]
        l = [suma_miesięczne_dochody, suma_miesięczne_wydatki, oszczędności ]
        plt.bar(k, l)
        plt.ylabel("Kwota")
        plt.title("Podsumowanie roczne")
        plt.show()
        
        r = ["średnie miesięczne dochody", "średnie miesięczne wydatki"]
        v = [średnia_miesięczne_dochody, średnia_miesięczne_wydatki]
        plt.pie(v, labels=r, autopct='%.2f')
        plt.show()

        
n = miesięczny_dochód_i_wydatki() 
miesięczne_dochody = n.pobierz_miesięczne_dochody()
miesięczne_wydatki = n.pobierz_miesięczne_wydatki()

print('Miesięczne dochody:', miesięczne_dochody)
print('Miesięczne wydatki:', miesięczne_wydatki)
k = dzialania_na_danych(miesięczne_dochody, miesięczne_wydatki)
k.oblicz_statystki()

l = wizualizacja_danych()
l.wykres(miesięczne_dochody, miesięczne_wydatki, k.get_najmniejszy_dochód(), k.get_najmniejszy_wydatek(), 
         k.get_najwiekszy_wydatek(), k.get_najwiekszy_dochód(), k.get_suma_miesięczne_dochody(), k.get_suma_miesięczne_wydatki(), k.get_oszczędności(),
         k.get_średnia_miesięczne_dochody(), k.get_średnia_miesięczne_wydatki())

           