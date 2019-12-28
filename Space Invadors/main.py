import pygame
import math
import random

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))
running = True

# title and icon
pygame.display.set_caption("Space Invador")
icon = pygame.image.load('Space Invadors\\ufo.png')
pygame.display.set_icon(icon)
background = pygame.image.load("Space Invadors\\background.png")

# Player
playerImg = pygame.image.load(f"Space Invadors\space-ship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load(f"Space Invadors\enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 1
enemyY_change = 30

# Bullet
bulletImg = pygame.image.load("Space Invadors\\bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 20

# "ready" - You can't see the bullet
# "fire" - Bullet is moving
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def is_collision(X1, X2, Y1, Y2):
    distance = math.sqrt(math.pow(X2 - x1, 2) + math.pow(Y2 - Y1, 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
while running:
    screen.fill((0, 0, 0))

    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check it
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state = "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

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
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
