"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    return GRAPH_MARGIN_SIZE + (width-GRAPH_MARGIN_SIZE*2)/len(YEARS)*year_index


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # create horizontal lines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # create vertical lines
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data. {'name':{'year':'rank','year1':'rank1','year2':'rank2'}}
        lookup_names (List[str]): A list of names whose data you want to plot. ['name1', 'name2', 'name3'......]

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # 1. Loop over lookup_names
    # 2. Get the year, rank from name_data of the name
    # 3. Create a list of x, a list of y
    # 4. Create text
    # 5. Create Line
    for i in range(len(lookup_names)):
        year_rank_d = name_data[lookup_names[i]]  # year_rank_d = {'year':'rank', 'year1':'rank1', 'year2':'rank2'.....}
        color = COLORS[i % len(COLORS)]
        x_lst = []
        y_lst = []
        for j in range(len(YEARS)):
            x_lst.append(get_x_coordinate(CANVAS_WIDTH, j))
            if str(YEARS[j]) in year_rank_d:
                rank = int(year_rank_d[str(YEARS[j])])
                y_lst.append(GRAPH_MARGIN_SIZE + ((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK) * rank)
                label = lookup_names[i] + ' ' + year_rank_d[str(YEARS[j])]
                canvas.create_text(x_lst[j]+TEXT_DX, y_lst[j], text=label, anchor=tkinter.SW, fill=color)
            else:
                # If out of rank give label '*'
                y_lst.append(GRAPH_MARGIN_SIZE + ((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK) * 1000)
                label = lookup_names[i] + '*'
                canvas.create_text(x_lst[j]+TEXT_DX, y_lst[j], text=label, anchor=tkinter.SW, fill=color)
            if j >= 1: # Create Line
                canvas.create_line(x_lst[j-1], y_lst[j-1], x_lst[j], y_lst[j], width=LINE_WIDTH, fill=color)



# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
