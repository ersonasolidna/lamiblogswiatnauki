# Łamiblog "Krzyżowanie bliźniaków" https://penszko.blog.polityka.pl/2022/07/16/krzyzowanie-blizniakow/import time
# skrypt zawiera dwa rozwiązania:
# moje - wolniejsze (main_rozwiazanie_wolniejsze)
# rowiązanie zaproponowane przez Tomasza Bosaka, przepisane na python - ok. 4x szybsze (main_rozwiazanie_szybsze_tb)

import time
import math

bliz = [101, 103, 107, 109, 137,139,149,151,179,181,191,193,197,199,227,229,239,241,269,271,281,283,311,313,347,349,419,421,431,433,461,463,521,523,569,571,
        599,601,617,619,641,643,659,661,809,811,821,823,827,829,857,859,881,883]


def main_rozwiazanie_wolniejsze():

    # rozwiązanie moje
    start = time.time()
    #print("start:", start)

    drukujemywyniki = True
    
    if drukujemywyniki:
        print ("Liczba bliżniaków: ", len(bliz))
    x = 0
    for a in range (1,10):
        for b in range (1,10):
            for c in range (1,10):
                w1 = a*100+b*10+c
                if (w1 in bliz):
                    for d in range (1,10):
                        for e in range (0,10):
                            for f in range (1,10):
                                w2 = d*100+e*10+f
                                if (w2 in bliz) and (w2 !=w1):
                                    for g in range (1,10):
                                        for h in range (0,10):
                                            for i in range (1,10):
                                                w3 = g*100+h*10+i
                                                k1 = a*100+d*10+g
                                                k2 = b*100+e*10+h
                                                k3 = c*100+f*10+i
                                                if (w3 in bliz) and (w3 != w2) and (w3 != w1) and (k1 in bliz) and (k2 in bliz) and (k3 in bliz) and (k1 != k2) and (k1 != k3) and (k2 != k3) and (w1 != k1) and (w1 != k2) and (w1 != k3) and (w2 != k1) and (w2 != k2) and (w2 != k3) and (w3 != k1) and (w3 != k2) and (w3 != k3):
                                                        x = x + 1
                                                        if drukujemywyniki:
                                                            #print(w1,w2,w3)
                                                            print ("---")
                                                            print(w1)
                                                            print(w2)
                                                            print(w3)
                                                        
    end = time.time()
    print("czas [s]:", end - start)
    print("Liczba rozwiązań = ", x)

def main_rozwiazanie_szybsze_tb():

    # rozwiązanie Tomasza Bosaka przepisane na python
    # rozwiązanie źródłowe: https://github.com/tomasz-bosak/lamiblogSolutions/blob/main/krzyzowanieBlizniakow/solution.go
    start = time.time()
    #print("start:", start)

    drukujemywyniki = True
    
    if drukujemywyniki:
        print ("Liczba bliżniaków: ", len(bliz))
    x = 0
    for a in range (0,54):
        for b in range (0,54):
            if a != b:
                for c in range (0,54):
                    if (c!=a) and (c!=b):
                        a1 = bliz[a]
                        a2 = bliz[b]
                        a3 = bliz[c]
                        b1 = math.floor(a1/100)*100 + 10*math.floor(a2/100) + math.floor(a3/100)
                        b2 = 100*int(str(a1)[1:2])+10*int(str(a2)[1:2])+int(str(a3)[1:2])
                        b3 = 100*int(str(a1)[2:3])+10*int(str(a2)[2:3])+int(str(a3)[2:3])
                        if (b1 in bliz) and (b2 in bliz) and (b3 in bliz):
                            if (b1 !=a1) and (b1 != a2) and (b1 !=a3) and (b2 !=a1) and (b2 != a2) and (b2 !=a3) and (b3 !=a1) and (b3!=a2) and (b3!=a3) and (b3!=b2) and (b2!=b1) and (b3!=b1):
                                x = x + 1
                                if drukujemywyniki:
                                    print("---")
                                    #print(a1,a2,a3)
                                    print(a1)
                                    print(a2)
                                    print(a3)
                                                        
                                                        
    end = time.time()
    print("czas [s]:", end - start)
    print("Liczba rozwiązań = ", x)
    
main_rozwiazanie_szybsze_tb()

 
