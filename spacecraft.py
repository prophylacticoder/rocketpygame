import pygame

class Spacecraft():
    def __init__(self, screen):
        self.screen = screen
        # Loads the spacecraft and get its rect
        self.image = pygame.image.load('images/spacecraft.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Position the spacecraft in the middle of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship on the screen in the rect position."""
        self.screen.blit(self.image, self.rect)

    def moving_rocket(self):
        """Function responsible for moving the rocket."""
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
