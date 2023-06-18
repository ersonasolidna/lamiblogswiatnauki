# Rozwiązanie Łamiblog 2023-06-18 (https://penszko.blog.polityka.pl/2023/06/18/igla-i-widly/)
# Wygenerowane w większości przez ChatGPT-4 i lekko zmodyfikowany

import time
import math

def check_unique_chars(input_string):
    return len(input_string) == len(set(input_string))

def main():
    start_time = time.time()

    # IGŁA
    valid_iglas = []
    for i in range(32, 100):
        igla = i**2
        if igla > 999 and igla < 10000:
            if check_unique_chars(str(igla)):
                multiplied = igla * 4
                if str(multiplied).count('0') == 2:
                    valid_iglas.append(igla)

    # WIDŁY
    for igla in valid_iglas:
        igla_str = str(igla)
        for i in range(32, 316):  # dla kwadratów od 10000 do 99999
            widly = i**2
            widly_str = str(widly)
            # Sprawdzamy, czy liczba spełnia nowe kryteria
            if widly_str[1] == igla_str[0] and widly_str[3] == igla_str[2] and check_unique_chars(widly_str):
                print(f"Liczba {igla} spełnia wszystkie kryteria IGŁA, pomnożona przez 4: {igla*4}. Kwadrat WIDŁY 5-cyfrowy: {widly}, a pierwiastek z niego to {math.sqrt(widly)}.")

    
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main() 
