

import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Triángulo Móvil")

# Colores
white = (255, 255, 255)
blue = (0, 0, 255)

# Posición y tamaño inicial del triángulo
triangle_x, triangle_y = screen_width // 2, screen_height // 2
triangle_size = 60

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
        # Mover el triángulo al lugar donde se encuentra el ratón
        triangle_x, triangle_y = mouse_x, mouse_y

    # Comprobar si la rueda del ratón se está utilizando
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 4:
            # Aumentar el tamaño del triángulo al hacer girar la rueda hacia arriba
            triangle_size += 5
        elif event.button == 5:
            # Disminuir el tamaño del triángulo al hacer girar la rueda hacia abajo
            triangle_size = max(5, triangle_size - 5)

    # Llenar la pantalla con color blanco
    screen.fill(white)

    # Dibujar el triángulo
    triangle_points = [(triangle_x, triangle_y - triangle_size),
                      (triangle_x - triangle_size, triangle_y + triangle_size),
                      (triangle_x + triangle_size, triangle_y + triangle_size)]
    pygame.draw.polygon(screen, blue, triangle_points)

    # Actualizar la pantalla
    pygame.display.update()

# Finalizar Pygame
pygame.quit()
sys.exit()