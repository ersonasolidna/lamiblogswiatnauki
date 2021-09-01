# skrypt jest rozwinięciem rozwiązania zaproponowanego przez Tech with Tim:
# https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
# skrypt rozwiązuje zagadkę https://penszko.blog.polityka.pl/2021/08/28/sudoku-z-biegiem-wstecznym/

board = [
    [0,0,1,6,0,0,0,0,7],
    [0,0,0,3,0,0,0,0,0],
    [0,2,0,0,0,0,0,0,5],
    [6,0,0,0,0,0,0,0,0],
    [0,0,4,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,7,0],
    [9,0,0,0,6,0,0,0,0],
    [0,0,5,0,0,3,0,0,1],
    [2,0,0,0,0,5,3,0,0]
]

def solve(bo):
    
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

   
        
    #return False
    
def valid (bo, num, pos):

    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3+3):
        for j in range(box_x * 3, box_x*3+3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    palindrom1 = [board[0][0], board[1][0], board[2][0], board[3][1], board[4][1], board[5][1]]
    if 0 not in palindrom1:
        if isPalindrome(palindrom1) == False:
            return False

    palindrom2 = [board[5][4], board[6][5], board[7][6], board[8][7]]
    if 0 not in palindrom2:
        if isPalindrome(palindrom2) == False:
            return False

    palindrom3 = [board[0][5], board[0][6], board[1][6], board[2][7],board[3][8],board[4][7],board[5][8],board[6][8]]
    if 0 not in palindrom3:
        if isPalindrome(palindrom3) == False:
            return False

    palindrom4 = [board[1][1], board[2][2], board[3][3], board[2][4],board[1][5],board[2][6],board[3][6],board[4][6],board[5][6],board[6][7]]
    if 0 not in palindrom4:
        if isPalindrome(palindrom4) == False:
            return False

    return True

def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print (bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def isPalindrome(s):
    return s == s[::-1]
 
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, col
    return None

def main():
    print_board(board)  
    solve(board)
    print(" ")
    print_board(board)

if __name__ == "__main__":
    main() 

