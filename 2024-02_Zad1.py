# UG 2024-02, zad. 1
#
# Generatorami addytywnymi 1809 są dwie liczby G - 1791 i 1800, ponieważ dodając do generatora sumę jego cyfr, otrzymamy w obu przypadkach 1809: 1791+18=1800+9=1809. 
# Która z 17 pozostałych 4-cyfrowych liczb-anagramow 0189 ma także dwa generatory addytywne i jakie sa to liczby?

import itertools
import time
import sys

def permutations(chars):
    if len(chars) <= 1:
        return [chars]

    perms = []
    for i in range(len(chars)):
        current_char = chars[i]
        remaining_chars = chars[:i] + chars[i+1:]
        for perm in permutations(remaining_chars):
            perms.append([current_char] + perm)

    return perms

def suma_cyfr(liczba):
    # Konwersja liczby na string, aby móc operować na jej cyfrach
    str_liczba = str(liczba)
    
    # Inicjacja iloczynu jako 1
    suma = 0
    
    # Iteracja po cyfrach i mnożenie ich przez siebie
    for cyfra in str_liczba:
        # Ignoruj znak minus (-) w przypadku liczb ujemnych
        if cyfra != '-':
            suma += int(cyfra)
    
    return suma

def iloczyn_cyfr(liczba):
    # Konwersja liczby na string, aby móc operować na jej cyfrach
    str_liczba = str(liczba)
    
    # Inicjacja iloczynu jako 1
    iloczyn = 1
    
    # Iteracja po cyfrach i mnożenie ich przez siebie
    for cyfra in str_liczba:
        # Ignoruj znak minus (-) w przypadku liczb ujemnych
        if cyfra != '-' and cyfra != '0':
            iloczyn *= int(cyfra)
    
    return iloczyn

def generatory_rodkow(liczba):
    # Tworzenie listy przechowującej różne liczby
    global debug_mode
    generatory = []
    for j in range (10,liczba):
        if debug_mode:
            print(j, iloczyn_cyfr(j), j+iloczyn_cyfr(j))
        if liczba == j+iloczyn_cyfr(j):
            generatory.append(j)
    return generatory


def generatory_rodkow_addytywnych(liczba):
    # Tworzenie listy przechowującej różne liczby
    global debug_mode
    generatory = []
    for j in range (1,liczba):
        if debug_mode:
            print(j, suma_cyfr(j), j+suma_cyfr(j))
        if liczba == j+suma_cyfr(j):
            generatory.append(j)
    return generatory  

def main():
    start_time = time.time()
    global debug_mode
    debug_mode = False

    characters = ['0', '1', '8', '9']
    all_permutations = permutations(characters)
    i = 0
    for perm in all_permutations:
        i = i + 1
        gens = generatory_rodkow_addytywnych(int(perm[0]+perm[1]+perm[2]+perm[3]))
        if len(gens) == 2:
            print(''.join(perm))
            print('generatory: ',gens)
    if debug_mode:
        print(i)
    
    print("--- %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
    main() 

