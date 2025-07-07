import pygame
import json
from solver import solve

WIDTH = 540
CELL_SIZE = WIDTH // 9

pygame.init()
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sudoku Solver")
font = pygame.font.SysFont("comicsans", 40)

def load_puzzle(filename="sudoku_puzzle.json"):
    with open(filename, "r") as f:
        board = json.load(f)
    return board

def draw_board(board, selected=None, value=None):
    screen.fill((255, 255, 255))

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                text = font.render(str(num), True, (0, 0, 0))
                screen.blit(text, (j * CELL_SIZE + 20, i * CELL_SIZE + 10))

    for i in range(10):
        thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)
        pygame.draw.line(screen, (0, 0, 0), (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), thickness)

    pygame.display.update()

def gui_loop():
    board = load_puzzle()
    draw_board(board)

    running = True
    solving = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solving = True

        if solving:
            solve(board, draw_func=draw_board)
            solving = False

        pygame.time.delay(100)

    pygame.quit()
