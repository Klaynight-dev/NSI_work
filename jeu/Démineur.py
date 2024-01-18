import pygame
import random

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BEIGE = (245, 245, 220)

# Paramètres de la grille
GRID_SIZE = 10
NUM_MINES = 15
CELL_SIZE = 50
MARGIN = 5
WIDTH = HEIGHT = GRID_SIZE * CELL_SIZE + (GRID_SIZE + 1) * MARGIN

# Initialisation de la grille
grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
flags = set()
mines = set()


def init_grid():
    global mines
    mines = set()
    count = 0

    while count < NUM_MINES:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)

        if (x, y) not in mines:
            grid[x][y] = 'X'
            count += 1
            mines.add((x, y))

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i, j) in mines:
                continue
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and (nx, ny) in mines:
                        count += 1
            grid[i][j] = str(count) if count > 0 else ' '


def reveal_empty_cells(x, y):
    if revealed[x][y]:
        return
    revealed[x][y] = True

    if grid[x][y] != ' ':
        return

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                reveal_empty_cells(nx, ny)


def draw_text(screen, text, pos):
    font = pygame.font.SysFont(None, 30)
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, pos)


def main():
    global revealed, flags
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Démineur')
    clock = pygame.time.Clock()

    init_grid()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                cell_x = x // (CELL_SIZE + MARGIN)
                cell_y = y // (CELL_SIZE + MARGIN)

                if event.button == 1:  # Clic gauche
                    if not revealed[cell_x][cell_y] and (cell_x, cell_y) not in flags:
                        if grid[cell_x][cell_y] == 'X':
                            game_over = True
                        else:
                            reveal_empty_cells(cell_x, cell_y)
                elif event.button == 3:  # Clic droit
                    if not revealed[cell_x][cell_y]:
                        if (cell_x, cell_y) in flags:
                            flags.remove((cell_x, cell_y))
                        else:
                            flags.add((cell_x, cell_y))

        screen.fill(WHITE)

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                rect = pygame.Rect((MARGIN + CELL_SIZE) * i + MARGIN, (MARGIN + CELL_SIZE) * j + MARGIN, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, GRAY, rect)

                if (i, j) in flags:
                    pygame.draw.rect(screen, BLUE, rect)
                elif revealed[i][j]:
                    if grid[i][j] == 'X':
                        pygame.draw.circle(screen, RED, (i * (CELL_SIZE + MARGIN) + CELL_SIZE // 2, j * (CELL_SIZE + MARGIN) + CELL_SIZE // 2), 10)
                        pygame.draw.rect(screen, BEIGE, rect)
                    else:
                        draw_text(screen, grid[i][j], (i * (CELL_SIZE + MARGIN) + 20, j * (CELL_SIZE + MARGIN) + 15))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()