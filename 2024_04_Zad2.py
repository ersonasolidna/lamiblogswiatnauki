# UG 2024-04, zad. 2
#
# Suma szcześcianów cyfr liczby A równa jest kwadratowi sumy cyfr liczby A, a także sumie cyfr kwadratu liczby A.
# Jaką liczbą jest A, jeśli nie ma w niej zera ani jedynki.


import time

def suma_szescianow_cyfr(liczba):
    suma = 0
    while liczba > 0:
        cyfra = liczba % 10
        suma += cyfra ** 3
        liczba //= 10
    return suma


def kwadrat_sumy_cyfr(liczba):
    suma_cyfr = sum(int(cyfra) for cyfra in str(liczba))
    return suma_cyfr ** 2

def suma_cyfr_kwadratu(liczba):
    kwadrat = liczba ** 2
    suma_cyfr_kwadratu = sum(int(cyfra) for cyfra in str(kwadrat))
    return suma_cyfr_kwadratu

def czy_zawiera_0_lub_1(liczba):
    for cyfra in str(liczba):
        if cyfra in ['0', '1']:
            return True
    return False

def main():
    start_time = time.time()
    global debug_mode
    debug_mode = False

    for licz in range (2,999):
        if not czy_zawiera_0_lub_1(licz):
            if kwadrat_sumy_cyfr(licz) == suma_cyfr_kwadratu(licz) == suma_szescianow_cyfr(licz):
                print("Liczba = ", licz, "Suma sześcianów cyfr, kwadrat sumy cyfr i suma cyfr kwadratu = ",kwadrat_sumy_cyfr(licz))
    print("--- %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
    main() 

