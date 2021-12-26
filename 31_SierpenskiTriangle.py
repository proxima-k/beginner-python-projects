# https://github.com/jorgegonzalez/beginner-projects#sierpinski-triangle

import turtle

def draw_traingle(pos_list,turtle):
    turtle.up()
    turtle.goto(pos_list[0])
    turtle.down()
    turtle.goto(pos_list[1])
    turtle.goto(pos_list[2])
    turtle.goto(pos_list[0])

def get_midpoint(pos_a,pos_b):
    x = (pos_a[0] + pos_b[0]) / 2
    y = (pos_a[1] + pos_b[1]) / 2
    midpoint = (x,y)
    return midpoint

def sierpenski_triangle(pos_list, turtle, depth):

    draw_traingle(pos_list, turtle)

    if depth > 0:
        sierpenski_triangle([pos_list[0], get_midpoint(pos_list[0],pos_list[1]),
                             get_midpoint(pos_list[0],pos_list[2])],
                            turtle,depth - 1)
        sierpenski_triangle([pos_list[1], get_midpoint(pos_list[1],pos_list[0]),
                             get_midpoint(pos_list[1],pos_list[2])],
                            turtle,depth - 1)
        sierpenski_triangle([pos_list[2], get_midpoint(pos_list[2],pos_list[1]),
                             get_midpoint(pos_list[2],pos_list[0])],
                            turtle,depth - 1)

dave = turtle.Turtle()
window = turtle.Screen()
position_list = [(-250, -150), (0, 300), (250, -150)]

sierpenski_triangle(position_list, dave, 5)

window.exitonclick()