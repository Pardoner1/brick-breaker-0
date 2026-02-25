import pygame
import random


class SpaceShooter:

    def __init__(self, screen):
        self.screen = screen
        self.displaySize = screen.get_size()
        self.clock = pygame.time.Clock()

        self.colors = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "yellow": (255, 255, 0)
        }

        # Player
        self.playerWidth = 60
        self.playerHeight = 20
        self.playerSpeed = 7
        self.player = pygame.Rect(
            self.displaySize[0] // 2 - 30,
            self.displaySize[1] - 60,
            self.playerWidth,
            self.playerHeight
        )

        # Bullets
        self.bullets = []
        self.bulletSpeed = 8

        # Enemies
        self.enemies = []
        self.enemyWidth = 40
        self.enemyHeight = 20
        self.enemySpeed = 2
        self.spawnTimer = 0
        self.spawnDelay = 60  # frames

        # Game
        self.score = 0
        self.running = True
        self.gameFinished = False

    # ---------------------------------
    # Spawn inimigos
    # ---------------------------------
    def spawnEnemy(self):
        x = random.randint(0, self.displaySize[0] - self.enemyWidth)
        enemy = pygame.Rect(x, 0, self.enemyWidth, self.enemyHeight)
        self.enemies.append(enemy)

    # ---------------------------------
    # Movimento player
    # ---------------------------------
    def playerMotion(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.player.left > 0:
            self.player.x -= self.playerSpeed

        if keys[pygame.K_RIGHT] and self.player.right < self.displaySize[0]:
            self.player.x += self.playerSpeed

    # ---------------------------------
    # Atualização do jogo
    # ---------------------------------
    def update(self):

        self.playerMotion()

        # Spawn inimigos
        self.spawnTimer += 1
        if self.spawnTimer >= self.spawnDelay:
            self.spawnEnemy()
            self.spawnTimer = 0

        # Movimento balas
        for bullet in self.bullets[:]:
            bullet.y -= self.bulletSpeed
            if bullet.bottom < 0:
                self.bullets.remove(bullet)

        # Movimento inimigos
        for enemy in self.enemies[:]:
            enemy.y += self.enemySpeed

            # Game Over se encostar no player
            if enemy.colliderect(self.player):
                self.gameFinished = True

            if enemy.top > self.displaySize[1]:
                self.enemies.remove(enemy)

        # Colisão bala x inimigo
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.colliderect(enemy):
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    if enemy in self.enemies:
                        self.enemies.remove(enemy)
                    self.score += 1
                    break

    # ---------------------------------
    # Desenho
    # ---------------------------------
    def draw(self):

        self.screen.fill(self.colors["black"])

        # Player
        pygame.draw.rect(self.screen, self.colors["green"], self.player)

        # Balas
        for bullet in self.bullets:
            pygame.draw.rect(self.screen, self.colors["yellow"], bullet)

        # Inimigos
        for enemy in self.enemies:
            pygame.draw.rect(self.screen, self.colors["red"], enemy)

        # Score
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {self.score}", True, self.colors["white"])
        self.screen.blit(text, (10, 10))

        if self.gameFinished:
            self.drawGameOver()

    # ---------------------------------
    # Tela final
    # ---------------------------------
    def drawGameOver(self):
        font = pygame.font.Font(None, 60)
        text = font.render("GAME OVER", True, self.colors["red"])
        rect = text.get_rect(center=(self.displaySize[0] // 2, self.displaySize[1] // 2))
        self.screen.blit(text, rect)

    # ---------------------------------
    # Loop principal
    # ---------------------------------
    def run(self):

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return {"status": "QUIT", "score": self.score}

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        return {"status": "MENU", "score": self.score}

                    if event.key == pygame.K_SPACE and not self.gameFinished:
                        bullet = pygame.Rect(
                            self.player.centerx - 3,
                            self.player.top,
                            6,
                            12
                        )
                        self.bullets.append(bullet)

            if not self.gameFinished:
                self.update()

            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

        return {"status": "MENU", "score": self.score}