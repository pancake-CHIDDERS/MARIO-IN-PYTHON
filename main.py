import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mario Game")

# Set up the player
player_width = 25
player_height = 40
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height
player_speed = 1

# Set up multiple objects
object_width = 50
object_height = 70
object_positions = [
    (700, 300),
    (400, 200),
    (100, 400)
]

# Game loop
running = True
while running:
    # Reset player speed
    player_speed = 1

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Store the player's previous position
    prev_player_x, prev_player_y = player_x, player_y

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Check for collision between player and each object
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for object_x, object_y in object_positions:
        object_rect = pygame.Rect(object_x, object_y, object_width, object_height)
        if player_rect.colliderect(object_rect):
            # Handle collision logic here
            print("Collision detected!")
            # Set player speed to 0
            player_speed = 0
            # Move the player back to its previous position
            player_x, player_y = prev_player_x, prev_player_y

    # Update the game window
    window.fill((0, 0, 0))  # Fill the window with black color
    pygame.draw.rect(window, (255, 0, 0), (player_x, player_y, player_width, player_height))  # Draw the player
    for object_x, object_y in object_positions:
        pygame.draw.rect(window, (0, 255, 0), (object_x, object_y, object_width, object_height))  # Draw each object
    pygame.display.update()

# Quit the game
pygame.quit()# Game loop
running = True
while running:
    # Reset player speed
    player_speed = 1

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Store the player's previous position
    prev_player_x, prev_player_y = player_x, player_y

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Check for collision between player and object
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    object_rect = pygame.Rect(object_x, object_y, object_width, object_height)
    if player_rect.colliderect(object_rect):
        # Handle collision logic here
        print("Collision detected!")
        # Set player speed to 0
        player_speed = 0
        # Move the player back to its previous position
        player_x, player_y = prev_player_x, prev_player_y

    # Update the game window
    window.fill((0, 0, 0))  # Fill the window with black color
    pygame.draw.rect(window, (255, 0, 0), (player_x, player_y, player_width, player_height))  # Draw the player
    pygame.draw.rect(window, (0, 255, 0), (object_x, object_y, object_width, object_height))  # Draw the object
    pygame.display.update()

# Quit the game
pygame.quit()