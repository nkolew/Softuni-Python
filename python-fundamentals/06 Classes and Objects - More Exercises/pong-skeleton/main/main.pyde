from player import Player
from ball import Ball

player_one = None
player_two = None
ball_obj = None
game_is_on = True
message = ""

def restart_game():
    global player_one, ball_obj, player_two, game_is_on, message
    player_one = Player(width * random(1), height * 0.9)
    player_two = Player(width * random(1), height * 0.05)
    ball_obj = Ball()
    game_is_on = True
    message = ""

def setup():
    global player_one, ball_obj, player_two
    fullScreen()
    player_one = Player(width * random(1), height * 0.9)
    player_two = Player(width * random(1), height * 0.05)
    ball_obj = Ball()

def draw():
    background(0)
    global game_is_on, player_one, player_two, ball_obj, message
    player_one.show()
    if player_one.check_collision(ball_obj):
        ball_obj.velocity.y *= -1
    player_two.show()
    if player_two.check_collision(ball_obj):
        ball_obj.velocity.y *= -1
    ball_obj.show()
    if ball_obj.score_player_one:
        message = "Player 1 wins"
        game_is_on = False
    if ball_obj.score_player_two:
        message = "Player 2 wins"
        game_is_on = False
    if game_is_on == False:
        textSize(30)
        fill(255)
        text(message, width * 0.45, height * 0.5)
        text("Press space to replay", width * 0.425, height * 0.55)
        if keyPressed and key == " ":
            restart_game()
    # else:
        # ball_obj.update()
        # if keyPressed and keyCode == LEFT:
        #    player_one.move("left")
        # elif keyPressed and keyCode == RIGHT:
        #    player_one.move("right")
        # elif keyPressed and key == "a":
        #    player_two.move("left")
        # elif keyPressed and key == "d":
        #    player_two.move("right")
