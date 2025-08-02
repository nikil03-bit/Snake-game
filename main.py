import pygame
import random

pygame.init()

# Screen size
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
green = (0, 255, 0)
red = (255, 0, 0)

# Load background image and scale to screen size
background_image = pygame.image.load('background.png')
background = pygame.transform.scale(background_image, (width, height))

# Load and play background music
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)  # Loop indefinitely

# Snake parameters
snake_block = 20
snake_list = []
length_of_snake = 1

# Initial positions
x1, y1 = width // 2, height // 2
x1_change = 0
y1_change = 0

# Food initial position
food_x = 300
food_y = 200

clock = pygame.time.Clock()
running = True
game_close = False

font_style = pygame.font.SysFont(None, 35)

def show_message(msg, color):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(width // 2, height // 2))
    window.blit(mesg, mesg_rect)

while running:
    while game_close:
        window.blit(background, (0, 0))
        show_message("Game Over! Press C-Play Again or Q-Quit", red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_close = False
                    running = False
                if event.key == pygame.K_c:
                    # Reset game state
                    x1, y1 = width // 2, height // 2
                    x1_change = 0
                    y1_change = 0
                    snake_list = []
                    length_of_snake = 1
                    food_x = 300
                    food_y = 200
                    game_close = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    # Update snake position
    x1 += x1_change
    y1 += y1_change

    # Check boundaries (for game over)
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_close = True

    window.blit(background, (0, 0))

    # Draw food
    pygame.draw.rect(window, red, [food_x, food_y, snake_block, snake_block])

    # Update snake list
    snake_head = [x1, y1]
    snake_list.append(snake_head)
    
    if len(snake_list) > length_of_snake:
        del snake_list[0]

    # Check for self collision
    for block in snake_list[:-1]:
        if block == snake_head:
            game_close = True

    # Draw snake
    for block in snake_list:
        pygame.draw.rect(window, green, [block[0], block[1], snake_block, snake_block])

    pygame.display.update()

    # Check if snake ate the food
    if x1 == food_x and y1 == food_y:
        food_x = random.randrange(0, (width - snake_block) // snake_block) * snake_block
        food_y = random.randrange(0, (height - snake_block) // snake_block) * snake_block
        length_of_snake += 1

    clock.tick(15)  # Controls the speed of the game

pygame.quit()
