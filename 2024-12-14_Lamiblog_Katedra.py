# Łamiblog 2024-12-14 "Oto ta kadra" https://penszko.blog.polityka.pl/2024/12/14/oto-ta-katedra/
# Są 4 rozwiązania, różnią się nieznacznie
# Z oznaczonych liter można ułożyć słowo DOKTOR

import time
def is_valid(board, row, col, num):
    """
    Sprawdza, czy liczba num może być umieszczona w komórce board[row][col].
    Uwzględnia:
    - unikalność w wierszu, kolumnie, bloku 3x3,
    - unikalność na przekątnych, jeśli komórka leży na przekątnej.
    """
    # Sprawdzenie wiersza i kolumny
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Sprawdzenie bloku 3x3
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row_start + i][box_col_start + j] == num:
                return False

    # Sprawdzenie przekątnych (jeśli komórka należy do przekątnej)
    if row == col:  # Główna przekątna
        for i in range(9):
            if board[i][i] == num:
                return False

    if row + col == 8:  # Druga przekątna
        for i in range(9):
            if board[i][8 - i] == num:
                return False

    return True

def solve_sudoku(board, solutions):
    """
    Rozwiązuje Sudoku za pomocą algorytmu backtracking.
    Znajduje wszystkie możliwe rozwiązania i zapisuje je w liście solutions.
    """
    # Znajdź pierwszą pustą komórkę (oznaczoną jako 0)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Wypróbuj liczby od 1 do 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        # Rekurencyjnie spróbuj rozwiązać resztę planszy
                        solve_sudoku(board, solutions)

                        # Cofamy zmianę
                        board[row][col] = 0

                return

    # Jeśli cała plansza jest wypełniona, dodaj rozwiązanie do listy
    solutions.append([row[:] for row in board])

def print_board(board):
    """
    Wypisuje planszę Sudoku w czytelnym formacie.
    """
    mapping = {0: '-',1: 'A', 2: 'D', 3: 'E', 4: 'K', 5: 'M', 6: 'N', 7: 'O', 8: 'R', 9: 'T'}
    for row in board:
        print(" ".join(mapping[num] if num != 0 else '.' for num in row))
    print("\nLitery w żółtych polach: ",mapping[board[0][4]],mapping[board[1][2]],mapping[board[5][1]],mapping[board[5][7]], mapping[board[8][1]],mapping[board[8][5]])

# Przykładowa plansza Sudoku (0 oznacza puste komórki)
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 1, 9, 3],
    [6, 0, 0, 7, 0, 0, 0, 0, 2],
    [7, 0, 0, 0, 9, 0, 0, 0, 8],
    [9, 0, 0, 0, 0, 7, 0, 0, 1],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 1, 5, 3, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0]
]

def main():

    start_time = time.time()
    print("Pierwotna plansza:")
    print_board(board)

    solutions = []
    solve_sudoku(board, solutions)

    if solutions:
        print(f"\nZnaleziono {len(solutions)} rozwiązanie/a:")
        for idx, solution in enumerate(solutions, 1):
            print(f"\nRozwiązanie {idx}:")
            print_board(solution)
    else:
        print("\nNie znaleziono rozwiązania.")

    print("--- %s seconds ---" % (time.time() - start_time))
    


if __name__ == "__main__":
    main()
