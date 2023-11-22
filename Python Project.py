import turtle
import random

wn = turtle.Screen()
wn.title("Turtle Race Game with Obstacles")
wn.bgcolor("lightgray")
wn.setup(width=800, height=600)

player1 = turtle.Turtle()
player1.shape("turtle")
player1.color("red")
player1.penup()
player1.goto(-300, 0)

player2 = turtle.Turtle()
player2.shape("turtle")
player2.color("blue")
player2.penup()
player2.goto(-300, -50)

obstacles = []
for _ in range(5):
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("black")
    obstacle.shapesize(stretch_wid=1, stretch_len=2)
    obstacle.penup()
    obstacle.speed(0)
    obstacle.goto(random.randint(-200, 200), random.randint(-200, 200))
    obstacles.append(obstacle)

finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(350, 250)
finish_line.pendown()
finish_line.goto(350, -250)
finish_line.hideturtle()

score_player1 = 0
score_player2 = 0
rounds = 3

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("black")
score_display.goto(0, 260)
score_display.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 16, "normal"))

wn.listen()

def move_player_up(player):
    y = player.ycor()
    y += 20
    player.sety(y)

def move_player_down(player):
    y = player.ycor()
    y -= 20
    player.sety(y)

def move_player_forward(player):
    x = player.xcor()
    x += 20
    player.setx(x)

def move_player_back(player):
    x = player.xcor()
    x -= 20
    player.setx(x)

wn.onkeypress(lambda: move_player_up(player1), "w")
wn.onkeypress(lambda: move_player_down(player1), "s")
wn.onkeypress(lambda: move_player_forward(player1), "d")
wn.onkeypress(lambda: move_player_back(player1), "a")

wn.onkeypress(lambda: move_player_up(player2), "Up")
wn.onkeypress(lambda: move_player_down(player2), "Down")
wn.onkeypress(lambda: move_player_forward(player2), "Right")
wn.onkeypress(lambda: move_player_back(player2), "Left")

for round_num in range(1, rounds + 1):
    while True:
        wn.update()

        for obstacle in obstacles:
            obstacle.setx(obstacle.xcor() + random.randint(-5, 5))
            obstacle.sety(obstacle.ycor() + random.randint(-5, 5))

            if player1.distance(obstacle) < 20 or player2.distance(obstacle) < 20:

                player1.goto(-300, 0)
                player2.goto(-300, -50)

                break

        if player1.xcor() > 340 or player2.xcor() > 340:
            if player1.xcor() > player2.xcor():
                score_player1 += 1
            else:
                score_player2 += 1

            score_display.clear()
            score_display.write(f"Player 1: {score_player1}  Player 2: {score_player2}", align="center",
                                font=("Courier", 16, "normal"))

            player1.goto(-300, 0)
            player2.goto(-300, -50)

            for obstacle in obstacles:
                obstacle.goto(random.randint(-200, 200), random.randint(-200, 200))

            break

overall_winner = "Player 1" if score_player1 > score_player2 else "Player 2"

score_display.goto(0, 0)
score_display.write(f"{overall_winner} wins the game!", align="center", font=("Courier", 20, "normal"))

wn.exitonclick()
