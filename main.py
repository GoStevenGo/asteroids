import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable) #adding all future Player instances to these groups

    spaceship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #instance of Player class

    while True: #Game loop
        for event in pygame.event.get(): #Makes the window's close button work
            if event.type == pygame.QUIT:
                return

        for object in updatable:
            object.update(dt) #checks for user input (WASD) for player rotation and movement 

        screen.fill("black") #Creates game window/screen

        for object in drawable:
            object.draw(screen) #Creates the player on screen each frame using the .draw method from Player class

        pygame.display.flip() #renders everything above

        dt = clock.tick(60) / 1000 #limit the framerate to 60 FPS



if __name__ == "__main__":
    main()
   