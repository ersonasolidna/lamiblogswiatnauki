# UG 2021-06, zad. 2

import time, math
    
def is_prime(n):
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

def is_square(n):
    if (n**0.5) == int(n**0.5):
        return True
    else:
        return False


def is_exp_but_not_square(n):
    if is_square(n):
        return False
    else:
        if (n**1/3) == int(n**1/3):
            return True
        if (n**1/4) == int(n**1/4):
            return True
        if (n**1/5) == int(n**1/5):
            return True

        
def main():

    start = time.time()
    liczba_5_cyfrowych_kw = 0
    liczba_4_cyfrowych_pr = 0

    for i in range(10000,100000):
        if is_square(i):
            #liczba_5_cyfrowych_kw +=1
            j = str(i)
            j = j[:4]            
            if is_prime(int(j)):
                #liczba_4_cyfrowych_pr += 1                            
                k = j
                k = k[1:]
                if is_exp_but_not_square(int(k)):
                    l = k
                    l = l[1:]
                    if is_prime(int(l)) and int(l)>9:
                        m = l
                        m = m[:1]
                        if is_square(int(m)):                            
                            print("Rozwiązanie:", i,j,k,l,m)                                
    
    end = time.time()
    print("czas [s]:", end - start)                            

if __name__ == "__main__":
    main()    
