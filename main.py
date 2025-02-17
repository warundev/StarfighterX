import random

import pygame

# initialize pygame
pygame.init()

 # create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.png')


# title and icon
pygame.display.set_caption("StarfighterX")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = pygame.image.load('monster.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 2.5
enemyY_change = 40

def player(x,y):
  screen.blit(playerImg, (x, y))

def enemy(x,y):
  screen.blit(enemyImg, (x, y))

# game loop
running  = True
while running:

  screen.fill((0, 0, 0))
  screen.blit(background, (0, 0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # moving the player
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        playerX_change = -5
      if event.key == pygame.K_RIGHT:
        playerX_change = 5
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        playerX_change = 0


  playerX += playerX_change

  if playerX <= 0:
    playerX = 0
  elif playerX >= 736:
    playerX = 736

  enemyX += enemyX_change

  if enemyX <= 0:
    enemyX_change = 3
    enemyY += enemyY_change
  elif enemyX >= 736:
    enemyX_change = -3
    enemyY += enemyY_change

  player(playerX,playerY)
  enemy(enemyX, enemyY)
  pygame.display.update()

