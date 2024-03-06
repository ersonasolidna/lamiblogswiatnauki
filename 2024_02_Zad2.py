# UG 2024-02, zad. 2
#
# 1089 i 2178 wyczerpują, zbiór liczb 4-cyfrowych, których "wspaki" są ich wielokrotnościami. Odwrotna, zależność nie jest jednak
# prawdziwa, czyli 9801 i 8712 nie stanowią calego zbioru liczb 4-cyfrowych podzielnych przez swoje "wspaki". Proszę
# podać przynajmniej jedną inną 4-cyfrową liczbę (złożoną z różnych cyfr), należącą do tego drugiego większego zbioru

# ODP:
# Poza 9801 i 8712, są jeszcze trzy takie liczby: 5610, 5940 i 8910.
# Ich cechą wspólną jest to, że ich wspaki zaczynają się od 0 i tworzą de facto liczby 3-cyfrowe (np. 5610 modulo 165 = 0).
# To też wyjaśnia, dlaczego odwrotna zależność, o której mowa w zadaniu, nie jest prawdziwa.

import time

def wspak(liczba):
    # Konwersja liczby na string, aby móc operować na jej cyfrach
    str_liczba = str(liczba)
    
    # Inicjacja iloczynu jako 1
    return int(str_liczba[3] + str_liczba[2] + str_liczba[1] + str_liczba[0])

def unikalne(liczba):
    cyfry = set(str(liczba))  # Tworzymy zbiór unikalnych cyfr w liczbie
    return len(cyfry) == 4
  
def main():
    start_time = time.time()
    global debug_mode
    debug_mode = False

    for liczba in range (1000,9999):
        if unikalne(liczba):
            if liczba % wspak(liczba) == 0:
               print(liczba, wspak(liczba), liczba % wspak(liczba))
            
    print("--- %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
    main() 

