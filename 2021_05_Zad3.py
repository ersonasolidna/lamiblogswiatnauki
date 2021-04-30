# UG 2021-05, zad. 3

import time
    
def isPrime(n):
# bardzo szybki sprawdzacz pierwszości znaleziony tu:
# https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
##    print('\t',f)
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True    

def main():

    start = time.time()

##    num = int(input("Enter a number: "))
    pierwsze  = []
    maxLim = 10000
    for i in range(1, maxLim):
        wynik = isPrime(i)        
        if (wynik):
            pierwsze.append (i)    
        
##    print (pierwsze)
    kandydaci = [] 
    spalone = []
    kandydacidousuniecia = []
    
    for s in range(1,maxLim):
        for pierwsza in pierwsze:        
            if (s % (pierwsza-1)) == 0:
                if (s % pierwsza) == 0:
                    kandydaci.append (s)
                else:
                    spalone.append (s)

## wyciągnięcie unikalnych wartości:
    myset = set(kandydaci)
    kandydaci = list(myset)

## wyciągnięcie unikalnych wartości:
    myset = set(spalone)
    spalone = list(myset)

    ## usunięcie spalonych wartości z listy kandydaci
    ## myk wziąłem stąd https://stackoverflow.com/questions/4211209/remove-all-the-elements-that-occur-in-one-list-from-another
    kandydaci = [x for x in kandydaci if x not in spalone]
    
#### wyznaczenie kandydatów do usunięcia
##    for kandydat in kandydaci:       
##        for spalony in spalone:
##            if kandydat == spalony:
##                kandydacidousuniecia.append(kandydat)
##
#### usunięcie kandydatów spalonych z listy
##    for kandydat in kandydacidousuniecia:
##            kandydaci.remove(kandydat)

## wydruk rozwiązania
    for kandydat in kandydaci:
            print ("s = ", kandydat)
            for pierwsza in pierwsze:        
                if (kandydat % (pierwsza-1)) == 0:
                    if (kandydat % pierwsza) == 0:
                        print ("pierwsza:", pierwsza,";", kandydat, "/", pierwsza,"=",kandydat/pierwsza, ";", kandydat, "/", pierwsza-1,"=",kandydat/(pierwsza-1))
    end = time.time()
    print(end - start)                            

if __name__ == "__main__":
    main()    

