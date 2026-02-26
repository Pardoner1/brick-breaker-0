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


current_state = "menu"
current_game = None

while appRunning:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            appRunning = False

        if current_state == "menu":
            handle_menu_event(event)

        elif current_state == "game":
            current_game.handle_event(event)

    if current_state == "menu":
        drawMenu()

    elif current_state == "game":
        current_game.update()
        current_game.draw()

        if current_game.gameFinished:
            games[current_game_name]["last_score"] = current_game.score
            current_state = "menu"
            current_game = None

    pygame.display.flip()
    clock.tick(45)

pygame.quit()