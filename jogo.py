import pygame

# inicializar
pygame.init()

displaySize = (800, 800)
mainDisplay = pygame.display.set_mode(displaySize)
pygame.display.set_caption("Brick Breaker Youtube")

colors = {
  "white": (255, 255, 255),
  "green": (0, 255, 0),
  "blue": (0, 0, 255),
  "black": (0, 0, 0),
  "yellow": (255, 255, 0),
  "red": (255, 0, 0)
}

endGame = False
gameScore = 0
gameTimeFrame = 1
playerSpeed = 5
ballSpeed = 1
maxSpeed = 10
speedLevel = 0
ballSize = 15
ballMove = [ballSpeed, -ballSpeed]
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

# criar as funções do jogo

def playerMotion(event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        if player.x > 0:
          player.x -= playerSpeed
      if event.key == pygame.K_RIGHT:
        if player.x < displaySize[0] - playerSize:
          player.x += playerSpeed

def ballMotion(ball):
  move = ballMove
  ball.x += move[0]
  ball.y += move[1]
  if ball.x < 0 or ball.x > displaySize[0] - ballSize:
    move[0] *= -1
  if ball.y < 0:
    move[1] *= -1
  if ball.y > displaySize[1] - ballSize:
    move = None
  if ball.colliderect(player):
    move[1] *= -1
  for brick in bricks:
    if ball.colliderect(brick):
        move[1] *= -1
        bricks.remove(brick)
        global gameScore, speedLevel
        gameScore += 1
        
        if gameScore % 2 == 0 and speedLevel < maxSpeed:
            speedLevel += 1
            
            if move[0] > 0:
                move[0] += 1
            else:
                move[0] -= 1

            if move[1] > 0:
                move[1] += 1
            else:
                move[1] -= 1
    
  return move

#desenhar as coisas na tela
def drawGameStart():
  mainDisplay.fill(colors["black"])
  pygame.draw.rect(mainDisplay, colors["blue"], player)
  pygame.draw.rect(mainDisplay, colors["white"], ball)

def drawBricks(bricks):
  for brick in bricks:
    pygame.draw.rect(mainDisplay, colors["green"], brick)

def gameScoreUpdate(gameScore):
  gameFont = pygame.font.Font("freesansbold.ttf", 20)
  text = gameFont.render("Score: " + str(gameScore), 1, colors["yellow"])
  mainDisplay.blit(text, (0, 780))
  if gameScore == totalBricks:
    return True
  else:
    return False

def gameFinish(gameWon):
  strText = "You Win" if gameWon else "Game Over"
  colorType = "green" if gameWon else "red"

  global ballMove
  ballMove = [0, 0]

  gameFont = pygame.font.Font("freesansbold.ttf", 40)
  text = gameFont.render(strText, True, colors[colorType])

  # Centralizar o texto corretamente
  textRect = text.get_rect(center=(displaySize[0] // 2, displaySize[1] // 2))
  mainDisplay.blit(text, textRect)


bricks = makeBricks(bricksPerRow, Rows)

# criar um loop infinito
while not endGame:
  drawGameStart()
  drawBricks(bricks)
  if gameScoreUpdate(gameScore):
    gameFinish(True)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      endGame = True
  playerMotion(event)
    
  ballMove = ballMotion(ball)
  if ballMove == None:
    gameFinish(False)



  pygame.time.wait(gameTimeFrame)
  pygame.display.flip()

pygame.quit()