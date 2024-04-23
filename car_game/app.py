import pygame
import os

pygame.init()

FPS = 30
clock = pygame.time.Clock()
WIDTH, HEIGHT = (400, 600)

FRAME = pygame.display.set_mode((WIDTH, HEIGHT))
MY_CAR = pygame.image.load(os.path.join('assets', 'sprites', 'car.png'))
MY_ICON = pygame.image.load(os.path.join('assets', 'sprites', 'car.png'))
MY_ICON = pygame.transform.scale(MY_ICON, (32, 32))

CAR_SPEED = 5
car_pos = MY_CAR.get_rect()

pygame.display.set_caption('Car Game')
pygame.display.set_icon(MY_ICON)

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)


keys_pressed = pygame.key.get_pressed()

#using functions


#Adding fonts
my_font = pygame.font.SysFont('comicsansms', 16)

running = True

while running:
    clock.tick(FPS) #30 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_a, pygame.K_LEFT] and WIDTH > 0:
                car_pos.x -= CAR_SPEED
                print(car_pos.x)
            
    FRAME.fill(WHITE)
    pygame.draw.line(FRAME, BLACK, (195, 0), (195, HEIGHT), 10)

    FRAME.blit(MY_CAR, (car_pos.x + 190, car_pos.y + HEIGHT - 120))
    pygame.display.update()


pygame.quit()