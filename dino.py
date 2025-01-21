import pygame


class Dino:
    X_POS = 80
    Y_POS = 310
    DUCK_Y_POS = 340
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.run_images = [
            pygame.image.load("assets/Dino/DinoRun1.png"),
            pygame.image.load("assets/Dino/DinoRun2.png"),
        ]
        self.jump_image = pygame.image.load("assets/Dino/DinoJump.png")
        self.duck_images = [
            pygame.image.load("assets/Dino/DinoDuck1.png"),
            pygame.image.load("assets/Dino/DinoDuck2.png"),
        ]
        self.image = self.run_images[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.running = True
        self.jumping = False
        self.ducking = False
        self.jump_velocity = self.JUMP_VELOCITY
        self.step_index = 0

    def update(self, keys, jump_sound):
        if self.jumping:
            self.jump()
        elif self.ducking:
            self.duck()
        else:
            self.run()
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            if not self.jumping:
                jump_sound.play()
                self.jumping = True
                self.running = False
                self.ducking = False
        elif keys[pygame.K_DOWN] and not self.jumping:
            self.ducking = True
            self.running = False
        else:
            self.running = True
            self.ducking = False
        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = self.run_images[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_image
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.jumping = False
            self.jump_velocity = self.JUMP_VELOCITY

    def duck(self):
        self.image = self.duck_images[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.DUCK_Y_POS
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
