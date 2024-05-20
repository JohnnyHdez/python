import pygame

pygame.init()
run = True

WIDTH = 300
HEIGHT = 200
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello Pygame')

BLACK = pygame.Color(10,10,10)
BLUE = pygame.Color(50, 50, 200)

while(run):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        SCREEN.fill(BLUE)
        pygame.draw.rect(SCREEN, BLACK, (WIDTH/2,HEIGHT/2,30,30))
        
        pygame.display.update()
        
pygame.quit()
