"""
File: lumber.py
Language: Python3
Authors : av2833@cs.rit.edu   Akash Venkatachalam
          rps7183@cs.rit.edu  Ruzan Sasuri
Description : A program to grow trees and harvest them in a sorted or unsorted manner.
"""
import turtle
from yard import LumberYard
import random

LY = LumberYard()

def doclick(x,y):
    """
    Based on user's click, this function calls to draw a tree or.
    calls to sort/unsort harvested tree logs.
    :param x: x position on co-ordinate axis chosen by the user.
    :param y: y position on co-ordinate axis chosen by the user.
    :pre: At the position the user clicked heading north.
    :post: At the position the user clicked heading north.
    :return: None
    """
    height = turtle.window_height()
    trunk = random.randint(50, 250)
    if y < (-height/4):
        if LY.allLogs() == []:
            print("No trees drawn yet.")
            return
        if x < 0:
            len = sorted(LY.allLogs(), reverse=True)
            drawlogs(len)
        else:
            len=LY.allLogs()
            drawlogs(len)
    elif (y + trunk) >= (height/2) - 50:
        print("Height Limit Exceeded")      # Height constraint.
        return
    else:
        turtle.goto(x,y)
        drawtree(trunk)


def drawtree(trunk_len):
    """
    A function to draw three different types of tree maple, pine and coconut at random.
    :param trunk_len: A randomly generated integer for tree's trunk length.
    :pre: At bottom of the tree trunk, Heading north.
    :post: At tree bottom, Heading north.
    :return: None
    """

    turtle.down()
    turtle.forward(trunk_len)
    turtle.right(90)
    rand=random.randint(1,3)

    if(rand==1):
        rand = "maple"
        turtle.circle(trunk_len / 4)       # draw maple tree

    elif(rand==2):
        rand = "pine"
        turtle.forward(trunk_len / 8)      # draw pine tree
        turtle.left(120)
        for i in range(2):
            turtle.forward(trunk_len / 4)
            turtle.left(120)
        turtle.forward(trunk_len / 8)

    elif(rand==3):
        rand = "coconut"
        for i in range(12):
            turtle.forward(trunk_len / 4)   # draw coconut tree
            turtle.back(trunk_len / 4)
            turtle.right(30)

    turtle.left(90)
    turtle.back(trunk_len)
    turtle.up()
    print("Grew a",rand,"tree of trunk height",trunk_len)
    LY.addLog(trunk_len)

def drawlogs(length):
    """
    A function to draw the harvested tree logs.
    :param length: A list for all the trees' trunk's length.
    :pre: Bottom center of the log, heading east.
    :post: Top center of the log, heading east.
    :return: None
    """
    totallen = 0
    logheight = 10
    turtle.clear()
    turtle.goto(0,0)
    turtle.right(90)
    for li in length:
        totallen += li
        turtle.back(li / 2)
        turtle.down()
        turtle.forward(li)
        turtle.left(90)
        turtle.forward(logheight)
        turtle.left(90)
        turtle.forward(li)
        turtle.left(90)
        turtle.forward(logheight)
        turtle.left(90)
        turtle.up()
        turtle.forward(li / 2)
        turtle.left(90)
        turtle.forward(logheight)
        turtle.right(90)
    print("The total length of the logs put together is:",totallen)
    turtle.exitonclick()


def drawline():
    """
    A function to draw a dividing line and the harvest buttons.
    :pre: Initial position at the origin, heading east.
    :post: Final position at the origin, heading north.
    :return: None
    """
    width = turtle.window_width()
    height = turtle.window_height()
    turtle.goto(width/2,-height/4)
    turtle.right(180)
    turtle.down()
    turtle.forward(width)
    turtle.left(90)
    turtle.up()
    turtle.forward(height/8)
    turtle.left(90)
    turtle.forward(width/8)
    turtle.write("Harvest and Sort", font=18)
    turtle.forward((3*width/8)+(width/8))
    turtle.write("Harvest Unsorted", font=18)
    turtle.goto(0,0)
    turtle.left(90)

def main():
    """
    The main function, it responds to user's click
    :return:None
    """
    turtle.speed(0)
    ##width = 700  # Graphics Window's Width
    ##height = 700  # Graphics Window's Height
    ##turtle.setup(width, height) # To set the width ad height of the screen if the user wants.
    turtle.up()
    drawline()
    turtle.onscreenclick(fun=doclick)
    turtle.mainloop()

if __name__ == '__main__':
    main()


