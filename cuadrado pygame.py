import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cuadrado Móvil")

# Colores
white = (255, 255, 255)
green = (0, 255, 0)

# Posición y tamaño inicial del cuadrado
square_size = 50
square_x, square_y = screen_width // 2 - square_size // 2, screen_height // 2 - square_size // 2

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener la posición del ratón
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Comprobar si el botón izquierdo del ratón está presionado
    if pygame.mouse.get_pressed()[0]:
        # Mover el cuadrado al lugar donde se encuentra el ratón
        square_x, square_y = mouse_x - square_size // 2, mouse_y - square_size // 2

    # Comprobar si la rueda del ratón se está utilizando
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 4:
            # Aumentar el tamaño del cuadrado al hacer girar la rueda hacia arriba
            square_size += 5
        elif event.button == 5:
            # Disminuir el tamaño del cuadrado al hacer girar la rueda hacia abajo
            square_size = max(5, square_size - 5)

    # Llenar la pantalla con color blanco
    screen.fill(white)

    # Dibujar el cuadrado
    pygame.draw.rect(screen, green, (square_x, square_y, square_size, square_size))

    # Actualizar la pantalla
    pygame.display.update()

# Finalizar Pygame
pygame.quit()
sys.exit()