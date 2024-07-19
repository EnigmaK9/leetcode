import os
os.environ["SDL_VIDEODRIVER"] = "dummy"  # Puedes intentar con "x11", "directfb", "dga", etc.
import pygame
import sys
from pygame.locals import QUIT

# Inicializa pygame
pygame.init()

# Constantes de pantalla
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Detección de Ciclos en Lista Enlazada')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Nodo de la lista enlazada
class ListNode:
    def __init__(self, value=0):
        self.value = value
        self.next = None

# Función para crear una lista enlazada con ciclo para la demostración
def create_cyclic_list(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    cycle_entry = None
    if pos == 0:
        cycle_entry = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_entry = current
    current.next = cycle_entry
    return head

# Dibujar nodo
def draw_node(screen, x, y, value, color=BLACK):
    pygame.draw.circle(screen, color, (x, y), 20)
    font = pygame.font.Font(None, 36)
    text = font.render(str(value), True, WHITE)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

# Dibujar flecha
def draw_arrow(screen, start, end):
    pygame.draw.line(screen, BLACK, start, end, 3)
    pygame.draw.polygon(screen, BLACK, [end, (end[0] - 5, end[1] - 5), (end[0] - 5, end[1] + 5)])

# Variables de la lista enlazada
values = [3, 2, 0, -4]
pos = 1
head = create_cyclic_list(values, pos)

# Variables de visualización
nodes_positions = [(100 + i * 150, HEIGHT // 2) for i in range(len(values))]
nodes = []
current = head
i = 0
while current:
    nodes.append((nodes_positions[i], current))
    current = current.next
    i += 1
    if i >= len(values):
        break

# Punteros lento y rápido
slow = head
fast = head

# Ciclo de visualización
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    SCREEN.fill(WHITE)

    # Dibujar lista enlazada
    for j, (node_pos, node) in enumerate(nodes):
        draw_node(SCREEN, node_pos[0], node_pos[1], node.value)
        if j < len(nodes) - 1:
            draw_arrow(SCREEN, (node_pos[0] + 20, node_pos[1]), (nodes_positions[j + 1][0] - 20, nodes_positions[j + 1][1]))

    # Dibujar ciclo si existe
    if pos >= 0:
        draw_arrow(SCREEN, (nodes_positions[-1][0] + 20, nodes_positions[-1][1]), (nodes_positions[pos][0] - 20, nodes_positions[pos][1]))

    # Mover punteros
    if fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Dibujar punteros
    slow_pos = nodes_positions[values.index(slow.value)]
    fast_pos = nodes_positions[values.index(fast.value)]
    draw_node(SCREEN, slow_pos[0], slow_pos[1], slow.value, RED)
    draw_node(SCREEN, fast_pos[0], fast_pos[1], fast.value, GREEN)

    # Detectar ciclo
    if slow == fast:
        font = pygame.font.Font(None, 74)
        text = font.render('¡Ciclo detectado!', True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        SCREEN.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)
        running = False

    pygame.display.update()
    clock.tick(1)  # Controlar la velocidad de la simulación

pygame.quit()
sys.exit()

