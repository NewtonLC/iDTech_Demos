import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 500, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cookie Clicker Pygame Demo")

# Colors
BLACK = (0, 0, 0)
BACKGROUND = (120, 180, 250)
GRAY = (200, 200, 200)

# Font
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)
smaller_font = pygame.font.Font(None, 18)

# Load cookie image
cookie_image = pygame.image.load('assets/images/cookie.png')
cookie_rect = cookie_image.get_rect(center=(width // 2, height // 2))

# Score
score = 0

# Upgrade amounts & prices
clicker_amount = 0
oven_amount = 0
truck_amount = 0
clicker_cost = 10
oven_cost = 50
truck_cost = 100

# Button settings
button_width = 140
button_height = 70
button_margin = 20
clicker_button_rect = pygame.Rect(button_margin, height - button_height - button_margin, button_width, button_height)
oven_button_rect = pygame.Rect((width - button_width) // 2, height - button_height - button_margin, button_width, button_height)
truck_button_rect = pygame.Rect(width - button_width - button_margin, height - button_height - button_margin, button_width, button_height)

def draw_screen():
    screen.fill(BACKGROUND)

    # Draw the cookie
    if cookie_clicked:
        scaled_cookie = pygame.transform.scale(cookie_image, (int(cookie_rect.width * 0.9), int(cookie_rect.height * 0.9)))
        scaled_rect = scaled_cookie.get_rect(center=cookie_rect.center)
        screen.blit(scaled_cookie, scaled_rect)
    else:
        screen.blit(cookie_image, cookie_rect)

    # Draw the score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Draw the buttons
    pygame.draw.rect(screen, GRAY, clicker_button_rect)
    clicker_text1 = small_font.render("Clicker", True, BLACK)
    clicker_text2 = smaller_font.render("+1 cookie / second", True, BLACK)
    clicker_cost_text = smaller_font.render(f"Cost: {clicker_cost}", True, BLACK)
    screen.blit(clicker_text1, (clicker_button_rect.x + 10, clicker_button_rect.y + 10))
    screen.blit(clicker_text2, (clicker_button_rect.x + 10, clicker_button_rect.y + 30))
    screen.blit(clicker_cost_text, (clicker_button_rect.x + 10, clicker_button_rect.y + 50))

    pygame.draw.rect(screen, GRAY, oven_button_rect)
    oven_text1 = small_font.render("Oven", True, BLACK)
    oven_text2 = smaller_font.render("+5 cookies / second", True, BLACK)
    oven_cost_text = smaller_font.render(f"Cost: {oven_cost}", True, BLACK)
    screen.blit(oven_text1, (oven_button_rect.x + 10, oven_button_rect.y + 10))
    screen.blit(oven_text2, (oven_button_rect.x + 10, oven_button_rect.y + 30))
    screen.blit(oven_cost_text, (oven_button_rect.x + 10, oven_button_rect.y + 50))

    pygame.draw.rect(screen, GRAY, truck_button_rect)
    truck_text1 = small_font.render("Truck", True, BLACK)
    truck_text2 = smaller_font.render("+10 cookies / second", True, BLACK)
    truck_cost_text = smaller_font.render(f"Cost: {truck_cost}", True, BLACK)
    screen.blit(truck_text1, (truck_button_rect.x + 10, truck_button_rect.y + 10))
    screen.blit(truck_text2, (truck_button_rect.x + 10, truck_button_rect.y + 30))
    screen.blit(truck_cost_text, (truck_button_rect.x + 10, truck_button_rect.y + 50))

    # Draw the upgrade amounts above each button
    clicker_amount_text = small_font.render(f"Clickers: {clicker_amount}", True, BLACK)
    screen.blit(clicker_amount_text, (clicker_button_rect.x, clicker_button_rect.y - 30))

    oven_amount_text = small_font.render(f"Ovens: {oven_amount}", True, BLACK)
    screen.blit(oven_amount_text, (oven_button_rect.x, oven_button_rect.y - 30))

    truck_amount_text = small_font.render(f"Trucks: {truck_amount}", True, BLACK)
    screen.blit(truck_amount_text, (truck_button_rect.x, truck_button_rect.y - 30))

    # Update the display
    pygame.display.flip()

def handle_events():
    global running, cookie_clicked, score, clicker_amount, oven_amount, truck_amount, clicker_cost, oven_cost, truck_cost
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cookie_rect.collidepoint(event.pos):
                score += 1
                cookie_clicked = True
            if clicker_button_rect.collidepoint(event.pos) and score >= clicker_cost:
                clicker_amount += 1
                score -= clicker_cost
                clicker_cost = int(clicker_cost * 1.1)
            if oven_button_rect.collidepoint(event.pos) and score >= oven_cost:
                oven_amount += 1
                score -= oven_cost
                oven_cost = int(oven_cost * 1.1)
            if truck_button_rect.collidepoint(event.pos) and score >= truck_cost:
                truck_amount += 1
                score -= truck_cost
                truck_cost = int(truck_cost * 1.1)
        if event.type == pygame.MOUSEBUTTONUP:
            cookie_clicked = False
        """
        if event.type == ADD_COOKIES_EVENT:
            score += clicker_amount + oven_amount * 5 + truck_amount * 10
        """

"""
# Set up a timer event for adding cookies every second
ADD_COOKIES_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_COOKIES_EVENT, 1000)  # 1000 milliseconds = 1 second
"""

running = True
cookie_clicked = False
while running:
    handle_events()
    draw_screen()

pygame.quit()
sys.exit()