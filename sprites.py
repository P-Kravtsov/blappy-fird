import pygame
from settings import *

# Responsible: Pavel Kravtsov
class Bird(pygame.sprite.Sprite):
    """
    Represents the player's bird.
    Handles image loading, rect creation, gravity, jumping, animation, and rotation.
    """
    def __init__(self, x, y):
        super().__init__()
        self.images = [
            pygame.transform.scale2x(pygame.image.load(path).convert_alpha())
            for path in ASSETS['bird']
        ]
        # Animation state
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))

        # Physics and sound
        self.velocity = 0
        self.animation_counter = 0
        self.animation_cooldown = 5
        self.jump_sound = pygame.mixer.Sound(ASSETS['sounds']['jump'])

    def update(self, game_active):
        # Animate the bird first
        self._animate()
        # Then apply physics and rotation only if the game is active
        if game_active:
            self._apply_gravity()
            self._rotate()
        else:
            # On game over, show a static, rotated bird
            self.image = pygame.transform.rotozoom(self.images[self.index], -90, 1)

    def jump(self):
        self.velocity = JUMP_STRENGTH
        self.jump_sound.play()

    def _apply_gravity(self):
        """Applies gravity to the bird."""
        self.velocity += GRAVITY
        if self.velocity > 8: self.velocity = 8
        if self.rect.bottom < 768: self.rect.y += int(self.velocity)

    def _rotate(self):
        """Rotates the bird image based on its vertical velocity."""
        # We create a new rotated image to avoid quality loss
        self.image = pygame.transform.rotozoom(self.images[self.index], -self.velocity * 3, 1)

    def _animate(self):
        """Cycles through the bird images to create a flapping animation."""
        self.animation_counter += 1
        if self.animation_counter > self.animation_cooldown:
            self.animation_counter = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

#Anastasiya Trafimovich
class Pipe(pygame.sprite.Sprite):
    # MODIFICATION: The constructor now accepts a pre-loaded pipe_image
    def __init__(self, x, y, position, pipe_image):
        super().__init__()
        self.image = pipe_image # Use the image passed from main.py
        self.rect = self.image.get_rect()
        self.passed = False

        if position == 1: # Top pipe
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(PIPE_GAP / 2)]
        if position == -1: # Bottom pipe
            self.rect.topleft = [x, y + int(PIPE_GAP / 2)]

    def update(self):
        self.rect.x -= SCROLL_SPEED
        if self.rect.right < 0:
            self.kill()
