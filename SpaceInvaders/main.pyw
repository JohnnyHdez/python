import pygame
import math
import random
import os

pygame.init()

screenWidth = 800
screenHeight = 600

SCREEN_BG_COLOR = pygame.Color(32, 64, 128)
WHITE = pygame.Color(255, 255, 255)

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Space Invaders")

level = 1
score = 0

player_pos_x = 368
player_pos_y = 520

bullet_load = False
bullet_pos_x = 368
bullet_pos_y = 560

enemy_pos_x = random.randint(10, 790)
enemy_pos_y = random.randint(30, 170)
enemy_dir_x = 0
enemy_dir_y = 0

running = True

def enemy(x: int, y: int):
	enemyImgPath = os.path.join("img", "enemy.png")
	enemyImg = pygame.image.load(enemyImgPath)
	enemyImg = pygame.transform.scale(enemyImg, (64, 64))
	enemyPos = enemyImg.get_rect()

	screen.blit(enemyImg, (x + enemy_dir_x, y + enemy_dir_y))

def player(x: int, y: int):
	playerImgPath = os.path.join("img", "player.png")
	playerImg = pygame.image.load(playerImgPath)
	playerImg = pygame.transform.scale(playerImg, (64, 64))
	screen.blit(playerImg, (x, y))

def background(x: int, y: int):
	font = pygame.font.Font("freesansbold.ttf", 28)

	scoretxt = font.render("Score {}".format(score), True, WHITE)
	leveltxt = font.render("Level {}".format(level), True, WHITE)

	screen.fill(SCREEN_BG_COLOR)
	screen.blit(scoretxt, (x+250, y))
	screen.blit(leveltxt, (x, y))

def player_life():
	playerImgPath = os.path.join("img", "player.png")
	playerImg = pygame.image.load(playerImgPath)
	playerImg = pygame.transform.scale(playerImg, (24, 24))
	player_current_life = []
	player_current_life.append(playerImg)
	player_current_life.append(playerImg)
	player_current_life.append(playerImg)

	screen.blit(player_current_life[0], (740, 10))
	screen.blit(player_current_life[0], (700, 10))
	screen.blit(player_current_life[0], (660, 10))

def bullets(x: int, y: int):
	bulletImgPath = os.path.join("img", "player.png")
	bulletImg = pygame.image.load(bulletImgPath)
	bulletImg = pygame.transform.scale(bulletImg, (16, 16))

	screen.blit(bulletImg, (x, y))

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if player_pos_x > 10:
				if event.key == pygame.K_LEFT:
					player_pos_x -= 20
					#bullet_pos_x -= 20
				if event.key == pygame.K_SPACE:
					bullet_load = True
				
			if player_pos_x < 726:
				if event.key == pygame.K_RIGHT:
					player_pos_x += 20
					bullet_pos_x += 20

	if bullet_load == True:
		bullet_pos_y -= 15
	if bullet_pos_y <= 0:
		bullet_load = False
		bullet_pos_y = 530
		

	

	background(20, 10)
	player_life()

	enemy_pos_x += enemy_dir_x
	if enemy_pos_x >= 10:
		enemy_dir_x = 15
	elif enemy_pos_x <= 770:
		enemy_dir_x = -15

	enemy(enemy_pos_x, enemy_pos_y)
	player(player_pos_x, player_pos_y)
	bullets(bullet_pos_x + 30, bullet_pos_y)

	pygame.display.update()

pygame.quit()
