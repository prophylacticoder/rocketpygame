import pygame
import sys
import settings
import spacecraft
import game_functions as gf

def run_game():
  pygame.init()
  rocket_settings = settings.Settings()
  screen = pygame.display.set_mode((rocket_settings.height, rocket_settings.width))
  pygame.display.set_caption('Rocket Game')
  rocket = spacecraft.Spacecraft(screen)

  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.quit
        gf.deal_with_up_events(event, rocket)
        gf.deal_with_down_events(event, rocket)
    rocket.moving_rocket()
    gf.update_screen(rocket_settings, screen, rocket)

run_game()
