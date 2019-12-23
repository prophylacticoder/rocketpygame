import pygame
import settings

def update_screen(rocket_settings, screen, rocket):
  screen.fill(rocket_settings.bg_color)
  rocket.blitme()
  pygame.display.flip()

def deal_with_down_events(event, rocket):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            rocket.moving_down = True
        elif event.key == pygame.K_RIGHT:
            rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            rocket.moving_left = True

def deal_with_up_events(event, rocket):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            rocket.moving_down = False
        elif event.key == pygame.K_RIGHT:
            rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            rocket.moving_left = False
