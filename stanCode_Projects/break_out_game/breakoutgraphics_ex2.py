"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# CONSTANT
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 3      # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)


        # Create a paddle
        self.paddle_width = PADDLE_WIDTH
        self.paddle_height = PADDLE_HEIGHT
        self.paddle = GRect(self.paddle_width, self.paddle_height)
        self.paddle.filled = 'True'
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset-paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = 'True'
        self.window.add(self.ball, x=(window_width-ball_radius*2)/2, y=(window_height-ball_radius*2)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Draw bricks
        self.draw_brick()
        self.b_r = BRICK_ROWS
        self.b_c = BRICK_COLS
        self.counter = 0  # how many times the ball hits the brick
        self.switch = False

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.set_ball_velocity)

        # Cubes
        self.cube1_lst = []  # if paddle detect obj in the list, paddle will expand
        self.cube2_lst = []  # if paddle detect obj in the list, paddle will shorten
        self.cubes = []  # to hold the cubes that been created and still in the window

        # score label
        self.score_label = GLabel('Score: '+str(self.counter))
        self.window.add(self.score_label, x=BRICK_WIDTH/2, y=BRICK_OFFSET/2)

        # To put the obj you want ball to ignore
        self.ball_ignore_lst = []
        self.ball_ignore_lst.append(self.score_label)

    def game_over(self):
        game_over = GLabel('GAME OVER')
        game_over.font = '-70'
        self.window.add(game_over, x=(self.window.width-game_over.width)/2, y=(self.window.height-game_over.height)*3/4)
        return game_over

    def reset_ball(self):
        self.window.add(self.ball, x=(self.window.width - self.ball.width)/2,
                        y=(self.window.height - self.ball.width)/2)
        self.switch = False
        self.__dx = 0
        self.__dy = 0

    def set_ball_velocity(self, _):
        if not self.switch:
            self.switch = True
            if self.switch:
                self.__dx = random.randint(1, MAX_X_SPEED)
                self.__dy = INITIAL_Y_SPEED
                if random.random() > 0.5:
                    self.__dx = -self.__dx

    # In case when ball hit the brick/ paddle/ window
    def get_dx(self):
        return self.__dx

    def set_dx(self):
        self.__dx = -self.__dx

    def get_dy(self):
        return self.__dy

    def set_dy(self):
        self.__dy = -self.__dy

    def paddle_move(self, mouse):
        if self.paddle.width/2 <= mouse.x <= self.window.width-self.paddle.width/2:
            self.paddle.x = mouse.x-self.paddle.width/2
        elif mouse.x <= self.paddle.width/2:
            self.paddle.x = 0
        else:
            self.paddle.x = self.window.width-self.paddle.width

    # Draw bricks
    def draw_brick(self):
        color_lst = ['red', 'orange', 'yellow', 'green', 'lightblue', 'purple']
        counter = 0
        for i in range(BRICK_ROWS):
            if i != 0 and i % 2 == 0:
                counter += 1
            for j in range(BRICK_COLS):
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.window.add(brick, x=(BRICK_SPACING+BRICK_WIDTH)*j,
                                y=BRICK_OFFSET+(BRICK_SPACING+BRICK_HEIGHT)*i)
                brick.filled = 'True'
                brick.fill_color = str(color_lst[counter % len(color_lst)])
                brick.color = str(color_lst[counter % len(color_lst)])

    # Make cubes and methods when the paddle catch the cubes(paddle expand and shorten)
    def make_cubes(self):
        n = random.randint(1, 3)
        # paddle expand
        cube1 = GRect(20, 20)
        cube1.filled = 'True'
        cube1.color = 'black'
        cube1.fill_color = 'magenta'
        # paddle shortened
        cube2 = GRect(20, 20)
        cube2.filled = 'True'
        cube2.color = 'black'
        cube2.fill_color = 'Aquamarine'
        if n == 1:
            self.cube1_lst.append(cube1)
            return cube1
        else:
            self.cube2_lst.append(cube2)
            return cube2

    def paddle_expand(self):
        if self.paddle.width <= 160:
            x, y = self.paddle.x, self.paddle.y
            self.window.remove(self.paddle)
            self.paddle_width += 20
            self.paddle = GRect(width=self.paddle_width, height=self.paddle_height)
            self.paddle.filled = True
            self.paddle.fill_color = 'magenta'
            self.window.add(self.paddle, x, y)
            return self.paddle

    def paddle_shorten(self):
        if self.paddle.width >= 40:
            x, y = self.paddle.x, self.paddle.y
            self.window.remove(self.paddle)
            self.paddle_width -= 20
            self.paddle = GRect(width=self.paddle_width, height=self.paddle_height)
            self.paddle.filled = True
            self.paddle.fill_color = 'Aquamarine'
            self.window.add(self.paddle, x, y)
            return self.paddle

    def detect_ball(self):
        # If the left_top of the ball collides, ball rebound and make cubes
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
            obj = self.window.get_object_at(self.ball.x, self.ball.y)
            if obj not in self.ball_ignore_lst:
                if obj is self.paddle:
                    if self.__dy > 0:
                        self.set_dy()
                else:
                    # When ball hit the obj(brick), dy will change and the obj(brick) will be removed
                    self.set_dy()
                    self.window.remove(obj)
                    # To calculate how much brick is hit by the ball
                    self.counter += 1
                    # Create cubes on the window and add it into cubes(list) and ball_ignore_lst
                    cube = self.make_cubes()
                    self.window.add(cube, obj.x+(obj.width-5)/2, obj.y+(obj.width-5)/2)
                    self.cubes.append(cube)
                    self.ball_ignore_lst.append(cube)

        # If the right_top of the ball collides, ball rebound (Don't make cubes)
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y) is not None:
            obj = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
            if obj not in self.ball_ignore_lst:
                if obj is self.paddle:
                    if self.__dy > 0:
                        self.set_dy()
                else:
                    self.set_dy()
                    self.window.remove(obj)
                    self.counter += 1

        # If the left_bottom of the ball collides, ball rebound and make cubes
        elif self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height) is not None:
            obj = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
            if obj not in self.ball_ignore_lst:
                if obj is self.paddle:
                    if self.__dy > 0:
                        self.set_dy()
                else:
                    self.set_dy()
                    self.window.remove(obj)
                    self.counter += 1
                    cube = self.make_cubes()
                    self.window.add(cube, obj.x+(obj.width-5)/2, obj.y+(obj.width-5)/2)
                    self.cubes.append(cube)
                    self.ball_ignore_lst.append(cube)

        # If the right_bottom of the ball collides, ball rebound  (Don't make cubes)
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height) is not None:
            obj = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
            if obj not in self.ball_ignore_lst:
                if obj is self.paddle:
                    if self.__dy > 0:
                        self.set_dy()
                else:
                    self.set_dy()
                    self.window.remove(obj)
                    self.counter += 1
