import pygame
import sys
# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Círculo Móvil")

# Colores
white = (255, 255, 255)
blue = (0, 0, 255)

# Posición y tamaño inicial del círculo
circle_x, circle_y = screen_width // 2, screen_height // 2
circle_radius = 30

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
        # Mover el círculo al lugar donde se encuentra el ratón
        circle_x, circle_y = mouse_x, mouse_y

    # Comprobar si la rueda del ratón se está utilizando
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 4:
            # Aumentar el radio del círculo al hacer girar la rueda hacia arriba
            circle_radius += 5
        elif event.button == 5:
            # Disminuir el radio del círculo al hacer girar la rueda hacia abajo
            circle_radius = max(5, circle_radius - 5)

    # Llenar la pantalla con color blanco
    screen.fill(white)

    # Dibujar el círculo
    pygame.draw.circle(screen, blue, (circle_x, circle_y), circle_radius)

    # Actualizar la pantalla
    pygame.display.update()

# Finalizar Pygame
pygame.quit()
sys.exit()