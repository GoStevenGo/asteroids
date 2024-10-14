import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True: #Game loop
        #Makes the window's close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Creates game window/screen
        screen.fill("black")
        pygame.display.flip()

        #limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
   