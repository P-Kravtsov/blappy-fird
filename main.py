import pygame
import sys
import random
from settings import *
from sprites import Bird, Pipe, Coin
from messages import * # ADDED: Import messages


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
    return 0, 0 # Return (score, coin_score)

def load_high_score():
    """Loads the high score from a file."""
    try:
        with open(HIGHSCORE_FILE, 'r') as f: return int(f.read())
    except (FileNotFoundError, ValueError): return 0

def update_score(current_score, high_score_val):
    """Updates the high score if the current score is higher."""
    if current_score > high_score_val:
        high_score_val = current_score
        with open(HIGHSCORE_FILE, 'w') as f: f.write(str(high_score_val))
    return high_score_val


def score_display(game_state):
    """Displays the current score or the final score and high score."""
    # icon score - coins (while active)
    if game_state == 'main_game':
        screen.blit(coin_icon, (15, 15))
        coin_score_surface = game_font.render(str(coin_score), True, (255, 255, 255))
        coin_score_rect = coin_score_surface.get_rect(topleft=(75, 25))
        screen.blit(coin_score_surface, coin_score_rect)

    if game_state == 'main_game':
        # main pipes score
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
        # ADDED: Display the death message
        message_surface = game_font_small.render(death_message, True, (255, 255, 255))
        message_rect = message_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
        screen.blit(message_surface, message_rect)

# --- Initialization ---
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Blappy Fird')
clock = pygame.time.Clock()
game_font = pygame.font.Font(FONT_PATH, 70)
game_font_small = pygame.font.Font(FONT_PATH, 30) # ADDED: Smaller font for messages

# --- Game State Variables ---
game_active = False
score = 0
coin_score = 0 # Новый счетчик для монет
high_score = load_high_score()
floor_x_pos = 0
death_message = ""

# --- Asset Loading & Theming ---
current_theme_name = random.choice(list(ASSETS['themes'].keys()))
current_theme = ASSETS['themes'][current_theme_name]
bg_surface = pygame.transform.scale2x(pygame.image.load(current_theme['background']).convert())
floor_surface = pygame.transform.scale2x(pygame.image.load(current_theme['ground']).convert())
pipe_image = pygame.transform.scale2x(pygame.image.load(current_theme['pipe']).convert_alpha())

death_sound = pygame.mixer.Sound(ASSETS['sounds']['hit'])
score_sound = pygame.mixer.Sound(ASSETS['sounds']['score'])
coin_sound = pygame.mixer.Sound(ASSETS['sounds']['coin'])
coin_icon = pygame.transform.scale(pygame.image.load(ASSETS['coin']).convert_alpha(), (50, 50))

# --- Sprites ---
bird = pygame.sprite.GroupSingle(Bird(100, SCREEN_HEIGHT / 2))
pipe_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

# --- Timer for Spawning Pipes ---
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, PIPE_FREQUENCY)
pipe_height = [350, 450, 550, 600]

# --- Timer for Spawning Coins (NEW) ---
SPAWNCOIN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNCOIN, random.randint(1000, 3000)) # Spawn every 1-3 seconds

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
                    game_active = True
                    score, coin_score = reset_game()  # Присваиваем оба значения
                    death_message = "" # Reset death message on restart
                    # Reload theme assets on restart
                    current_theme_name = random.choice(list(ASSETS['themes'].keys()))
                    current_theme = ASSETS['themes'][current_theme_name]
                    bg_surface = pygame.transform.scale2x(pygame.image.load(current_theme['background']).convert())
                    floor_surface = pygame.transform.scale2x(pygame.image.load(current_theme['ground']).convert())
                    pipe_image = pygame.transform.scale2x(pygame.image.load(current_theme['pipe']).convert_alpha())

        # --- spawn pipes and coins logic ---
        if event.type == SPAWNPIPE and game_active:
            pipe_y = random.choice(pipe_height)
            bottom_pipe = Pipe(SCREEN_WIDTH + 50, pipe_y, -1, pipe_image)
            top_pipe = Pipe(SCREEN_WIDTH + 50, pipe_y, 1, pipe_image)
            pipe_group.add(bottom_pipe, top_pipe)

        if event.type == SPAWNCOIN and game_active:
            # Create a temporary coin to check for collisions
            temp_coin = Coin(SCREEN_WIDTH + 50, 0)

            # Find a safe Y position for the coin
            is_safe = False
            while not is_safe:
                # Choose a random Y position
                coin_y = random.randint(100, SCREEN_HEIGHT - 200)
                temp_coin.rect.center = (SCREEN_WIDTH + 50, coin_y)

                # Check if this position collides with any pipe
                if not pygame.sprite.spritecollide(temp_coin, pipe_group, False):
                    is_safe = True

            # Add the coin with the safe position to the group
            coin_group.add(Coin(SCREEN_WIDTH + 50, coin_y))

            # Reset the timer with a new random interval
            pygame.time.set_timer(SPAWNCOIN, random.randint(1000, 3000))


    # --- Drawing and Updates ---
    screen.blit(bg_surface, (0, 0))

    if game_active:
        # --- ACTIVE GAME LOGIC ---
        bird.update(game_active)
        pipe_group.update()
        coin_group.update()
        bird.draw(screen)
        pipe_group.draw(screen)
        coin_group.draw(screen)

        # --- Floor Animation (runs in all states) ---
        floor_x_pos -= SCROLL_SPEED
        if floor_x_pos <= -SCREEN_WIDTH:
            floor_x_pos = 0

        game_active = check_collision(pipe_group)

        # SCORING LOGIC (Corrected)
        # We only check the bottom pipes to avoid double counting.
        for pipe in pipe_group:
            if pipe.is_bottom and not pipe.passed and pipe.rect.centerx < bird.sprite.rect.centerx:
                pipe.passed = True
                score += 1 # +1 к основному счету за трубы
                score_sound.play()

        # Coin collision logic
        if pygame.sprite.spritecollide(bird.sprite, coin_group, True):
            coin_score += 1
            coin_sound.play()

        score_display('main_game')

    else:  # --- GAME OVER / START SCREEN LOGIC ---
        high_score = update_score(score, high_score)

        if score == 0: # Start screen
            title_surface = game_font.render("Blappy Fird", True, (255, 255, 255))
            title_rect = title_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100))
            screen.blit(title_surface, title_rect)
            start_surface = game_font_small.render("Press SPACE to start", True, (255, 255, 255))
            start_rect = start_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            screen.blit(start_surface, start_rect)
        else: # Game over screen
            if not death_message: # Set death message only once per game over
                death_message = random.choice(DEATH_MESSAGES)
            score_display('game_over')

        # Draw static bird on game over/start screen
        bird.draw(screen)

    draw_floor()

    pygame.display.update()
    clock.tick(FPS)