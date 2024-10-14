import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    spaceship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #instance of Player class

    while True: #Game loop
        for event in pygame.event.get(): #Makes the window's close button work
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") #Creates game window/screen
        spaceship.draw(screen) #rendering the player on screen each frame using the .draw method from Player class
        pygame.display.flip()

        dt = clock.tick(60) / 1000 #limit the framerate to 60 FPS

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
   