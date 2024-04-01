# UG 2024-03, zad. 1
# 
# Pytanie: Zakładamy następującą hipotezę: zmieniając jedną cyfrę w dowolnej liczbie naturalnej, można ją zmienić w liczbę pierwszą
# Która najmniejsza liczba jest sprzeczna z tą hipotezą?
#
# Odp:
# 200 jest najmniejszą liczbą sprzeczną z hipotezą, że zmieniając jedną cyfrę w dowolnej liczbie naturalnej, można ją zmienić w liczbę pierwszą


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

def substitute_digit(n, k, new_digit):
    # Zamień liczbę na listę cyfr
    digits = [int(d) for d in str(n)]
    
    # Sprawdź czy k jest prawidłowe (licząc od 0)
    if k < 0 or k >= len(digits):
        print("Nieprawidłowa wartość k.")
        return n
    
    # Zamień k-tą cyfrę na nową wartość
    digits[k] = new_digit
    
    # Zbuduj nową liczbę z listy cyfr
    new_number = int("".join(map(str, digits)))
    return new_number

def is_changebale_to_prime(n):
    dlug = len(str(n))
    #print("analiujemy liczbę",n)
    for i in range(0,dlug):
        for j in range(1,10):
            nowa_liczba = substitute_digit(n,dlug-i-1,j)
            #print("nowa liczba z podmienioną cyfrą na",j," to:",nowa_liczba)
            if is_prime(nowa_liczba):
                return True
    return False

def change_to_prime(n):
    dlug = len(str(n))
    for i in range(0,dlug):
        for j in range(1,10):
            nowa_liczba = substitute_digit(n,dlug-i-1,j)
            if is_prime(nowa_liczba):
                return nowa_liczba


def main():
    start_time = time.time()
    global debug_mode
    debug_mode = False

    for liczba in range (100,300):
        if is_prime(liczba):
            print("pierwsza: ",liczba)
        elif is_changebale_to_prime(liczba):
            newliczba = change_to_prime(liczba)
            print("pierwsza po zmianie 1 cyfry:", liczba,">>", newliczba)
        else:
            print("nie da się zmieinć tej liczby na pierwszą:",liczba)
            break
            
    print("--- %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
    main() 

