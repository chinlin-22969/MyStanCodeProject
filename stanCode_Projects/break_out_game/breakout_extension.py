"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_ex2 import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    while True:
        pause(FRAME_RATE)
        graphics.score_label.text = 'Score: '+str(graphics.counter)
        # Cube animation
        # ball ignore lst
        # if cube.y > window.y remove the cube from cube lists
        if graphics.cubes != 0:
            for cube in graphics.cubes:
                cube.move(0, 3)
                if cube.y-cube.height > graphics.window.height:
                    graphics.window.remove(cube)
                    graphics.cubes.remove(cube)
                    graphics.ball_ignore_lst.remove(cube)

                ################################################
                # if cube detect paddle delete from cube lists and call method(expand/shorten paddle,......)

                # cube1_lst --> paddle expand
                elif cube in graphics.cube1_lst:
                    if graphics.window.get_object_at(cube.x, cube.y) is not None:
                        obj = graphics.window.get_object_at(cube.x-2, cube.y-2)
                        if obj is graphics.paddle:
                            graphics.paddle_expand()
                            graphics.window.remove(cube)
                            graphics.cubes.remove(cube)
                            graphics.ball_ignore_lst.remove(cube)
                # cube2_lst --> paddle shorten
                elif cube in graphics.cube2_lst:
                    if graphics.window.get_object_at(cube.x, cube.y) is not None:
                        obj = graphics.window.get_object_at(cube.x-2, cube.y-2)
                        if obj is graphics.paddle:
                            graphics.paddle_shorten()
                            graphics.window.remove(cube)
                            graphics.cubes.remove(cube)
                            graphics.ball_ignore_lst.remove(cube)
                ################################################

        # the game ends when no lives left or no bricks left
        if lives <= 0 or graphics.b_c*graphics.b_r == graphics.counter:
            break
        # when the paddle doesnt catch the ball, minus one life
        if graphics.ball.y >= graphics.window.height - graphics.ball.height:
            lives -= 1
            graphics.reset_ball()
        # ball animation
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
            graphics.set_dx()
        if graphics.ball.y <= 0:
            graphics.set_dy()
        graphics.detect_ball()

    graphics.game_over()


if __name__ == '__main__':
    main()
