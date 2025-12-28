# Łamiblog 2024-12-28 "Kwadratowo"https://blog.polityka.pl/penszko/2024/12/28/kwadratowo-4/
# Jest jedno rozwiązanie:
# 4 3 8
# 7 6 2
# 9 5 1

import time
import math

def main():

    j = 0
    start_time = time.time()
    for a in range (1,10):
        for b in range (1,10):
            if a!=b:
                for c in range (1,10):
                    if a!=c and b!=c and a*b+c == 20:
                        for d in range (1,10):
                            if a!=d and b!=d and c!=d:
                                for g in range (1,10):
                                    if a!=g and b!=g and c!=g and d!=g and a+d+g==20:
                                        for e in range (1,10):
                                            if a!=e and b!=e and c!=e and d!=e and g!=e:
                                                for f in range (1,10): 
                                                    if a!=f and b!=f and c!=f and d!=f and g!=f and e!=f and (d-e)*f==2:
                                                        for h in range (1,10):
                                                            if a!=h and b!=h and c!=h and d!=h and g!=h and e!=h and f!=h and b-e+h==2:
                                                                for i in range (1,10):
                                                                    if a!=i and b!=i and c!=i and d!=i and g!=i and e!=i and f!=i and h!=i and c/f+i==5 and (g-h)/i:
                                                                        j = j +1
                                                                        print(a,b,c)
                                                                        print(d,e,f)
                                                                        print(g,h,i)

    print("Liczba rozwiązań:",j)
    print("--- %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":

    main()
