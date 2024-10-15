import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable) #adding all future Player instances to these groups
    Asteroid.containers = (asteroids, updatable, drawable) #adding all future Asteroid instances to these groups
    AsteroidField.containers = (updatable) #adding all future AsteroidField instances to this one group
    Shot.containers = (shots, updatable, drawable) #you know at this point

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #instance of Player class
    asteroid_field = AsteroidField()

    while True: #Game loop
        for event in pygame.event.get(): #Makes the window's close button work
            if event.type == pygame.QUIT:
                return

        for object in updatable:
            object.update(dt) #checks for user input (WASD) for player rotation and movement 

        for asteroid in asteroids:
            if asteroid.is_colliding(player): #checks for collision between player and all asteroids
                print("Game Over!") #gets printed to console, not game screen since it's exiting the next line
                return
            
            for shot in shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black") #Creates game window/screen

        for object in drawable:
            object.draw(screen) #Creates the player on screen each frame using the .draw method from Player class

        pygame.display.flip() #renders everything above

        dt = clock.tick(60) / 1000 #limit the framerate to 60 FPS



if __name__ == "__main__":
    main()
   