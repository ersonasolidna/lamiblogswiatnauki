# UG 2025-01, zad. 2
#
# Należy utworzyć kwadrat półmagiczny z dziewięciu liczb wybranych z 15 mniejszych od 50 liczb złożonych bezkwadratowych
# (6, 10, 14, 15, 21, 22, 26, 30, 33, 34, 35, 38, 39, 42, 46)
# Rozwiązanie to kwadrat:
# [6 26 42]
# [30 34 10]
# [38 14 22]

import time
import itertools

LICZBY = [6, 10, 14, 15, 21, 22, 26, 30, 33, 34, 35, 38, 39, 42, 46]

def wyswietl_kwadrat(arr):
    """ Pomocnicza funkcja do ładnego wyświetlenia macierzy 3×3. """
    print("Kwadrat półmagiczny (3×3):")
    for i in range(0, 9, 3):
        print(arr[i], arr[i+1], arr[i+2])
    print()

def znajdz_kwadrat_polmagiczny(zbior9):
    """
    Próbuje ułożyć 9 liczb w kwadrat 3×3 metodą backtracking.
    Zwraca listę 9 liczb w układzie półmagicznym lub None, jeśli brak rozwiązania.
    """
    # Suma 9 liczb (sprawdzamy to już wcześniej, ale tu też pobieramy do zmiennej)
    total_sum = sum(zbior9)
    # Docelowa suma w każdym wierszu/kolumnie
    row_sum = total_sum // 3

    # Zamieniamy na listę, by łatwo manipulować i wybierać poszczególne liczby
    dostepne = list(zbior9)

    # Tutaj będziemy budować finalny układ 3×3 w postaci 9-elementowej listy
    uklad = [None]*9

    # Pomocnicze tablice na sumy wierszy i kolumn – na bieżąco uzupełniane
    # r[i] = bieżąca suma i-tego wiersza
    # c[j] = bieżąca suma j-tej kolumny
    r = [0, 0, 0]
    c = [0, 0, 0]

    def backtrack(pos):
        """
        pos = indeks w ukladzie (0..8),
        czyli pos//3 = nr wiersza, pos%3 = nr kolumny
        """
        if pos == 9:
            # Udało się wypełnić wszystkie pola bez konfliktów
            return True

        # Wiersz i kolumna odpowiadające bieżącej pozycji
        w = pos // 3
        k = pos % 3

        # Próbujemy wstawić każdą z dostępnych jeszcze liczb
        for i, num in enumerate(dostepne):
            if num is None:
                continue

            # Dodajemy num do aktualnego wiersza i kolumny
            uklad[pos] = num
            r[w] += num
            c[k] += num

            # Oznaczamy liczbę jako "zużytą"
            dostepne[i] = None

            # Sprawdzamy, czy nie przekroczyliśmy row_sum w wierszu lub kolumnie
            if r[w] <= row_sum and c[k] <= row_sum:
                # Jeżeli jest to koniec wiersza, sprawdź, czy jego suma jest dokładnie row_sum
                if (k == 2) and (r[w] != row_sum):
                    # Błędna suma wiersza – cofamy zmiany i próbujemy dalej
                    pass
                else:
                    # Jeżeli to koniec kolumny, sprawdź czy suma kolumny = row_sum
                    # Koniec kolumny następuje dopiero gdy w == 2 (ostatni wiersz),
                    # ale możemy sprawdzać etapami (opcja). Na razie uprośćmy:
                    # Sprawdzamy kolumnę dopiero przy w == 2 (czyli przy ostatnim wierszu)
                    if (w == 2) and (c[k] != row_sum):
                        # Błędna suma kolumny – cofamy zmiany
                        pass
                    else:
                        # Jeżeli dotąd OK, idź dalej
                        if backtrack(pos + 1):
                            return True

            # Cofanie zmian (backtracking)
            r[w] -= num
            c[k] -= num
            dostepne[i] = num
            uklad[pos] = None

        return False

    # Uruchamiamy backtracking
    if backtrack(0):
        return uklad
    else:
        return None


def main():
    start_time = time.time()
    # Szukamy 9-elementowych kombinacji
    for kombinacja in itertools.combinations(LICZBY, 9):
        # Szybka weryfikacja, czy suma 9 liczb jest podzielna przez 3
        if sum(kombinacja) % 3 != 0:
            continue  # jeśli nie, pomijamy

        # Próbujemy ułożyć kwadrat półmagiczny z danej kombinacji
        wynik = znajdz_kwadrat_polmagiczny(kombinacja)
        if wynik is not None:
            print(f"Znaleziono rozwiązanie dla kombinacji: {kombinacja}")
            wyswietl_kwadrat(wynik)
            return

    print("Nie znaleziono żadnego kwadratu półmagicznego dla podanych liczb.")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()