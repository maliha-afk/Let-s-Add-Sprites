#Colorful bounce

import pygame

pygame.init()
screen=pygame.display.set_mode((900,900))
pygame.display.set_caption("myfirst game")
x=450
y=450
sprite= pygame.image.load("ship.png")
sprite_rect= sprite.get_rect(center=(x,y))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    key=pygame.key.get_pressed()
    
    if key[pygame.K_LEFT]:
        x=x-5
    
    if key[pygame.K_RIGHT]:
        x=x+5

    
    if key[pygame.K_DOWN]:
        y=y-5
    
    if key[pygame.K_UP]:
        y=y+5
    sprite_rect.center=(x,y)
    
    screen.blit(sprite,sprite_rect)
    pygame.display.flip()