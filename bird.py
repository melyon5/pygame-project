import pygame
import random

class Bird:
    BIRD_HEIGHTS = [250, 300, 310]

    def __init__(self):
        self.images = [
            pygame.image.load("assets/Bird/Bird1.png"),
            pygame.image.load("assets/Bird/Bird2.png"),
        ]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = random.choice(self.BIRD_HEIGHTS)
        self.animation_counter = 0

    def update(self, game_speed):
        self.animation_counter += 1
        if self.animation_counter >= 10:
            self.animation_counter = 0
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]

        self.rect.x -= game_speed - 2
        if self.rect.x < -self.rect.width:
            return False
        return True

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
