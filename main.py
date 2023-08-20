
from typing import Any
import pygame
import random

#class for crosshair
class Crosshair(pygame.sprite.Sprite):
    def __init__(self,picture_path):
        super().__init__()
        # gives surface image
        self.image = pygame.image.load('images\\'+picture_path)
        # makes image rectangle
        self.rect = self.image.get_rect()
        # gunshot sound
        self.gunshot = pygame.mixer.Sound('sound\\gun.mp3') # Sound Effect from Pixabay
        # duck sound
        self.ducksound = pygame.mixer.Sound('sound\\duck.mp3') # Sound Effect from Pixabay
    
    # shooting 
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair,target_group,True)
    
    def deadduck(self):
        self.ducksound.play()
       
    # updates crosshair position
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        return super().update()


#class for target
class Target(pygame.sprite.Sprite):
    def __init__(self,picture_path,pos_x,pos_y):
        super().__init__()
        
        # gives surface image
        self.image = pygame.image.load('images\\'+picture_path)
        # makes image rectangle
        self.rect = self.image.get_rect()
        
        self.rect.center = [pos_x,pos_y]




# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
fps = 60

# resolution
display_height = 720
display_width = 1280

# background
screen = pygame.display.set_mode((display_width, display_height))
background = pygame.image.load('images\\Background.jpg')

# mouse visibility
pygame.mouse.set_visible(False)

# crosshair
crosshair = Crosshair('crosshair_blue_small.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target('target.png',random.randrange(0,display_width-50),random.randrange(0,display_height-50))
    target_group.add(new_target)
    

while running:
    # poll for events
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # gunshot sound when clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

            
            
    
   
    # Draws the surface object to the screen.
    pygame.display.update()
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    
    # sets background image
    screen.blit(background,(0,0))
    
    #draws targets
    target_group.draw(screen)
    
    # crosshair linked with mouse movement
    crosshair_group.draw(screen)
    crosshair_group.update()
    


    # limits FPS to 60
    clock.tick(fps)  

pygame.quit()