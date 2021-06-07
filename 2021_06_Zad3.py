# UG 2021-06, zad. 3

import time, math
import numpy as np
            
def main():

    start = time.time()

    # Parametry
    LIMIT = 10_000_000
    MAX_KROKI = 26

    # Zbiór właściwy i zbiór wsteczny powinny mieć tyle samo wierszy, ale mogą się różnić liczbą kolumn    
    zbior = np.zeros((MAX_KROKI+1,1000000), dtype=int)
    zbior_wstecz = np.zeros((MAX_KROKI+1,10000), dtype=int)

    # Zbiór właściwy od 4 do 2021
    # Potrzebny, aby określić, w ilu minimalnie krokach można dojść do 2021
    
    zbior[0,0] = 4 # wartość startowa

    for j in range(0,MAX_KROKI):

        templist = zbior[j]
        myset = set(zbior[j])
        mylist = list(myset)
        mylist.sort()
        mylist = mylist[1:] # ucinamy pierwsze zero

        k = 0

        j +=1
        for a in mylist:
          if a*10 > 0 and a*10 <= LIMIT:
              zbior[j,k] = a*10
              k += 1
          if a*10+4 > 0 and a*10+4 <= LIMIT:  
              zbior[j,k] = a*10+4
              k += 1
          if (a % 2) == 0:
            zbior[j,k] =  a / 2
            k +=1
    
    # Zbiór wstecz od 2021 do 4
    # Potrzebny, aby określić, jakie są konkretnie ścieżki dojścia od 4 do 2021
    
    zbior_wstecz[0,0] = 2021 # wartość startowa

    for j in range(0,MAX_KROKI):

        templist = zbior_wstecz[j]
        myset = set(zbior_wstecz[j])
        mylist = list(myset)
        mylist.sort()
        mylist = mylist[1:] # ucinamy pierwsze zero

        k = 0

        j +=1
        for a in mylist:
          if (a % 10) == 0:
              zbior_wstecz[j,k] = a/10
              k += 1
          if ((a-4) % 10) == 0 and (a-4)>0:  
              zbior_wstecz[j,k] = (a-4)/10
              k += 1
          if  (a * 2) <= LIMIT:
              zbior_wstecz[j,k] =  a * 2
          k +=1


##    print ("\nZBIÓR\n")
##    print("Zbiór 4 -> 2021",zbior)
##
##    count_nonzero = np.count_nonzero(zbior)
##    count_nonzero_perwiersz = np.count_nonzero(zbior, axis=1)
##    print (f"Wartości niezerowych jest {count_nonzero}, {count_nonzero_perwiersz}")
##
##
##    print ("\n\nZBIÓR WSTECZ\n")
##
##    print("Zbiór 2021  -> 4",zbior_wstecz)

    # To jest rozwiązanie:
    x = np.where(zbior_wstecz == 4)
    print ("ROZWIĄZANIE: Znalezione 4 w kroku nr:", x[0][0])

##    count_nonzero = np.count_nonzero(zbior_wstecz)
##    count_nonzero_perwiersz = np.count_nonzero(zbior_wstecz, axis=1)
##    print (f"Wartości niezerowych jest {count_nonzero}, {count_nonzero_perwiersz}")

    # Odtworzenie wszystkich ścieżek prowadzących z 4 do 2021
    print ("SUPLEMENT - ŚCIEŻKI (możliwe wartości w poszczególnych krokach):")
    for j in range(0,MAX_KROKI+1):
        print(j,".", np.intersect1d(zbior[j],zbior_wstecz[MAX_KROKI-j])[1:])
    
    end = time.time()
    print("czas [s]:", end - start)                            

if __name__ == "__main__":
    main()    
