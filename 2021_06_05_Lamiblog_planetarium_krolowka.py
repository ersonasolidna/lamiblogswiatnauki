# Łamiblog 2021-05-06, Planetarium - królówka

import time, math
import numpy as np

def czy_wystpuje_slowo(macierz, slowo):

    # najpierw szukamy pierwszej litery słowa "slowo" w macierzy "macierz"
    
    result =  np.where(macierz == slowo[0])
        
    for el in range(1,len(slowo)):
        
        new_result =  np.where(macierz == slowo[el])
        #print ("Adres poprzedniej litery:", result[0][0], result[1][0])
        #print ("Adres kolejnej litery:", new_result[0][0], new_result[1][0])
        if czy_sa_sasiadami(new_result, result) == False:
            return False
        result = new_result
    return True
    
def czy_sa_sasiadami(new_result, result):
    
    if abs(new_result[0][0] - result[0][0]) <=1 and abs(new_result[1][0] - result[1][0]) <=1:
        return True
    return False

def main():

    """

    a1 a2 a3 a4
    b1 b2 b3 b4
    c1 c2 c3 c4
    
    A E I K M N R S U W  Y  Z
    1 2 3 4 5 6 7 8 9 10 11 12

    MERKURY = 5,2,7,4,9,7,11
    WENUS = 10,2,6,9,8
    ZIEMIA = 12,3,2,5,3,1
    MARS = 5,1,7,8
    
    """

    
    start = time.time()

  
    mars = np.array([5,1,7,8])
    merkury = np.array([5,2,7,4,9,7,11])
    wenus = np.array([10,2,6,9,8])    
    ziemia = np.array([12,3,2,5,3,1])

    znajdki = np.zeros([479001601,4], dtype=bool)
    znajdki_obiecujace = np.zeros([200,3,4])
    krolowka = np.zeros([479001601,3,4], dtype='int8')
    #print(krolowka)

    planety = [mars, merkury,wenus,ziemia]
    nazwy = ["mars","merkury","wenus","ziemia"]

    liczba_roznych_liter = 12
    znaleziono = 0
    licz_planety = 0
    licz_rozw = 0
    
    licz = 0
    #for a1 in range (1, liczba_roznych_liter+1):
    for a1 in [4,5,8,10,11,12]: # ograniczenie do kilku cyfr w celu przyspieszenia algorytmu
        #for a2 in range (1, liczba_roznych_liter+1):
        for a2 in [1,2,3,4,5,6,7,8,9,10,11,12]:
            if a2 != a1:
                #print("Progress: ", a1*100/liczba_roznych_liter+a2*(1/liczba_roznych_liter)*(1/liczba_roznych_liter)*100)
                #for a3 in range (1, liczba_roznych_liter+1):
                for a3 in [1,2,3,4,5,6,7,8,9,10,11,12]:
                    if (a3 != a2) and (a3 != a1):
                        #for a4 in range (1, liczba_roznych_liter+1):
                        for a4 in [4,5,8,10,11,12]:
                            if (a4 != a3) and (a4 != a2) and (a4 != a1):                                 
                                 #for b1 in range (1, liczba_roznych_liter+1):
                                 for b1 in [3,4,5,8,9]:
                                     if (b1 != a4) and (b1 != a3) and (b1 != a2) and (b1 != a1):
                                         #for b2 in range (1, liczba_roznych_liter+1):
                                         for b2 in [2,3,5,7]:
                                             if (b2 != b1) and (b2 != a4) and (b2 != a3) and (b2 != a2) and (b2 != a1):
                                                 #for b3 in range (1, liczba_roznych_liter+1):
                                                 for b3 in [2,3,5,7]:
                                                     if (b3 != b2) and (b3 != b1) and (b3 != a4) and (b3 != a3) and (b3 != a2) and (b3 != a1):
                                                         #for b4 in range (1, liczba_roznych_liter+1):
                                                         for b4 in [3,4,5,8,9]:
                                                             if (b4 != b3) and (b4 != b2) and (b4 != b1) and (b4 != a4) and (b4 != a3) and (b4 != a2) and (b4 != a1):   
                                                                 #for c1 in range (1, liczba_roznych_liter+1):
                                                                 for c1 in [4,5,8,10,11,12]:
                                                                     if (c1 != b4) and (c1 != b3) and (c1 != b2) and (c1 != b1) and (c1 != a4) and (c1 != a3) and (c1 != a2) and (c1 != a1):
                                                                         #for c2 in range (1, liczba_roznych_liter+1):
                                                                         for c2 in [1,2,3,4,5,6,7,8,9,10,11,12]:
                                                                             if (c2 != c1) and (c2 != b4) and (c2 != b3) and (c2 != b2) and (c2 != b1) and (c2 != a4) and (c2 != a3) and (c2 != a2) and (c2 != a1):
                                                                                 #for c3 in range (1, liczba_roznych_liter+1):
                                                                                 for c3 in [1,2,3,4,5,6,7,8,9,10,11,12]:
                                                                                     if (c3 != c2) and (c3 != c1) and (c3 != b4) and (c3 != b3) and (c3 != b2) and (c3 != b1) and (c3 != a4) and (c3 != a3) and (c3 != a2) and (c3 != a1):
                                                                                        #for c4 in range (1, liczba_roznych_liter+1):
                                                                                        for c4 in [4,5,8,10,11,12]:
                                                                                            if (c4 != c3) and (c4 != c2) and (c4 != c1) and (c4 != b4) and (c4 != b3) and (c4 != b2) and (c4 != b1) and (c4 != a4) and (c4 != a3) and (c4 != a2) and (c4 != a1):                                                                                                                                                                           
                                                                                                licz += 1
                                                                                                krolowka[licz,0,0] = a1
                                                                                                krolowka[licz,0,1] = a2
                                                                                                krolowka[licz,0,2] = a3
                                                                                                krolowka[licz,0,3] = a4
                                                                                                krolowka[licz,1,0] = b1
                                                                                                krolowka[licz,1,1] = b2
                                                                                                krolowka[licz,1,2] = b3
                                                                                                krolowka[licz,1,3] = b4
                                                                                                krolowka[licz,2,0] = c1
                                                                                                krolowka[licz,2,1] = c2
                                                                                                krolowka[licz,2,2] = c3
                                                                                                krolowka[licz,2,3] = c4
                                                                                                znajdki[licz,0] = czy_wystpuje_slowo(krolowka[licz], merkury)
                                                                                                znajdki[licz,1] = czy_wystpuje_slowo(krolowka[licz], wenus)                                                                                        
                                                                                                znajdki[licz,2] = czy_wystpuje_slowo(krolowka[licz], mars)
                                                                                                znajdki[licz,3] = czy_wystpuje_slowo(krolowka[licz], ziemia)

                                                                                                if znajdki[licz,0] and znajdki[licz,1] and znajdki[licz,2] and znajdki[licz,3]:
                                                                                                    znaleziono +=1
                                                                                                    
                                                                                                    for p1 in range (1, 5):        
                                                                                                        for p2 in range (1, 5):
                                                                                                            if p2 != p1:
                                                                                                                for p3 in range (1, 5):
                                                                                                                    if (p3 != p2) and (p3 != p1):
                                                                                                                        for p4 in range (1, 5):
                                                                                                                            if (p4 != p3) and (p4 != p2) and (p4 != p1):                                                                  
                                                                                                                                licz_planety += 1
                                                                                                                                #print (nazwy[p1-1],nazwy[p2-1],nazwy[p3-1],nazwy[p4-1])
                                                                                                                                #print (planety[a1-1],planety[a2-1],planety[a3-1],planety[a4-1])
                                                                                                                                
                                                                                                                                #print (np.concatenate((planety[p1-1],planety[p2-1],planety[p3-1],planety[p4-1]),axis=None))
                                                                                                                                planety_concat = np.concatenate((planety[p1-1],planety[p2-1],planety[p3-1],planety[p4-1]),axis=None)
                                                                                                                                if czy_wystpuje_slowo(krolowka[licz], planety_concat):
                                                                                                                                    licz_rozw +=1
                                                                                                                                    print("Rozwiązanie nr ", licz_rozw, krolowka[licz], "\n", planety_concat, "\n", nazwy[p1-1],nazwy[p2-1],nazwy[p3-1],nazwy[p4-1])
    
    end = time.time()
    print("czas [s]:", end - start)                            

if __name__ == "__main__":
    main()    
