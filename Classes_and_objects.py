import math
from swampy.World import World
#Exercice 15.1
class Point(object):
    """represents a point in 2-D space"""
class Rectangle(object):
    """the parameters of a rectangle
    bbox is a list of the upper-corner and the lower corner
    color is the color to fill the rectangle"""
class Circle(object):
    """the parameters of the circle are the radius
    and a point object where to start drawing
    """
def distance(p1,p2):
    return math.sqrt((p2.x-p1.x)+(p2.y-p1.y))
world = World()
#
#1
def draw_rectangle(canvas,rectangle):
    return canvas.rectangle(rectangle.bbox,outline = 'black',width = 1,fill = rectangle.color)
#3
def draw_point(canvas,point):
    return canvas.circle([point.x,point.y], 1, outline=None, fill='black')
#4
def draw_circle(canvas,circle):
    return canvas.circle([circle.point.x,circle.point.y], circle.radius, None, circle.color)
#5
def draw_flag():
    canvas = world.ca(width=500, height=500, background='grey')
    bbox = [[-150,-100], [150, 100]]
    red_rectangle = Rectangle()
    red_rectangle.bbox = [[0,0], [250,100]]
    red_rectangle.color = 'red'
    white_rectangle = Rectangle()
    white_rectangle.bbox = [[0,-100],[250,0]]
    white_rectangle.color = 'white'
    points = [[0,100], [0, -100], [100,0]]
    draw_rectangle(canvas,white_rectangle)
    draw_rectangle(canvas,red_rectangle)
    canvas.polygon(points, fill='blue')
    world.mainloop()
