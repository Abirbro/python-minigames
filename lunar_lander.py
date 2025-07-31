import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Asteroid Avoidance")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the clock for framerate control
clock = pygame.time.Clock()

# Define the spaceship
spaceship_width = 50
spaceship_height = 50
spaceship_x = screen_width // 2 - spaceship_width // 2
spaceship_y = screen_height - spaceship_height - 10
spaceship_speed = 7

# Define the asteroid
asteroid_width = 50
asteroid_height = 50
asteroid_speed = 5

# Set up the font
font = pygame.font.SysFont("Arial", 30)

# Game over function
def game_over():
    text = font.render("Game Over!", True, RED)
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)  # Show "Game Over" for 2 seconds
    pygame.quit()
    sys.exit()

# Set up the asteroid list
asteroids = []

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key handling for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_x > 0:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT] and spaceship_x < screen_width - spaceship_width:
        spaceship_x += spaceship_speed

    # Add new asteroids
    if random.randint(1, 30) == 1:  # Randomly create asteroids
        asteroid_x = random.randint(0, screen_width - asteroid_width)
        asteroids.append([asteroid_x, -asteroid_height])

    # Move asteroids down
    for asteroid in asteroids[:]:
        asteroid[1] += asteroid_speed
        if asteroid[1] > screen_height:  # Remove off-screen asteroids
            asteroids.remove(asteroid)
        
        # Check for collision with spaceship
        if (spaceship_x < asteroid[0] + asteroid_width and spaceship_x + spaceship_width > asteroid[0] and
            spaceship_y < asteroid[1] + asteroid_height and spaceship_y + spaceship_height > asteroid[1]):
            game_over()

    # Fill the screen with black color
    screen.fill(BLACK)

    # Draw the spaceship (a simple rectangle)
    pygame.draw.rect(screen, WHITE, (spaceship_x, spaceship_y, spaceship_width, spaceship_height))

    # Draw the asteroids
    for asteroid in asteroids:
        pygame.draw.rect(screen, RED, (asteroid[0], asteroid[1], asteroid_width, asteroid_height))

    # Update the display
    pygame.display.flip()

    # Control the frame rate (60 frames per second)
    clock.tick(60) 
    
    
