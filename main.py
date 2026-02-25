import pygame
from game import Game

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Brick Breaker")

app_running = True
clock = pygame.time.Clock()

def draw_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Press ENTER to Play", True, (255, 255, 255))
    rect = text.get_rect(center=(400, 400))
    screen.blit(text, rect)

while app_running:

    draw_menu()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game = Game(screen)
                result = game.run()

                if result == "QUIT":
                    app_running = False

    clock.tick(60)

pygame.quit()