# UG 2024-04, zad. 1
#
# Suma szcześcianów cyfr 3-cyfrowej liczby pierwszej P3 równa jest 4-cyfrowej liczbie pierwszej P4.
# Jaką liczbą jest P3, jeśli pierwsza cyfra obu liczb jest taka sama?
#
# Odp:
# Liczba P3 = 199 Liczba P4 = 1459



import time

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def suma_szescianow_cyfr(liczba):
    suma = 0
    while liczba > 0:
        cyfra = liczba % 10
        suma += cyfra ** 3
        liczba //= 10
    return suma

def main():
    start_time = time.time()
    global debug_mode
    debug_mode = False

    for licz in range (100,1000):
        if is_prime(licz):
            ssc = suma_szescianow_cyfr(licz)
            if ssc < 10000 and ssc > 999 and is_prime(ssc) and str(licz)[0] == str(ssc)[0]:
                print("Liczba P3 =", licz, "Liczba P4 =", ssc)
    print("--- %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
    main() 

