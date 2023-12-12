import pygame
import random

# Initialisation de Pygame
pygame.init()

# Constantes du jeu
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Création de la fenêtre du jeu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Définition des pièces Tetris
tetrominos = [
    [[1, 1, 1, 1]],            # I
    [[1, 1, 1, 1]],            # O
    [[1, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]],  # T
    [[1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0]],  # L
    [[1, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]],  # J
    [[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]],  # S
    [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]   # Z
]


# Classe pour représenter une pièce
class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = random.choice(tetrominos)
        self.color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        self.rotation = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

    def get_blocks(self):
        return self.shape[self.rotation]

# Fonction pour dessiner une pièce
def draw_piece(piece):
    blocks = piece.get_blocks()
    color = piece.color
    for row in range(len(blocks)):
        for col in range(len(blocks[row])):
            if blocks[row][col]:
                pygame.draw.rect(screen, color, (piece.x + col * BLOCK_SIZE, piece.y + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, BLACK, (piece.x + col * BLOCK_SIZE, piece.y + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 2)

# Fonction principale
def main():
    clock = pygame.time.Clock()
    piece = Piece(3 * BLOCK_SIZE, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    piece.x -= BLOCK_SIZE
                elif event.key == pygame.K_RIGHT:
                    piece.x += BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    piece.y += BLOCK_SIZE
                elif event.key == pygame.K_SPACE:
                    piece.rotate()

        screen.fill(WHITE)
        draw_piece(piece)
        pygame.display.update()
        clock.tick(5)

if __name__ == "__main__":
    main()
