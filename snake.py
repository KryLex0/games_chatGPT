import asyncio
import time
from turtle import down, left, right, up
import pygame
import random

SCREEN_WIDTH = 40
SCREEN_HEIGHT = 30
CELL_SIZE = 20

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# This class represents the snake
class Snake:
    # Initialize the snake
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = WHITE

    # This method will move the snake
    def move(self):
        # Get the current position of the head of the snake
        cur = self.positions[0]
        x, y = cur
        # If the direction is UP, subtract 1 from y
        if self.direction == up:
            y -= 1
        # If the direction is DOWN, add 1 to y
        elif self.direction == down:
            y += 1
        # If the direction is LEFT, subtract 1 from x
        elif self.direction == left:
            x -= 1
        # If the direction is RIGHT, add 1 to x
        elif self.direction == right:
            x += 1
        # Set the new position of the snake's head
        self.positions = [(x, y)] + self.positions#[:-1]

        self.positions = self.positions[:self.length]

    # This method will draw the snake on the screen
    def draw(self, screen):
        for p in self.positions[:self.length]:
            draw_object(screen, self.color, p)

# This class represents the apple that the snake will eat
class Apple:
    # Initialize the apple
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    # This method will randomly place the apple
    def randomize_position(self):
        self.position = (random.randint(0, SCREEN_WIDTH - 1), random.randint(0, SCREEN_HEIGHT - 1))

    # This method will draw the apple on the screen
    def draw(self, screen):
        draw_object(screen, self.color, self.position)
    
    def drawGoldApple(self, snake, goldApple, screen, goldAppleVisible):
        if(goldAppleVisible == True):
            goldApple.draw(screen)
            if(check_eat(snake, goldApple)):
                print("golden apple")
                snake.length += 4
                goldAppleVisible = False


        if(goldAppleVisible == False):
            goldenAppleTimer = random.randint(0, 30)
            if(goldenAppleTimer == 15):
                # Draw the gold apple
                goldAppleVisible = True
        return goldAppleVisible

# This function will draw an object (either a snake or an apple) on the screen
def draw_object(screen, color, pos):
    r = pygame.Rect((pos[0] * CELL_SIZE, pos[1] * CELL_SIZE), (CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, color, r)
    pygame.display.update()

# This function will check if the snake has eaten an apple
def check_eat(snake, apple):
    if snake.positions[0] == apple.position:
        print("snake ate apple")
        snake.length += 1
        apple.randomize_position()
        return True
    # return snake

# This function will check if the snake has run into a wall or itself
def check_collision(snake):
    print(snake.positions[1:])
    if snake.positions[0] in snake.positions[1:]:
        print("snake collision")
        return True

    if snake.positions[0][0] < 0: # or snake.positions[0][0] > SCREEN_WIDTH - 1:
        x = SCREEN_WIDTH
        y = snake.positions[0][1]
        snake.positions = [(x, y)] + snake.positions[:-1]

        print("left wall collision")
        return False
    
    if snake.positions[0][0] > SCREEN_WIDTH - 1:
        x = 0
        y = snake.positions[0][1]
        snake.positions = [(x, y)] + snake.positions[:-1]
        print("right wall collision")
        return False
    
    if snake.positions[0][1] < 0: # or snake.positions[0][1] > SCREEN_HEIGHT - 1:
        x = snake.positions[0][0]
        y = SCREEN_HEIGHT
        snake.positions = [(x, y)] + snake.positions[:-1]
        print("top wall collision")
        return False

    if snake.positions[0][1] > SCREEN_HEIGHT - 1:
        x = snake.positions[0][0]
        y = 0
        snake.positions = [(x, y)] + snake.positions[:-1]
        print("bottom wall collision")
        return False

    return False


def main():
    print('Welcome to Snake!')
    # Initialize pygame
    pygame.init()

    # Set the screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH * CELL_SIZE, SCREEN_HEIGHT * CELL_SIZE))

    # Set the title of the window
    pygame.display.set_caption('Snake')

    # Create a clock
    clock = pygame.time.Clock()

    # Create a snake and an apple
    snake = Snake()
    apple = Apple()

    goldApple = Apple()
    goldApple.color = YELLOW

    goldAppleVisible = False

    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != down:
                    snake.direction = up
                elif event.key == pygame.K_DOWN and snake.direction != up:
                    snake.direction = down
                elif event.key == pygame.K_LEFT and snake.direction != right:
                    snake.direction = left
                elif event.key == pygame.K_RIGHT and snake.direction != left:
                    snake.direction = right

        # Draw the background
        screen.fill(BLACK)

        # Draw the apple
        apple.draw(screen)
        
        goldAppleVisible = goldApple.drawGoldApple(snake, goldApple, screen, goldAppleVisible)


        # Move the snake
        snake.move()

        # Check if the snake has eaten an apple
        check_eat(snake, apple)

        # Check if the snake has collided with itself or a wall
        if check_collision(snake):
            break

        # Draw the snake
        snake.draw(screen)

        # Update the screen
        pygame.display.update()

        # Set the speed of the game
        clock.tick(5)
        


    print('Final length: ', snake.length)
    pygame.quit()

if __name__ == '__main__':
    main()