import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dice Roll Pygame Demo")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Font
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Dice settings
dice = []
dice_results = []

# Button settings
button_rect = pygame.Rect(width // 2 + 60, height // 2 + 150, 100, 50)

# Input box settings
input_box = pygame.Rect(width // 2 - 160, height // 2 + 150, 100, 50)
input_text = ''

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Roll one die
                dice_results[0] = random.randint(1, dice[0])
                """
                # Roll all dice
                # dice_results = [random.randint(1, sides) for sides in dice]
                """
            if input_box.collidepoint(event.pos):
                input_text = ''
            else: 
                # Check if a dice was clicked to remove it
                dice_size = 100
                margin = 10
                columns = 5
                for i in range(len(dice)):
                    row = i // columns
                    col = i % columns
                    x = margin + col * (dice_size + margin)
                    y = margin + row * (dice_size + margin)
                    dice_rect = pygame.Rect(x, y, dice_size, dice_size)
                    if dice_rect.collidepoint(event.pos):
                        del dice[i]
                        del dice_results[i]
                        break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text.isdigit():
                    dice_sides = int(input_text)
                    dice.append(dice_sides)
                    dice_results.append(dice_sides)
                    input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
    
    # Fill the screen with a color (e.g., off-white)
    screen.fill(WHITE)

    # Draw the input box
    label_text = small_font.render("Add a die with # sides:", True, BLACK)
    screen.blit(label_text, (input_box.x - 35, input_box.y - 30))
    pygame.draw.rect(screen, GRAY, input_box)
    input_surface = font.render(input_text, True, BLACK)
    screen.blit(input_surface, (input_box.x + 10, input_box.y + 10))

    # Draw the button
    pygame.draw.rect(screen, GRAY, button_rect)
    button_text = font.render("Roll", True, BLACK)
    screen.blit(button_text, (button_rect.x + 20, button_rect.y + 10))

    # Draw the dice results in a grid layout
    dice_size = 100
    margin = 10
    columns = 5  # Number of columns in the grid
    for i, result in enumerate(dice_results):
        row = i // columns
        col = i % columns
        x = margin + col * (dice_size + margin)
        y = margin + row * (dice_size + margin)
        dice_rect = pygame.Rect(x, y, dice_size, dice_size)
        pygame.draw.rect(screen, GRAY, dice_rect)
        result_text = font.render(str(result), True, BLACK)
        screen.blit(result_text, (dice_rect.x + (dice_rect.width - result_text.get_width()) // 2,
                                  dice_rect.y + (dice_rect.height - result_text.get_height()) // 2))

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()