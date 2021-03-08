class Ball:
    def __init__(self):
        self.position = PVector(width * 0.5, height * 0.5)
        self.w = 20
        self.velocity = PVector(5, 5)
        self.score_player_one = False
        self.score_player_two = False
    def show(self):
        fill(255)
        ellipse(self.position.x, self.position.y, self.w, self.w)
    # TODO: Create a move() method that adds the velocity to the position
        # Help: https://processing.org/reference/PVector_add_.html
    # TODO: Create a border() method that checks for collision using the current possition
        # Help: check if the x or y of the possition are outside the screen borders
    # TODO: Create an update() method that simply calls the 2 methods you just created
        
        
