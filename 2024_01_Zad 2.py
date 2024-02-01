# UG 2024-01, zad. 2
# Do 7-miejscowego parkingu zmierza pięć aut. Ile różnych dobrych kolejek mogą one utworzyć przed wjazdem na parking przy zachowaniu opisanych w artykule standardowych warunków wyboru stanowisk i sposobu parkowania?

debug_mode = False
import time
import math

def czy_dobra_kolejka(kolejka):
    dl = len(kolejka)
    # reguła brzmi nastepujaco:
    # jako s_k oznaczmy liczbe wszystkich aut z numerami nie wiekszymi niz k (k<n; n - liczba stanowisk)
    # przynajmniej jeden samochod zostanie odeslany z kwitkiem, jesli s_k > k
    for k in range(1,dl+1):
        mniejnizk = 0
        for j in range (1, k+1):
            #print("liczba wystąpień znaku = ",j, "=", kolejka.count(str(j)))
            mniejnizk = mniejnizk + kolejka.count(str(j))
        #print("liczba wystąpień znaków <= ",k, "=", mniejnizk)
        if mniejnizk > k:
            return False
    return True

def main():
    k = 5
    n = 7
    licz = 0
    odrzut = 0
    start_time = time.time()

    # nie używam itertools aby nie komplikować tego programu
    for i in range(1,n+1):
        for j in range (1,n+1):
            for k in range (1,n+1):
                for l in range (1,n+1):
                    for m in range (1,n+1): 
                        
                        kolejka = str(i) + "" + str(j) + "" + str(k) + "" + str(l) + "" + str(m)
                        if czy_dobra_kolejka(kolejka):
                            licz = licz+ 1
                        else:
                            odrzut = odrzut + 1
                        #print (kolejka)
    
    print ("Liczba dobrych kolejek dla", k, "aut na parkingu",n,"-miejscowym to",licz)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main() 
