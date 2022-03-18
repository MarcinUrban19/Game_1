from random import randint

liczby = []
proba = 1
los = randint(1,10)
print(los)
liczba= int(input('Podaj liczbe w zakresie od 1 do 10: '))
while liczba != los:
    if liczba in liczby:
        print('Podane liczby', liczby)
        liczba = int(input('Podwales juz ta liczbe!Podaj nowa:'))

    elif liczba not in range(1,10):
        liczba = int(input('Liczba nie jest z zakresu od 1 do 10.Podaj poprawna liczba: '))
    else:
        if liczba > los:
            proba += 1
            liczby.append(liczba)
            print('Podane liczby', liczby)
            liczba = int(input('Nie udalo ci sie zgadnac!Liczba ktora chcesz zgadnac jest mniejsza.Sprobuj dalej: '))

        else:
            proba += 1
            liczby.append(liczba)
            print('Podane liczby', liczby)
            liczba = int(input('Nie udalo ci sie zgadnac!Liczba ktora chcesz zgadnac jest wieksza.Sprobuj dalej: '))


else:
    print('Brawo zgadles!Wylosowana liczba to ',los,' :)')
    print('Zgadles za ',proba,'razem!')


# def liczydlo(x,y):
#     suma = x + y
#     print('Suma tych liczb wynosi:',suma)
#
# liczydlo(2,6)

# def calculator():
#     x = int(input('Podaj liczbe x: '))
#     y = int(input('Podaj liczbe y: '))
#     dzialanie = input('Ktore dzialanie chcesz wykonac? +/- ?')
#     if dzialanie == '+':
#         wynik = x+ y
#         print('x + y =',wynik)
#     elif dzialanie == '-':
#         wynik = x-y
#         print('x - y=',wynik)
#     else:
#         print('Wpisales niepoprawny znak!')
#
#
# calculator()