import pygame


res = (400, 300)
screen = pygame.display.set_mode(res)

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

#My colors
YELLOW = pygame.Color(200, 200, 30)

pygame.display.set_caption("Hello Pygame")

#Starting pygame
pygame.init()

default_font = pygame.font.get_default_font()
my_sysfont = pygame.font.SysFont('impact', 32)

my_font = pygame.font.Font(default_font, 34)

hello = my_sysfont.render('Hello World of Python', True, (10, 10, 10), YELLOW)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(YELLOW)
    screen.blit(hello, (10, 20))
    pygame.display.update()

pygame.quit()
#Ending pygame