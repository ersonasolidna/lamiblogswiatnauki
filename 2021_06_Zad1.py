# UG 2021-06, zad. 1

import time
        
def main():

    start = time.time()

    for i in range(100,100000):
        suma = (i+1)/2*i
        pierwsza_cyfra = int(str(int(suma))[:1])
        ostatnie_dwie_cyfry = int(str(int(suma))[-2:])
        srodek = int(str(int(suma))[1:-2])
        if ostatnie_dwie_cyfry/pierwsza_cyfra == 10:            
            if i == srodek:              
              print("Rozwiązanie:",srodek)
              print("Suma:",suma)              
            
    end = time.time()
    print("czas [s]:", end - start)                            

if __name__ == "__main__":
    main()    
