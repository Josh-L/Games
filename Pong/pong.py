import sys, pygame
pygame.init()

size = width, height = 1280, 768
paddle_speed = [0,0]
ball_speed   = [3,3]
ai_speed     = [0,0]
black =   0,   0,   0
white = 255, 255, 255
red   = 155,   0,   0
green =   0, 155,   0
blue  =   0,   0, 155

screen = pygame.display.set_mode(size)

paddle = pygame.draw.rect(screen, green, (width*0.05, height*0.5, 20, 200))
paddle.center = width*0.05, height*0.5

ai = pygame.draw.rect(screen, red, (width*0.95, height*0.5, 20, 200))
ai.center = width*0.95, height*0.5

ball = pygame.draw.rect(screen, white, (width*0.5, height*0.5, 10, 10))
ball.center = width*0.5, height*0.5

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key = pygame.key.get_pressed()

    if key[pygame.K_UP]:
        paddle_speed[1] = -3
    if key[pygame.K_DOWN]:
        paddle_speed[1] = 3
        
    if paddle.top <= 0:
        if paddle_speed[1] < 0:
                paddle_speed[1] = 0
    if paddle.bottom >= height:
        if paddle_speed[1] > 0:
                paddle_speed[1] = 0

    if ai.top <= 0:
        if ai_speed[1] < 0:
                ai_speed[1] = 0
    if ai.bottom >= height:
        if ai_speed[1] > 0:
                ai_speed[1] = 0

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] = -ball_speed[1]
    if ball.left <= 0 or ball.right >= width:
        ball_speed[0] = -ball_speed[0]

    if ball.colliderect(paddle):
        if ball.left < paddle.right:
            ball_speed[0] = -ball_speed[0]
            ball_speed[1] += paddle_speed[1]
        elif ball.bottom > paddle.top or ball.top < paddle.bottom:
            ball_speed[1] = -ball_speed[1]

    paddle = paddle.move(paddle_speed)
    ball = ball.move(ball_speed)
                
    screen.fill(black)
    paddle = pygame.draw.rect(screen, green, paddle)
    ai = pygame.draw.rect(screen, red, ai)
    ball = pygame.draw.rect(screen, white, ball)
    pygame.display.flip()
    paddle_speed = [0,0]
