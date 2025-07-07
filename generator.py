import random
import json

def is_valid(board, num, pos):
    row, col = pos

    for i in range(9):
        if board[row][i] == num and i != col:
            return False

    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def fill_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if is_valid(board, num, (i, j)):
                        board[i][j] = num
                        if fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def generate_puzzle(holes=40):
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)

    while holes > 0:
        i, j = random.randint(0, 8), random.randint(0, 8)
        if board[i][j] != 0:
            board[i][j] = 0
            holes -= 1

    return board

def save_puzzle(board, filename="sudoku_puzzle.json"):
    with open(filename, "w") as f:
        json.dump(board, f)

if __name__ == "__main__":
    puzzle = generate_puzzle(holes=40)
    save_puzzle(puzzle)
    print("✅ Puzzle saved to sudoku_puzzle.json")
