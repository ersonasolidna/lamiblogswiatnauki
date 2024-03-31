# UG 2024-02, zad. 3
#
# Która z osiemnastu 4-cyfrowych liczb-anagramów 0189 może być zapisana jako suma kolejnych liczb na najwięcej sposobów? I pytanie dodatkowe - ile?

import itertools
import time
import numpy as np

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


def main():
    start_time = time.time()
    global debug_mode
    debug_mode = False

    characters = ['0', '1', '8', '9']
    all_permutations = permutations(characters)
    i = 0

    wyniki = np.zeros((500,3))
    if debug_mode:
        print ("dimensions",wyniki.ndim)
    
    anagramy = []
    for perm in all_permutations:
        if perm[0] != "0":
            i = i + 1
            aktualny_anagram = int(perm[0]+perm[1]+perm[2]+perm[3])        
            anagramy.append(aktualny_anagram)
    
    kr = 0
    r = 0
    for st in range (1,4906):
        suma_dotychczasowych = 0        
        for k in range (st,4906):
            kr = kr + 1
            suma_dotychczasowych = suma_dotychczasowych + k
            if suma_dotychczasowych in (anagramy):
                #print(st,"+...+",k,"=", suma_dotychczasowych)
                wyniki[r,0]= st
                wyniki[r,1]= k
                wyniki[r,2]= suma_dotychczasowych
                r = r + 1
    if debug_mode:
        print("liczba wierszy do macierzy:",r)

    # przycinam liczbę wierszy:
    wyniki = np.resize(wyniki, (r,3))
    wyniki_int = wyniki.astype(int)

    # porosortowane po postatniej kolumnie:
    wyniki_int_sort = wyniki_int[wyniki_int[:, 2].argsort()]
    if debug_mode:
        print( wyniki_int_sort[:,2])

    # wyswietlanie liczby dzielnikow dla kazdej liczby-anagramu
    wyniki_pivot = np.zeros((30,2))
    r = 0
    aktualny_wyb = 0
    aktualny_liczba = 0
    
    for kr in wyniki_int_sort[:,2]:
        if aktualny_wyb != kr:
            # wyswietl poprzedni:
            if aktualny_wyb !=0:
                if debug_mode:
                    print(aktualny_wyb, aktualny_liczba)
                wyniki_pivot[r,0] = aktualny_wyb
                wyniki_pivot[r,1] = aktualny_liczba
                r = r +1
            aktualny_wyb = kr
            aktualny_liczba = 1
        else:
            aktualny_liczba = aktualny_liczba + 1
    # przycinanie zer:
    wyniki_pivot = np.resize(wyniki_pivot, (r,2))
    wyniki_pivot_int = wyniki_pivot.astype(int)
    
    print("Liczba-anagram", "Liczba dzielników")
    wyniki_pivot_sort = wyniki_pivot_int[wyniki_pivot_int[:, 1].argsort()]
    print(wyniki_pivot_sort)
    print("Spośród 4-cyfrowych anagramów 0189, liczba ", wyniki_pivot_sort[-1][0],"może być zapisana na najwięcej, bo ",wyniki_pivot_sort[-1][1]," sposoby jako suma kolejnych liczb.")
    print("--- %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
    main() 

