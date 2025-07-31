import pygame
import random

# Initialize pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PACMAN_SIZE = 40
DOT_SIZE = 10
SPEED = 5

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pac-Man Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Define Pac-Man class
class PacMan:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.width = PACMAN_SIZE
        self.height = PACMAN_SIZE
        self.speed = SPEED
        self.direction = 'RIGHT'

    def move(self):
        if self.direction == 'UP':
            self.y -= self.speed
        elif self.direction == 'DOWN':
            self.y += self.speed
        elif self.direction == 'LEFT':
            self.x -= self.speed
        elif self.direction == 'RIGHT':
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.width // 2)

    def change_direction(self, new_direction):
        self.direction = new_direction

    def check_boundaries(self):
        if self.x < 0 or self.x > SCREEN_WIDTH or self.y < 0 or self.y > SCREEN_HEIGHT:
            return True  # Pac-Man is out of the frame
        return False

# Define Dot class
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = DOT_SIZE

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.size)

# Game function
def game():
    pacman = PacMan()
    dots = [Dot(random.randint(20, SCREEN_WIDTH - 20), random.randint(20, SCREEN_HEIGHT - 20)) for _ in range(20)]
    score = 0

    running = True
    while running:
        screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pacman.change_direction('UP')
                if event.key == pygame.K_DOWN:
                    pacman.change_direction('DOWN')
                if event.key == pygame.K_LEFT:
                    pacman.change_direction('LEFT')
                if event.key == pygame.K_RIGHT:
                    pacman.change_direction('RIGHT')

        # Move pacman
        pacman.move()

        # Check if Pac-Man eats a dot
        for dot in dots[:]:
            if pacman.x - pacman.width // 2 < dot.x < pacman.x + pacman.width // 2 and pacman.y - pacman.height // 2 < dot.y < pacman.y + pacman.height // 2:
                dots.remove(dot)
                score += 1

        # Check if Pac-Man goes out of bounds (dies)
        if pacman.check_boundaries():
            game_over(score)
            running = False

        # Draw Pac-Man and dots
        pacman.draw(screen)
        for dot in dots:
            dot.draw(screen)

        # Display score
        font = pygame.font.SysFont('Arial', 24)
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(30)

    # Quit pygame
    pygame.quit()

# Game over function
def game_over(score):
    screen.fill(BLACK)
    font = pygame.font.SysFont('Arial', 48)
    game_over_text = font.render('GAME OVER', True, RED)
    score_text = font.render(f'Your Score: {score}', True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3))
    screen.blit(score_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(2000)  # Wait for 2 seconds before closing

# Run the game
game()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               