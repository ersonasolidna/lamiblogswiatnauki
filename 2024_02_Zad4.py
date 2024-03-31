# UG 2024-02, zad. 4
#
# Podczas wyprzedaży luksusowych towarów przez pewną firmę zdecydowano się na oryginalny sposób
# obniżki cen: każda nowa cena była poprzednią zapisaną wspak. Wszystkie ceny pozostały jednak 4-cyfrowymi
# całkowitymi liczbami złotych, a - co osobliwe - okazało się, że każda różnica między nową, okazyjną
# a porzednią ceną była kwadratem liczby całkowitej.
# Na przykład towar, który dotąd kosztował 7216 złotych, teraz był oferowany za 6127 złotych, czyli jego cena zmalała o 1089=33^2 złotych.
# Obniżka ceny jednego z towarów była zaskakująco duża i teoretycznie w opisanej sytuacji największa możliwa.
# Jaka była ta największa różnica między dawną a nową ceną?

import math
import time
import sys

def anagram(cena):
    cena_anagram = 1000*int(str(cena)[3])+100*int(str(cena)[2])+10*int(str(cena)[1])+int(str(cena)[0])
    return cena_anagram

def main():
    start_time = time.time()
    global debug_mode
    debug_mode = False

    maxroznica = 0
    ceny = []
    
    for cena in range (1000,10000):
        if str(cena)[3] != "0":
            if anagram(cena) - cena > 0:
                pierw = math.sqrt(anagram(cena) - cena)
                if pierw == math.floor(pierw):
                    if debug_mode:
                        print(cena, anagram(cena) - cena, pierw, math.floor(pierw))
                    if anagram(cena) - cena >= maxroznica:
                        maxroznica = anagram(cena) - cena
                        if debug_mode:
                            print("Maxróżnica: ",cena, maxroznica)
                        ceny.append(cena)
                        
    print("Max różnica (największa obniżka ceny) to:",maxroznica)
    print("Ceny: ", ceny)
    print("--- %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
    main() 

