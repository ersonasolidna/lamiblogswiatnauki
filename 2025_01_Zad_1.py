# UG 2025-01, zad. 1
#
# Odtworzenie zapisu rozkładania liczby na czynniki pierwsze 

import time

def rozloz_na_czynniki_pierwsze(n: int):
    """
    Zwraca krotkę:
      (lista_czynnikow_pierwszych, lista_wartosci_posrednich)
    gdzie:
      - lista_czynnikow_pierwszych to lista kolejno znalezionych czynników pierwszych
      - lista_wartosci_posrednich to wartości n po każdym podziale przez aktualny czynnik
    """
    czynniki = []
    wartosci_posrednie = []
    
    # Sprawdzamy wielokrotne dzielenie przez 2
    while n % 2 == 0:
        n //= 2
        czynniki.append(2)
        wartosci_posrednie.append(n)
    
    # Sprawdzamy potencjalne dzielniki nieparzyste od 3 w górę
    dzielnik = 3
    while dzielnik * dzielnik <= n:
        while n % dzielnik == 0:
            n //= dzielnik
            czynniki.append(dzielnik)
            wartosci_posrednie.append(n)
        dzielnik += 2
    
    # Jeśli po powyższej pętli n > 1, to znaczy, że jest on już liczbą pierwszą
    if n > 1:
        czynniki.append(n)
        n //= n  # ustawiamy n na 1
        wartosci_posrednie.append(n)
    
    return czynniki, wartosci_posrednie

def main():

    j = 0
    start_time = time.time()
    # Przykładowe wywołanie
    liczba = 4810
    for liczba in range (40000,100000):
        czynniki, wartosci = rozloz_na_czynniki_pierwsze(liczba)
        if len(czynniki) == 5:
            if czynniki[0] < 10 and czynniki[1] < 10 and czynniki[2] > 9 and czynniki[2] < 100 and czynniki[3] > 9 and czynniki[3] < 100 and czynniki[4] > 9 and czynniki[4] < 100:
                if str(czynniki[2])[0] == '2' and str(wartosci[0])[4] == '2':
                    print("Liczba startowa: ", liczba)
                    print("Czynniki pierwsze:", czynniki)
                    print("Wartości pośrednie:", wartosci)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()

