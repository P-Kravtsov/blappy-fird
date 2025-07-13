import pygame
import sys
import random # for pipe heights
from settings import *
from sprites import Bird, Pipe

# --- Initialization ---
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Blappy Fird')
clock = pygame.time.Clock()

# --- Game State Variables ---
game_active = True

# --- Asset Loading ---
bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
bg_surface.fill((40, 40, 60))

# --- Sprites ---
bird = pygame.sprite.GroupSingle(Bird(100, SCREEN_HEIGHT / 2))
pipe_group = pygame.sprite.Group() # Create a group for pipes

# --- Timer for Spawning Pipes ---
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, PIPE_FREQUENCY)
pipe_height = [350, 450, 550, 600]

# --- The Game Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird.sprite.jump()
        # Check for the pipe spawn event
        if event.type == SPAWNPIPE and game_active:
            pipe_y = random.choice(pipe_height)
            bottom_pipe = Pipe(SCREEN_WIDTH + 50, pipe_y, -1)
            top_pipe = Pipe(SCREEN_WIDTH + 50, pipe_y, 1)
            pipe_group.add(bottom_pipe, top_pipe)

    # --- Drawing and Updates ---
    screen.blit(bg_surface, (0, 0))

    if game_active:
        bird.update(game_active)
        pipe_group.update()
        bird.draw(screen)
        pipe_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

