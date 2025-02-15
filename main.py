import pygame

# initialize pygame
pygame.init()

 # create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("StarfighterX")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

running  = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((0, 0, 0))

