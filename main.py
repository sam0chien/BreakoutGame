from time import sleep
from turtle import Screen

from ball import Ball
from brick import Brick
from over import Over
from paddle import Paddle


# Pause
def pause():
    global is_pause
    is_pause = not is_pause


# Screen
screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Breakout🧱')
screen.tracer(0)
# Paddle
paddle = Paddle()
# Ball
ball = Ball()
# Brick Layout
x_layout = list(range(-330, 330, 50))
y_layout = list(range(240, 0, -20))
bricks = []  # For determining if game over
for x in x_layout:
    for y in y_layout:
        brick = Brick(x, y)
        bricks.append(brick)
screen.listen()
screen.onkey(pause, 'space')  # Space key for start game and pause

game_is_up = True
is_pause = True
while game_is_up:
    screen.update()
    if not is_pause:
        screen.onkey(paddle.go_left, 'Left')
        screen.onkey(paddle.go_right, 'Right')
        sleep(ball.move_speed)
        ball.move()
        # Detect collision with wall
        if ball.xcor() > 380 or ball.xcor() < -385:
            ball.bounce_x()
        if ball.ycor() > 290:
            ball.bounce_y()
        # Detect collision with paddle
        if ball.distance(paddle) < 50 and -260 < ball.ycor() < -240:
            ball.bounce_y()
        # Detect paddle misses
        if ball.ycor() < -300:
            ball.reset_position()
            paddle.reset_position()
            is_pause = True
        # Detect collision with brick
        for brick in bricks:
            if ball.distance(brick) < 50 and ball.ycor() >= brick.ycor() - 20:
                if ball.xcor() > brick.xcor() + 20 or ball.xcor() < brick.xcor() - 20:
                    brick.get_hit()
                    ball.bounce_x()
                else:
                    brick.get_hit()
                    ball.bounce_y()
                bricks.remove(brick)
                ball.move_speed *= 0.9  # Increase ball speed per brick hit
                break
        if len(bricks) < 1:  # No more brick
            game_is_up = False
    else:  # Pause
        screen.onkey(None, 'Left')
        screen.onkey(None, 'Right')

while not game_is_up:
    screen.update()
    sleep(ball.move_speed)
    ball.move()  # Ball still move
    Over('GAME OVER')  # Show text
    paddle.goto(1000, 1000)
    # Detect collision with wall
    if ball.xcor() > 380 or ball.xcor() < -385:
        ball.bounce_x()
        ball.move_speed *= 0.9
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce_y()
        ball.move_speed *= 0.9

screen.mainloop()
