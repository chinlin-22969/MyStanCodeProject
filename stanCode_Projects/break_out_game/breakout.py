"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    while True:
        # SCORE: Update the score on the label
        graphics.score_label.text = 'Score: '+str(graphics.counter)

        # BALL ANIMATION
        pause(FRAME_RATE)
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        # LIMIT1: If hit the window, set dx & dy
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
            graphics.set_dx()
        if graphics.ball.y <= 0:
            graphics.set_dy()
        # LIMIT2: If hit the bricks, ball rebound and randomly make cubes
        graphics.ball_hit_brick()

        # CUBES:
        # 1.Cube animation
        # 2.if cube.y > window.y remove the cube from cube lists
        if graphics.cubes != 0:
            for cube in graphics.cubes:
                cube.move(0, 3)
                if cube.y-cube.height > graphics.window.height:
                    graphics.window.remove(cube)
                    graphics.cubes.remove(cube)
                    graphics.ball_ignore_lst.remove(cube)

                # if cube detect paddle delete from cube lists and call method(expand/shorten paddle)
                # 1. cube1_lst --> paddle expand
                elif cube in graphics.cube1_lst:
                    if graphics.window.get_object_at(cube.x, cube.y) is not None:
                        obj = graphics.window.get_object_at(cube.x-2, cube.y-2)
                        if obj is graphics.paddle:
                            graphics.paddle_expand()
                            graphics.window.remove(cube)
                            graphics.cubes.remove(cube)
                            graphics.ball_ignore_lst.remove(cube)
                # 2. cube2_lst --> paddle shorten
                elif cube in graphics.cube2_lst:
                    if graphics.window.get_object_at(cube.x, cube.y) is not None:
                        obj = graphics.window.get_object_at(cube.x-2, cube.y-2)
                        if obj is graphics.paddle:
                            graphics.paddle_shorten()
                            graphics.window.remove(cube)
                            graphics.cubes.remove(cube)
                            graphics.ball_ignore_lst.remove(cube)

        # RESET: reset ball, when the paddle doesn't catch the ball
        if graphics.ball.y >= graphics.window.height - graphics.ball.height:
            lives -= 1
            graphics.reset_ball()
        # END: Game ends when no lives left or no bricks left
        if lives <= 0:
            graphics.game_over()
            break
        if graphics.b_c * graphics.b_r == graphics.counter:
            graphics.win_game()
            break


if __name__ == '__main__':
    main()
