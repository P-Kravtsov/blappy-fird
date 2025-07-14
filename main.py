# main.py
import pygame
import sys
import random
from settings import *
from sprites import Bird, Pipe, Coin


# --- Game Functions ---
def draw_floor():
    """Draws two floor surfaces to create a scrolling effect."""
    screen.blit(floor_surface, (floor_x_pos, 768))
    screen.blit(floor_surface, (floor_x_pos + SCREEN_WIDTH, 768))


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
    coin_group.empty()
    bird.sprite.rect.center = (100, SCREEN_HEIGHT / 2)
    bird.sprite.velocity = 0
    return True, 0


def load_high_score():
    """Loads the high score from a file."""
    try:
        with open(HIGHSCORE_FILE, 'r') as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0


def update_score(current_score, high_score_val):
    """Updates the high score if the current score is higher."""
    if current_score > high_score_val:
        high_score_val = current_score
        with open(HIGHSCORE_FILE, 'w') as f: f.write(str(high_score_val))
    return high_score_val


def score_display(game_state):
    """Displays the current score or the final score and high score."""
    if game_state == 'main_game':
        score_surface = game_font.render(str(score), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH / 2, 100))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {score}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH / 2, 100))
        screen.blit(score_surface, score_rect)
        high_score_surface = game_font.render(f'High score: {high_score}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(SCREEN_WIDTH / 2, 200))
        screen.blit(high_score_surface, high_score_rect)


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
high_score = load_high_score()
floor_x_pos = 0

# --- Asset Loading & Theming ---
current_theme_name = random.choice(list(ASSETS['themes'].keys()))
current_theme = ASSETS['themes'][current_theme_name]
bg_surface = pygame.transform.scale2x(pygame.image.load(current_theme['background']).convert())
floor_surface = pygame.transform.scale2x(pygame.image.load(current_theme['ground']).convert())
pipe_image = pygame.transform.scale2x(pygame.image.load(current_theme['pipe']).convert_alpha())

death_sound = pygame.mixer.Sound(ASSETS['sounds']['hit'])
score_sound = pygame.mixer.Sound(ASSETS['sounds']['score'])
coin_sound = pygame.mixer.Sound(ASSETS['sounds']['coin'])

# --- Sprites ---
bird = pygame.sprite.GroupSingle(Bird(100, SCREEN_HEIGHT / 2))
pipe_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

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
                    # On restart, choose a new theme
                    current_theme_name = random.choice(list(ASSETS['themes'].keys()))
                    current_theme = ASSETS['themes'][current_theme_name]
                    bg_surface = pygame.transform.scale2x(pygame.image.load(current_theme['background']).convert())
                    floor_surface = pygame.transform.scale2x(pygame.image.load(current_theme['ground']).convert())
                    pipe_image = pygame.transform.scale2x(pygame.image.load(current_theme['pipe']).convert_alpha())

        if event.type == SPAWNPIPE and game_active:
            pipe_y = random.choice(pipe_height)
            # Pass the themed pipe image to the constructor
            bottom_pipe = Pipe(SCREEN_WIDTH + 50, pipe_y, -1, pipe_image)
            top_pipe = Pipe(SCREEN_WIDTH + 50, pipe_y, 1, pipe_image)
            pipe_group.add(bottom_pipe, top_pipe)
            coin_group.add(Coin(SCREEN_WIDTH + 50, pipe_y))

    # --- Drawing and Updates ---
    screen.blit(bg_surface, (0, 0))

    if game_active:
        bird.update(game_active)
        pipe_group.update()
        coin_group.update()
        bird.draw(screen)
        pipe_group.draw(screen)
        coin_group.draw(screen)
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
                    if p.rect.centerx == first_pipe.rect.centerx: p.passed = True

        # Coin collision logic
        if pygame.sprite.spritecollide(bird.sprite, coin_group, True):
            score += 1
            coin_sound.play()

        score_display('main_game')
    else:
        high_score = update_score(score, high_score)
        score_display('game_over')
        bird.update(game_active)
        bird.draw(screen)
        pipe_group.draw(screen)
        coin_group.draw(screen)

    # Animate the floor
    floor_x_pos -= SCROLL_SPEED
    if floor_x_pos <= -SCREEN_WIDTH: floor_x_pos = 0
    draw_floor()

    pygame.display.update()
    clock.tick(FPS)
