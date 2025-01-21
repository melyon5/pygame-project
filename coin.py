import pygame
import random

class Coin:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            return False
        return True

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


def spawn_coin(image):
    x_pos = 1100
    y_pos = random.randint(250, 350)
    return Coin(x_pos, y_pos, image)
