import pygame


class Bullet():
    def __init__(self):
        self.image = pygame.image.load('photos/bullet.png')
        self.positionX = 2000
        self.positionY = 480
        self.bullet_state = 'ready'
        self.moveY = 0
        self.speed = 10

    def bullet_keydown(self, event, player_position):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.bullet_state == 'ready':
                    self.bullet_state = 'fire'
                    self.positionX = player_position

    def movement(self):
        if self.bullet_state == 'fire':
            self.moveY = self.speed

        self.positionY -= self.moveY

    def reload(self):
        if self.positionY < 20:
            self.bullet_state = 'ready'

        if self.bullet_state == 'ready':
            self.positionY = 480
            self.positionX = 2000
            self.moveY = 0
