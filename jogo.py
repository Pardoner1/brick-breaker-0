import pygame

# inicializar
pygame.init()

displaySize = (800, 800)
mainDisplay = pygame.display.set_mode(displaySize)
pygame.display.set_caption("Brick Breaker Youtube")

ballSize = 15
ball = pygame.Rect(100, 500, ballSize, ballSize)
playerSize = 100
player = pygame.Rect(0, 750, playerSize, ballSize)
bricksPerRow = 8
Rows = 5
totalBricks = Rows * bricksPerRow

def makeBricks(bricksPerRow, Rows):
  displayHeight = displaySize[1]
  displayWidth = displaySize[0]
  brickHeight = 15
  bricksGaping = 5
  brickWidth = displayWidth/8-bricksGaping
  bricks = []
  for i in range(Rows):
    for j in range(bricksPerRow):
      brick = pygame.Rect(j*(brickWidth + bricksGaping), i*(brickHeight + bricksGaping), brickWidth, brickHeight)
      bricks.append(brick)
  
  return bricks

colors = {
  "white": (255, 255, 255),
  "green": (0, 255, 0),
  "blue": (0, 0, 255),
  "black": (0, 0, 0),
  "yellow": (255, 255, 0),
}

endGame = False
gameScore = 0
ballMotion = [1, 1]




# criar as funções do jogo

#desenhar as coisas na tela
def drawGameStart():
  mainDisplay.fill(colors["black"])
  pygame.draw.rect(mainDisplay, colors["blue"], player)
  pygame.draw.rect(mainDisplay, colors["white"], ball)

def drawBricks(bricks):
  for brick in bricks:
    pygame.draw.rect(mainDisplay, colors["green"], brick)

drawGameStart()
bricks = makeBricks(bricksPerRow, Rows)
drawBricks(bricks)

# criar um loop infinito
while not endGame:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      endGame = True
  pygame.time.wait(1)
  pygame.display.flip()

pygame.quit()