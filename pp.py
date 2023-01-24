import tkinter
import swampy
print('hello')
def right_justify(s):
    print(" "*(70-(len(s)))+s)
right_justify('allen')
def do_twice(f,a):
    f(a)
    f(a)
do_twice(right_justify,"allen")
def carre():
    print('+'+' -'*4,'+'+' -'*4,'+')
    print('|'+' '*8,'|'+' '*4,' '*3+' |')
    print('|'+' '*8,'|'+' '*4,' '*3+' |')
    print('|'+' '*8,'|'+' '*4,' '*3+' |')
    print('|'+' '*8,'|'+' '*4,' '*3+' |')
    print('+'+' -'*4,'+'+' -'*4,'+')
    print('|'+' '*8,'|'+' '*4,' '*3+' |')
    print('|'+' '*8,'|'+' '*4,' '*3+' |')
    print('|'+' '*8,'|'+' '*4,' '*3+' |')
    print('|'+' '*8,'|'+' '*4,' '*3+' |')
    print('+'+' -'*4,'+'+' -'*4,'+')
carre()
from swampy import  TurtleWorld
import math
def square(t,length):
    for i in range(4):
        TurtleWorld.fd(t, length)
        TurtleWorld.lt(t)
    print(t)
def polygon(t,length,n):
    """a function that makes the Turtule draw a polygon

    Args:
        t (Turtle): the turtule object
        length (float): the length of each segment
        n (integer): number of segments
    """
    for i in range(n):
        TurtleWorld.fd(t, length)
        TurtleWorld.lt(t, 360/n)
    print(t)
def circle(t,radius):
    """the turtule will draw a circle

    Args:
        t (Turtle):turtle instance
        radius (integer): the radius of the circle in degrees
    """
    c = 2*math.pi*radius
    n = 300
    polygon(t,c/n,n)
def arc(t,radius,angle):
    """function that makes the Turtule draw an arc

    Args:
        t (Turtle): turtle instance
        radius (integer):the radius of the arc in degrees
        angle (integer): the angle in which we have to stop in degrees
    """
    c = 2*math.pi*radius
    n = 300
    for i in range(n):
        TurtleWorld.fd(t, c/n)
        TurtleWorld.lt(t, angle/n)
def flower(t,n,r):
    for i in range(n*2):
        m = math.sqrt((r**2)/2)
        TurtleWorld.lt(t,math.atan(r/m))
        
world =  TurtleWorld.TurtleWorld()
bob =  TurtleWorld.Turtle()
bob.delay = 0.0001 
