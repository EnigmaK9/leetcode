import os
os.environ["SDL_VIDEODRIVER"] = "dummy"  # Cambia esto a "x11" o "directfb" si "dummy" no funciona
import pygame
import sys
from pygame.locals import QUIT

# Inicializa pygame
pygame.init()

# Constantes de pantalla
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Test')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ciclo de visualización
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    SCREEN.fill(WHITE)

    # Dibujar un círculo de prueba
    pygame.draw.circle(SCREEN, BLACK, (WIDTH // 2, HEIGHT // 2), 50)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()

