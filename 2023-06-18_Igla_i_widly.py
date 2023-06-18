# rozwiązanie Łamiblog 2023-06-18
# wygenerowane prawie w całości przez ChatGPT-4 i lekko poprawiony

import time
import math

def check_unique_chars(input_string):
    return len(input_string) == len(set(input_string))

def main():
    start_time = time.time()


    # 
    valid_nums = []
    for i in range(32, 100):
        num = i**2
        if num > 999 and num < 10000:
            multiplied = num * 4
            if str(multiplied).count('0') == 2:
                valid_nums.append(num)

    # Dla każdej liczby z listy sprawdzamy, czy spełnia nowe kryteria
    for num in valid_nums:
        num_str = str(num)
        for i in range(32, 316):  # dla kwadratów od 10000 do 99999
            sqr = i**2
            sqr_str = str(sqr)
            # Sprawdzamy, czy liczba spełnia nowe kryteria
            if sqr_str[1] == num_str[0] and sqr_str[3] == num_str[2] and check_unique_chars(sqr_str) and check_unique_chars(num_str):
                print(f"Liczba {num} spełnia wszystkie kryteria IGŁA, pomnożona przez 4: {num*4}. Kwadrat WIDŁY 5-cyfrowy: {sqr}, a pierwiastek z niego to {math.sqrt(sqr)}.")

    
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main() 
