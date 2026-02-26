import pygame
from brick_breaker import BrickBreaker
from space_shooter import SpaceShooter

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Game Hub")

clock = pygame.time.Clock()
appRunning = True

# Registro escalável de jogos
games = {
    "Brick Breaker": {
        "class": BrickBreaker,
        "last_score": 0
    },
    "Space Shooter": {
        "class": SpaceShooter,
        "last_score": 0
    }
}

selected_index = 0


def drawMenu():
    screen.fill((20, 20, 20))

    titleFont = pygame.font.SysFont(None, size)
    itemFont = pygame.font.SysFont(None, size)

    title = titleFont.render("Game Hub", True, (255, 255, 255))
    screen.blit(title, (300, 100))

    for index, game_name in enumerate(games.keys()):

        color = (255, 255, 0) if index == selected_index else (255, 255, 255)

        last_score = games[game_name]["last_score"]

        text = itemFont.render(
            f"{game_name}  |  Last Score: {last_score}",
            True,
            color
        )

        screen.blit(text, (200, 250 + index * 60))


while appRunning:

    drawMenu()
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            appRunning = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            
            for index, game_name in enumerate(games.keys()):
                rect = pygame.Rect(200, 250 + index * 60, 600, 50)
                if rect.collidepoint(mouse_x, mouse_y):
                    selected_index = index
                    game_name = list(games.keys())[selected_index]
                    game_class = games[game_name]["class"]

                    game_instance = game_class(screen)
                    result = game_instance.run()
                    games[game_name]["last_score"] = result["score"]

                if result["status"] == "QUIT":
                    appRunning = False

    clock.tick(45)

pygame.quit()