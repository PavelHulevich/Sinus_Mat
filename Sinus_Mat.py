import time
from tkinter import Canvas, Tk, PhotoImage, CENTER
from random import randint
from math import sin, pi

monitor_delay = 17
size = 900  # size of canvas
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()
qnt_balls = 9  # number of balls along each axis
balls_coord = [[x for x in range(0, 10)] for _ in range(0, 10)]  # array of ball properties [X coord, Y old_coord,
                                                            # Contains references to objects of canvas.create_image]
sin_list = [int(sin(i * pi / 180) * 55) for i in range(0, 361)]  # table of sinus
img_ball = [PhotoImage(file='green.png'), PhotoImage(file='red.png'), PhotoImage(file='silver.png'),
            PhotoImage(file='azure.png'), PhotoImage(file='blue.png'), PhotoImage(file='cyan.png'),
            PhotoImage(file='emerald.png'), PhotoImage(file='gold.png'), PhotoImage(file='pink.png'),
            PhotoImage(file='purple.png'), PhotoImage(file='scarlet.png'), PhotoImage(file='steel.png'),
            PhotoImage(file='bronze.png'), PhotoImage(file='yellow.png')]


def move_balls(grad: int):  # Move every ball
    for y in range(qnt_balls):  # Rows of balls
        for x in range(qnt_balls):  # Columns of balls
            balls_angel_new = grad + x * 15 + y * 15  # x * 15 - Each column of balls is at a diff. height (diff. angle)
                                                      # y * 15 - Delay rows of ball. Vertical tilt.
            if balls_angel_new > 360:
                balls_angel_new -= 360
            balls_angel_new = sin_list[balls_angel_new]  # Sinus
            balls_y_new = (650 - y * 60) + balls_angel_new  # New Y-coord each ball
            canvas.move(balls_coord[y][x][2], 0, (balls_y_new - balls_coord[y][x][1]))  # Move current ball
            balls_coord[y][x][1] = balls_y_new  # Old Y-coord <== New Y-coord


def draw_balls():  # Fill start balls array and draw them
    for y in range(qnt_balls):
        for x in range(qnt_balls):
            color_index = randint(0, 13)  # index for list of ball color
            balls_coord[y][x] = [70 * (x + 1) + y * 20, 650 - y * 60, 0]  # [x, old_y, new_y]
            balls_coord[y][x][2] = canvas.create_image(balls_coord[y][x][0],
                                                       balls_coord[y][x][1],
                                                       image=img_ball[color_index], anchor=CENTER)


start = time.time()
draw_balls()
# Main cycle
for _ in range(5):
    for j in range(360):
        move_balls(j)
        root.update()

end = time.time()
print(end - start)

