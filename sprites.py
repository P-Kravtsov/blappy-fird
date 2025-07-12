import pygame
from settings import *

# Responsible: Pavel Kravtsov
class Bird(pygame.sprite.Sprite):
    """
    Represents the player's bird.
    Handles image loading, rect creation, gravity, and jumping.
    """
    def __init__(self, x, y):
        super().__init__()
        self.images = [
            pygame.transform.scale2x(pygame.image.load(path).convert_alpha())
            for path in ASSETS['bird']
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(x, y))

        # Physics and sound
        self.velocity = 0
        self.jump_sound = pygame.mixer.Sound(ASSETS['sounds']['jump'])

    def update(self):
        # Apply gravity
        self.velocity += GRAVITY
        # A simple terminal velocity to prevent falling too fast
        if self.velocity > 8:
            self.velocity = 8
        # Move the bird, but not past the placeholder floor
        if self.rect.bottom < 768:
            self.rect.y += int(self.velocity)

    def jump(self):
        self.velocity = JUMP_STRENGTH
        self.jump_sound.play()
