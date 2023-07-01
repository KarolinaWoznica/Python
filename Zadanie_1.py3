import random

while True:
    lista = []

    for x in range(100):
        y = random.randint(64,99)
        lista.append(y)

    print(lista)   

    lista_nieparzyste = []
    lista_parzyste = []

    for i in lista:
        if i%2!=0:
            lista_nieparzyste.append(i)
        else:
            lista_parzyste.append(i) 

    print(lista_nieparzyste)
    print(lista_parzyste)

    suma_nieparzyste = 0
    suma_parzyste = 0
    for i in lista_nieparzyste:
        suma_nieparzyste += i
    for j in lista_parzyste:
        suma_parzyste += j

    print(suma_nieparzyste)
    print(suma_parzyste)    

    if suma_nieparzyste > suma_parzyste: 
        print("suma wartości elementów jest większa w zbiorze liczb nieparzystych ")
    else:
        print("suma wartości elementów jest większa w zbiorze liczb parzystych ")

    średnia_nieparzyste = suma_nieparzyste / len(lista_nieparzyste)
    print("średnia zbioru liczb nieparzystych:", średnia_nieparzyste)

    średnia_parzyste = suma_parzyste / len(lista_parzyste)
    print("średnia zbioru liczb parzystych:", średnia_parzyste)

    lista_parzyste.sort()
    lista_nieparzyste.sort(reverse= True)

    print(lista_parzyste)
    print(lista_nieparzyste)

    uchwyt = open('plik_do_zapisu.txt', 'a')
    uchwyt.write(str(lista) + '\n')
    uchwyt.write(str(lista_nieparzyste) + '\n')
    uchwyt.write(str(lista_parzyste) + '\n')
    if suma_nieparzyste > suma_parzyste: 
        uchwyt.write("suma wartości elementów jest większa w zbiorze liczb nieparzystych\n")
    else:
        uchwyt.write("suma wartości elementów jest większa w zbiorze liczb parzystych\n")
    uchwyt.write("średnia zbioru liczb nieparzystych:" + str(średnia_nieparzyste) + '\n')
    uchwyt.write("średnia zbioru liczb parzystych:" + str(średnia_parzyste) + '\n')
    uchwyt.close()

    czy_kontynuować = False
    while True:
        print("Czy chcesz ponownie losować liczby?")
        wybór = input()
        if wybór == 'No' or wybór == 'no' or wybór == 'Nie' or wybór == 'nie':
            print("Uzytkownik nie chce losować liczb ponownie.")
            czy_kontynuować = False
            break
        elif wybór == 'Yes' or wybór == 'yes' or wybór == 'Tak' or wybór == 'tak':
            czy_kontynuować = True
            break
        else:
            print('Nieznane polecenie.')
            continue
    if czy_kontynuować == True:
        continue
    else:
        break
    
print("Koniec")
        
        
     

