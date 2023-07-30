# łamiblog 2023-07-29, "Kwartet", oba warianty (dla cyfr 1-9 i 0-9)
# https://penszko.blog.polityka.pl/2023/07/29/kwartet

import numpy as np
import time
import math

debug_mode = False

def check_distinct_digits(string, numberofdigits):

    digits = set()
    
    for char in string:
        if char.isdigit():
            digits.add(char)
    
    if len(digits) == numberofdigits:
        return True
    else:
        return False

def check_0(tekst):
    if "0" in tekst:
        return True
    else:
        return False

def utworz_macierz(typ):
            
    i = 0
    j = 0
    row = 0

    if typ == "odejmowanie": 
        liczba_rek = 2709 # zawyżenie tej liczby bardzo spowolni skrypt
    elif typ == "dodawanie":
        liczba_rek = 2986
    elif typ == "mnozenie":
        liczba_rek = 510
    elif typ == "dzielenie":
        liczba_rek = 324

    macierz = np.zeros((liczba_rek,3),dtype=int)
    
    for i in range(0,100):
        for j in range(0,100):
            concat = str(i)+str(j)
            
            if typ == "odejmowanie":                                
                if i-j >= 0 and check_distinct_digits(concat,len(concat)):                
                    #print(i,j, i-j)
                    macierz[row][0] = i
                    macierz[row][1] = j
                    macierz[row][2] = i-j
                    row = row + 1
            elif typ == "dodawanie":                
                if i+j <= 100 and check_distinct_digits(concat,len(concat)):                 
                    #print(i,j, i-j)
                    macierz[row][0] = i
                    macierz[row][1] = j
                    macierz[row][2] = i+j
                    row = row + 1
            elif typ == "mnozenie":                
                if i*j <= 100 and check_distinct_digits(concat,len(concat)):              
                    #print(i,j, i-j)
                    macierz[row][0] = i
                    macierz[row][1] = j
                    macierz[row][2] = i*j
                    row = row + 1
            elif typ == "dzielenie":                
                if j != 0:
                    if i/j <= 100 and (i % j) == 0 and check_distinct_digits(concat,len(concat)):               
                        #print(i,j, i-j)
                        macierz[row][0] = i
                        macierz[row][1] = j
                        macierz[row][2] = i/j
                        row = row + 1                       
    print(f"liczba wierszy w macierzy {typ}: {row}")
    return macierz


def main():
    start_time = time.time()
    global debug_mode        

    # te 4 macierze listują wszystkie działania i ich wyniki dla i,j od 1 do 99. Więcej nie ma sensu, ponieważ maksymalna liczba cyfr w jednym działaniu wynosi 4 (wtedy w pozostałych 3 działaniach musi wystarczyć 6)
    m_odejmowanie = utworz_macierz("odejmowanie")    
    m_dodawanie = utworz_macierz("dodawanie")
    m_mnozenie = utworz_macierz("mnozenie")
    m_dzielenie = utworz_macierz("dzielenie")

    
    for i in range(0,100):
        if np.any(m_odejmowanie[:, 2] == i) and np.any(m_dodawanie[:, 2] == i) and np.any(m_mnozenie[:, 2] == i) and np.any(m_dzielenie[:, 2] == i):            
            #print (f"Dzielnik rozważany: {i}")
            lokalizacje_dzielenie = np.where(m_dzielenie[:, 2] == i)
            for lok_dziel in lokalizacje_dzielenie[0]:
                #print (f"{m_dzielenie[lok_dziel][0]}/{m_dzielenie[lok_dziel][1]}={m_dzielenie[lok_dziel][2]}")
                lokalizacje_mnozenie = np.where(m_mnozenie[:, 2] == i)
                for lok_mno in lokalizacje_mnozenie[0]:
                    concat = str(m_dzielenie[lok_dziel][0]) + str(m_dzielenie[lok_dziel][1]) + str(m_mnozenie[lok_mno][0])+ str(m_mnozenie[lok_mno][1])
                    if check_distinct_digits(concat,len(concat)):
                        lokalizacje_odejmowanie = np.where(m_odejmowanie[:, 2] == i)
                        for lok_ode in lokalizacje_odejmowanie[0]:
                            #print (f"{m_odejmowanie[lok_ode][0]}-{m_odejmowanie[lok_ode][1]}={m_odejmowanie[lok_ode][2]}")
                            concat = str(m_dzielenie[lok_dziel][0]) + str(m_dzielenie[lok_dziel][1]) + str(m_odejmowanie[lok_ode][0])+ str(m_odejmowanie[lok_ode][1]) + str(m_mnozenie[lok_mno][0])+ str(m_mnozenie[lok_mno][1])
                            if check_distinct_digits(concat,len(concat)):
                                lokalizacje_dodawanie = np.where(m_dodawanie[:, 2] == i)
                                for lok_dod in lokalizacje_dodawanie[0]:
                                    concat = str(m_dzielenie[lok_dziel][0]) + str(m_dzielenie[lok_dziel][1]) + str(m_odejmowanie[lok_ode][0])+ str(m_odejmowanie[lok_ode][1]) + str(m_mnozenie[lok_mno][0])+ str(m_mnozenie[lok_mno][1]) + str(m_dodawanie[lok_dod][0])+ str(m_dodawanie[lok_dod][1])
                                    if check_distinct_digits(concat,len(concat)):
                                        if not check_0(concat):
                                            print(f"Cyfry od 1-9: Dzielenie: {m_dzielenie[lok_dziel][0]}/{m_dzielenie[lok_dziel][1]}={m_dzielenie[lok_dziel][2]}, Mnożenie: {m_mnozenie[lok_mno][0]}*{m_mnozenie[lok_mno][1]}={m_mnozenie[lok_mno][2]}, Odejmowanie: {m_odejmowanie[lok_ode][0]}-{m_odejmowanie[lok_ode][1]}={m_odejmowanie[lok_ode][2]}, Dodawanie: {m_dodawanie[lok_dod][0]}+{m_dodawanie[lok_dod][1]}={m_dodawanie[lok_dod][2]}")
                                        elif check_0(concat) and len(concat)==10:
                                            print (f"Cyfry od 0-9: Dzielenie: {m_dzielenie[lok_dziel][0]}/{m_dzielenie[lok_dziel][1]}={m_dzielenie[lok_dziel][2]}, Mnożenie: {m_mnozenie[lok_mno][0]}*{m_mnozenie[lok_mno][1]}={m_mnozenie[lok_mno][2]}, Odejmowanie: {m_odejmowanie[lok_ode][0]}-{m_odejmowanie[lok_ode][1]}={m_odejmowanie[lok_ode][2]}, Dodawanie: {m_dodawanie[lok_dod][0]}+{m_dodawanie[lok_dod][1]}={m_dodawanie[lok_dod][2]}")
 
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
if __name__ == "__main__":
    main() 
