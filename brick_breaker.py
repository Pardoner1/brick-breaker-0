import pygame


class BrickBreaker:

    def __init__(self, screen):
        self.screen = screen
        self.displaySize = screen.get_size()

        self.colors = {
            "white": (255, 255, 255),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "black": (0, 0, 0),
            "yellow": (255, 255, 0),
            "red": (255, 0, 0)
        }

        self.gameScore = 0
        self.gameTimeFrame = 1
        self.playerSpeed = 5
        self.ballSpeed = 1
        self.maxSpeed = 10
        self.speedLevel = 0

        self.ballSize = 15
        self.ballMove = [self.ballSpeed, -self.ballSpeed]
        self.ball = pygame.Rect(100, 500, self.ballSize, self.ballSize)

        self.playerSize = 100
        self.player = pygame.Rect(0, 750, self.playerSize, self.ballSize)

        self.bricksPerRow = 8
        self.Rows = 5
        self.totalBricks = self.Rows * self.bricksPerRow
        self.bricks = self.makeBricks()

        self.running = True
        self.gameFinished = False
        self.gameWon = False

    # -----------------------------
    # Criação dos blocos
    # -----------------------------
    def makeBricks(self):
        brickHeight = 15
        bricksGaping = 5
        brickWidth = self.displaySize[0] / 8 - bricksGaping
        bricks = []

        for i in range(self.Rows):
            for j in range(self.bricksPerRow):
                brick = pygame.Rect(
                    j * (brickWidth + bricksGaping),
                    i * (brickHeight + bricksGaping),
                    brickWidth,
                    brickHeight
                )
                bricks.append(brick)

        return bricks

    # -----------------------------
    # Movimento do player
    # -----------------------------
    def playerMotion(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.player.x > 0:
            self.player.x -= self.playerSpeed

        if keys[pygame.K_RIGHT] and self.player.x < self.displaySize[0] - self.playerSize:
            self.player.x += self.playerSpeed

    # -----------------------------
    # Movimento da bola
    # -----------------------------
    def ballMotion(self):

        move = self.ballMove

        self.ball.x += move[0]
        self.ball.y += move[1]

        if self.ball.x < 0 or self.ball.x > self.displaySize[0] - self.ballSize:
            move[0] *= -1

        if self.ball.y < 0:
            move[1] *= -1

        if self.ball.y > self.displaySize[1] - self.ballSize:
            self.gameFinished = True
            self.gameWon = False
            return

        if self.ball.colliderect(self.player):
            move[1] *= -1

        for brick in self.bricks:
            if self.ball.colliderect(brick):
                move[1] *= -1
                self.bricks.remove(brick)
                self.gameScore += 1

                if self.gameScore % 2 == 0 and self.speedLevel < self.maxSpeed:
                    self.speedLevel += 1

                    move[0] += 1 if move[0] > 0 else -1
                    move[1] += 1 if move[1] > 0 else -1

                break

    # -----------------------------
    # Desenho
    # -----------------------------
    def draw(self):

        self.screen.fill(self.colors["black"])

        pygame.draw.rect(self.screen, self.colors["blue"], self.player)

        pygame.draw.circle(
            self.screen,
            self.colors["white"],
            self.ball.center,
            self.ballSize // 2
        )

        for brick in self.bricks:
            pygame.draw.rect(self.screen, self.colors["green"], brick)

        self.drawScore()

        if self.gameFinished:
            self.gameFinish()

    # -----------------------------
    # Score
    # -----------------------------
    def drawScore(self):
        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render(f"Score: {self.gameScore}",
                           True, self.colors["yellow"])
        self.screen.blit(text, (0, 780))

        if self.gameScore == self.totalBricks:
            self.gameFinished = True
            self.gameWon = True

    # -----------------------------
    # Finalização
    # -----------------------------
    def gameFinish(self):
        textValue = "You Win" if self.gameWon else "Game Over"
        colorType = "green" if self.gameWon else "red"

        self.ballMove = [0, 0]

        font = pygame.font.Font("freesansbold.ttf", 40)
        text = font.render(textValue, True, self.colors[colorType])
        rect = text.get_rect(
            center=(self.displaySize[0] // 2, self.displaySize[1] // 2))
        self.screen.blit(text, rect)

    # -----------------------------
    # Loop do jogo
    # -----------------------------
    def run(self):

        clock = pygame.time.Clock()

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "QUIT"

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return {
                        "status": "MENU",
                        "score": self.gameScore
                    }

            self.playerMotion()  # <- aqui, fora do for

            if not self.gameFinished:
                self.ballMotion()

            self.draw()
            pygame.display.flip()
            clock.tick(60)

        return {
            "status": "MENU",
            "score": self.gameScore
        }
