import pygame
import sys

# Initialize Pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball position
x, y = 300, 200
speed_x, speed_y = 3, 3
radius = 20

# Game loop
while True:
    # Check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move ball
    x += speed_x
    y += speed_y

    # Bounce from walls
    if x - radius < 0 or x + radius > 600:
        speed_x = -speed_x
    if y - radius < 0 or y + radius > 400:
        speed_y = -speed_y

    # Fill background
    screen.fill(WHITE)

    # Draw ball
    pygame.draw.circle(screen, RED, (x, y), radius)

    # Update display
    pygame.display.flip()

    # Control FPS
    pygame.time.Clock().tick(60)
