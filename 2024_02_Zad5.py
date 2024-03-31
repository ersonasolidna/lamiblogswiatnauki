# UG 2024-02, zad. 5
#
# Dysponujemy czterema żetonami. Na każdym jest inna cyfra: 0, 1, 8 i 9. W kolejnych krokach bierzemy jeden, dwa, trzy lub cztery żetony i  tworzymy z nich liczby dodatnie
# 1-, 2-, 3- i 4-cyfrowe, które zapisujemy. W ten sposób powstanie 48 różnych liczb. Dzielnikiem żadnej z nich nie będzie 24, ale każda liczba z przedziału od 2 do 23 pojawi się jako
# dzielnik przynajmniej jednej liczby, a nawet cały ten przedział "obsłuży" tylko szczęść liczb: 19, 80, 901, 910, 1890, 9108.
# Które cztery liczby powinny znaleźć się na żetonach, aby tworzone w opisany sposob liczby dodatnie "obsłużyły" wszystkie dzielniki od 2 do największego możliwego?
# Wsród liczb musi być oczywiście zero ze względu na wielokrotności 10 w roli dzielników. 

import math
import time
import sys
from itertools import permutations
from itertools import combinations

def integeruj(astring):
    temp = ""
    for i in range (0,len(astring)):
        temp = temp + astring[i]
    return int(temp)

def unique(list1):
 
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list

def main():
    # podejście:
    # 1. Musimy sprawdzić każdy zbiór 4-elementowy cyfr 0-9, przy czym każdy zbiór musi zawierać 0
    # 2. Mamy już zbiór. Teraz szukamy wszystkie kombinacje 1, 2, 3 i 4-elementowe tego zbioru 4-elementowego
    # 3. Następnie dla wszystkich kombinacji analizujemy permutacje
    # 4. Na koniec łączymy wszystkie listy permutacji i usuwamy duplikaty

    start_time = time.time()
    global debug_mode
    debug_mode = False

    # Krok pierwszy: określamy zbiór 4-elementowy

    cyfry_do_wyboru = ['1','2','3','4','5','6','7','8','9']
    zbiory = list(combinations(cyfry_do_wyboru,3))
    #print(zbiory, len(zbiory))
    zbiory_docelowe = []
    for zbior in zbiory:
        zbiory_docelowe.append(zbior + ("0",))
    #print(zbiory_docelowe, len(zbiory_docelowe))

    global_max_dzielnik = 0 # w tej zmiennej przechowujemy wynik końcowy
    global_max_characters = []
    for zbior_docelowy in zbiory_docelowe:  
    
        characters = zbior_docelowy
        #characters = ['0', '1', '8', '9'] - zbiór testowy z treści zadania
        
    # Krok drugi: Kombinacje od 1 do 4-elementowe

        docelowe_komb = [] # ta zmienna będzie zawierać wszystkie kombinacje do dalszej analizy
        for liczba_elementow_komb in range (1,5):
            tymczasowe_komb = list(combinations(characters,liczba_elementow_komb))
            docelowe_komb.extend(tymczasowe_komb)
        #print("Docelowe kombinacje", docelowe_komb, len(docelowe_komb))

        # Krok trzeci: analizujemy permutacje
        liczby = []
        for doc_kombinacja in docelowe_komb:
            all_permutations = list(permutations(doc_kombinacja))
            #print("permutacje",all_permutations)
            for perm in all_permutations:
                liczba_integerowa = integeruj(perm)
                if liczba_integerowa !=0: # muszą być tylko liczby dodatnie
                    liczby.append(liczba_integerowa)

        # Krok czwarty: usuwam duplikaty
        
        liczby = unique(liczby)
        if debug_mode:
            print("Liczy unikalne dla cyfr", characters, ":",liczby, len(liczby))

        # Krok piąty: dla każdej liczby z przedziału od 2 do maksymalnego X testuję, czy jest dzielnikiem choćby jednej liczby ze zbioru "liczby unikalne" utworzonego przed chwilą
        # Wyłamaniem wtedy maksymalne X dla danego zbioru początkowych 4 cyfr
        
        current_max_dzielnik = 2
        for dzielnik in range (2,100):
            znalazlem = False    
            for liczba_u in liczby:
                #print ("liczba_u % dzielnik == 0", liczba_u, dzielnik,liczba_u % dzielnik == 0)
                if liczba_u % dzielnik == 0:            
                   current_max_dzielnik = dzielnik
                   znalazlem = True
            if znalazlem == False:
                break
        if current_max_dzielnik > global_max_dzielnik:
            global_max_dzielnik = current_max_dzielnik
            global_max_characters = characters
        if debug_mode:
            print("current_max_dzielnik", current_max_dzielnik)
        
    print("Największy zakres dzielników - od 2 do", global_max_dzielnik, "dla cyfr", global_max_characters)                       
    print("--- %s seconds ---" % (time.time() - start_time))

    # rozwiązanie:
    ##    Cyfry ('1', '4', '5', '0')
    ##    [1, 514, 4, 5, 1540, 4105, 10, 5014, 140, 14, 15, 145, 401, 5140, 405, 150, 1045, 4501, 5401, 154, 410, 540, 541, 1054, 415, 4510, 5410, 40, 41, 1450, 45, 4015, 5041, 50, 51, 54, 4150, 450, 451, 4051, 1504, 104, 105, 5104, 501, 504, 1405, 510] 48
    ##    Maaksymalny dzielnik = 32
    
if __name__ == "__main__":
    main() 

