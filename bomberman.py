import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 40
SCREEN_HEIGHT = 30
CELL_SIZE = 20


# This class represents the bomberman character
class BomberMan:
    # Initialize the bomberman
    def __init__(self):
        self.position = (100, 100)
        self.color = WHITE
        self.speed = 5

    # This method will move the bomberman
    def move(self, direction):
        if direction == "up":
            self.position = (self.position[0], self.position[1] - self.speed)
        elif direction == "down":
            self.position = (self.position[0], self.position[1] + self.speed)
        elif direction == "left":
            self.position = (self.position[0] - self.speed, self.position[1])
        elif direction == "right":
            self.position = (self.position[0] + self.speed, self.position[1])

    # This method will draw the bomberman on the screen
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], 50, 50))

# This class represents the enemies
class Enemy:
    # Initialize the enemy
    def __init__(self):
        self.position = (100, 200)
        self.color = RED
        self.speed = 5

    # This method will move the enemy
    def move(self):
        self.position = (self.position[0] + self.speed, self.position[1])

    # This method will draw the enemy on the screen
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], 50, 50))

# This class represents the bombs
class Bomb:
    # Initialize the bomb
    def __init__(self):
        self.position = (0, 0)
        self.color = GREEN
        self.timer = 60

    # This method will update the bomb's timer
    def update(self):
        self.timer -= 1

    # This method will draw the bomb on the screen
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], 50, 50))

def main():
    # Initialize pygame
    pygame.init()

    # Set the screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH * CELL_SIZE, SCREEN_HEIGHT * CELL_SIZE))

    # Set the title of the window
    pygame.display.set_caption('BomberMan')

    # Create a bomberman, an enemy, and a bomb
    bomberman = BomberMan()
    enemy = Enemy()
    bomb = Bomb()

    # Loop until the user clicks the close button
    done = False
    while not done:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bomberman.move("up")
                elif event.key == pygame.K_DOWN:
                    bomberman.move("down")
                elif event.key == pygame.K_LEFT:
                    bomberman.move("left")
                elif event.key == pygame.K_RIGHT:
                    bomberman.move("right")
                elif event.key == pygame.K_SPACE:
                    bomb.position = bomberman.position

        # Update the bomb's timer
        bomb.update()

        # Clear the screen
        screen.fill(BLACK)

        # Draw the bomberman, enemy, and bomb
        bomberman.draw(screen)
        enemy.draw(screen)
        bomb.draw(screen)

        # Update the screen
        pygame.display.flip()


if __name__ == '__main__':
    main()