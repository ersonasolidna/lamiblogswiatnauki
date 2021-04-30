# UG 2021-05, zad. 1

import time

def obliczLiczbeNL(i,j,k,l,m=2,p=2):
    wynik = 1
    liczby = [i,j,k,l,m,p,2]
    dowyrzucenia = []

    for liczba in liczby:
        if liczba > 10:
            liczby.append(1)
            liczby.append(liczba % 10)
            dowyrzucenia.append(liczba)
            #print ("cyfra druga",liczba % 10)        

    liczby = [x for x in liczby if x not in dowyrzucenia]            
    return len(set(liczby))  
    
def main():

    start = time.time()

    wynikinL= []    
    z = 0

    n = 4
    for i in range (1,16):
        for j in range (1,16):
            for k in range (1,16):
                for l in range (1,16):
                    if i**2+j**2+k**2+l**2 == 287:
                          wynikinL.append(n * obliczLiczbeNL(i,j,k,l))
                          z = z +1
                          if wynikinL[-1] == min(wynikinL):
                            print ("dotychczas_min =", wynikinL[-1], ", n =",n,", podstawy kwadratów =", i,j,k,l) 


    n = 5 
    for i in range (1,16):
        for j in range (1,16):
            for k in range (1,16):
                for l in range (1,16):
                    for m in range (1,16):
                        if i**2+j**2+k**2+l**2+m**2 == 287:
                            wynikinL.append(n * obliczLiczbeNL(i,j,k,l,m))
                            z = z +1
                            if wynikinL[-1] == min(wynikinL):
                              print ("dotychczas_min =", wynikinL[-1], ", n =",n,", podstawy kwadratów =", i,j,k,l,m) 

##    n = 6 # sprawdzenie dla n = 6 nie ma już sensu - nie zejdziemy poniżej wyniku 12
##    for i in range (1,16):
##        for j in range (1,16):
##            for k in range (1,16):
##                for l in range (1,16):
##                    for m in range (1,16):
##                        for p in range (1,16):
##                            if i**2+j**2+k**2+l**2+m**2+p**2 == 287:
##                                wynikinL.append(n * obliczLiczbeNL(i,j,k,l,m,p))
##                                z = z +1
##                                if wynikinL[-1] == min(wynikinL):
##                                  print ("dotychczas_min =", wynikinL[-1], " ,n =",n,", kwadraty =", i,j,k,l,m,p)



    print ("min = ", min(wynikinL), "max = ",max(wynikinL))

    end = time.time()
    print(end - start)                            

if __name__ == "__main__":
    main()    

