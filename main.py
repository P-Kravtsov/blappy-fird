import pygame
import sys
import random
from settings import *
from sprites import Bird, Pipe


# --- Game Functions ---
def check_collision(pipes):
    """Checks for collisions with pipes and screen boundaries."""
    # Collision with pipes
    if pygame.sprite.spritecollide(bird.sprite, pipes, False):
        death_sound.play()
        return False
    # Collision with top or bottom of the screen
    if bird.sprite.rect.top <= -50 or bird.sprite.rect.bottom >= 768:
        death_sound.play()
        return False
    return True


def reset_game():
    """Resets the game to its initial state."""
    pipe_group.empty()
    bird.sprite.rect.center = (100, SCREEN_HEIGHT / 2)
    bird.sprite.velocity = 0
    return True, 0  # Return game_active status and reset score


def score_display():
    """Displays the current score on the screen."""
    score_surface = game_font.render(str(score), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(SCREEN_WIDTH / 2, 100))
    screen.blit(score_surface, score_rect)


# --- Initialization ---
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Blappy Fird')
clock = pygame.time.Clock()
game_font = pygame.font.Font(FONT_PATH, 70)

# --- Game State Variables ---
game_active = True
score = 0

# --- Asset Loading ---
bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
bg_surface.fill((40, 40, 60))
death_sound = pygame.mixer.Sound(ASSETS['sounds']['hit'])
score_sound = pygame.mixer.Sound(ASSETS['sounds']['score'])  # Load sound

# --- Sprites ---
bird = pygame.sprite.GroupSingle(Bird(100, SCREEN_HEIGHT / 2))
pipe_group = pygame.sprite.Group()

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
            if event.key == pygame.K_SPACE:
                if game_active:
                    bird.sprite.jump()
                else:
                    game_active, score = reset_game()

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
        # Check for collisions and update game state
        game_active = check_collision(pipe_group)

        # Scoring logic
        if pipe_group:
            # Check the first pipe in the group
            first_pipe = pipe_group.sprites()[0]
            if not first_pipe.passed and first_pipe.rect.centerx < bird.sprite.rect.centerx:
                score += 1
                score_sound.play()
                # Mark both top and bottom pipes as passed
                for p in pipe_group.sprites():
                    if p.rect.centerx == first_pipe.rect.centerx:
                        p.passed = True

        score_display()

    else:
        # If game is not active, just draw the bird and pipes in their last position
        bird.draw(screen)
        pipe_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
