import pygame
import sys

# --- Constants ---
SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936
FPS = 60

# --- Game Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Blappy Fird')
clock = pygame.time.Clock()

# --- Main Game Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw
    screen.fill((0, 0, 0))

    pygame.display.update()
    clock.tick(FPS)
