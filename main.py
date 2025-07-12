import pygame
import sys
from settings import *
from sprites import Bird

# --- Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Blappy Fird')
clock = pygame.time.Clock()

# --- Asset Loading ---
# For now, just a simple dark blue background
bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
bg_surface.fill((40, 40, 60))

# --- Sprites ---
# Create a group for the bird sprite. Using GroupSingle ensures there's only one.
bird = pygame.sprite.GroupSingle(Bird(100, SCREEN_HEIGHT / 2))

# --- The Game Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- Drawing ---
    screen.blit(bg_surface, (0, 0))
    bird.draw(screen) # Draw the bird sprite onto the screen

    pygame.display.update()
    clock.tick(FPS)

