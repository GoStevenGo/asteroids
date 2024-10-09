import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        #Makes the window's close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Creates game screen
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
   