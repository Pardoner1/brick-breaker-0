import pygame
from brick_breaker import BrickBreaker
from space_shooter import SpaceShooter

pygame.init()

info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h))
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

    titleFont = pygame.font.Font(None, 60)
    itemFont = pygame.font.Font(None, 40)

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

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                selected_index = max(0, selected_index - 1)

            if event.key == pygame.K_DOWN:
                selected_index = min(len(games) - 1, selected_index + 1)

            if event.key == pygame.K_RETURN:

                game_name = list(games.keys())[selected_index]
                game_class = games[game_name]["class"]

                game_instance = game_class(screen)
                result = game_instance.run()

                games[game_name]["last_score"] = result["score"]

                if result["status"] == "QUIT":
                    appRunning = False

    clock.tick(45)

pygame.quit()