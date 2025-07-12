import pygame
import sys
from settings import *
from sprites import Bird

# --- Initialization ---
pygame.init()
# Initialize the mixer for sound effects
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Blappy Fird')
clock = pygame.time.Clock()

# --- Game State Variables ---
# For now, the game starts active and we can control the bird
game_active = True

# --- Asset Loading ---
bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
bg_surface.fill((40, 40, 60))

# --- Sprites ---
bird = pygame.sprite.GroupSingle(Bird(100, SCREEN_HEIGHT / 2))

# --- The Game Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Check for keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird.sprite.jump()

    # --- Drawing and Updates ---
    screen.blit(bg_surface, (0, 0))

    # Update and draw the bird if the game is active
    if game_active:
        bird.update()
        bird.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
