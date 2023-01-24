import color_list
#Exercise 17.1 
class Time(object):
    """represents the time of day.
    attributes: hour, minute, second"""
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
class Point(object):
    """represents a point in 2-D space"""
#Exercise 17.2
    def __init__(self,x=0,y=0) :
        self.x = x
        self.y = y
#Exercise 17.3
    def __str__(self):
        return '(%d,%d)'%(self.x,self.y)
    def __add__(self,other):
        if isinstance(other,Point):
            return Point(self.x+other.x,self.y+other.y) 
        else:
            return Point(self.x+other[0],self.y+other[1]) 
 
#Exercise 17.6
class Kangaroo(object):
    def __init__(self,content=None):
        #if we just put [] in content and assign it to
        # the pouch_contents we will have a problem which is
        # every kangaroo object we creat 
        # will have the same list of pounch contents 
        if content == None:
            content = []
        self.pouch_contents = content
    def put_in_pouch(self,obj):
        self.pouch_contents.append(obj)
    def __str__(self):
        return 'the kangaroo has in its pouch ' +str(self.pouch_contents) 
from mayavi import mlab

#Exercise 17.7
#2
def cubes():
    t = range(0, 256, 51)
    mlab.figure(bgcolor=(0, 0, 0))
    for x in t:
        for y in t:
            for z in t:
                pos = x, y, z
                mlab.points3d(pos[0], pos[1], pos[2], scale_factor=10, color=(pos[0]/255, pos[1]/255, pos[2]/255))
    mlab.show()
#the result is amazing 

#1
def colors():
    mlab.figure(bgcolor=(0, 0, 0))
    dic,rgb = color_list.read_colors()
    for code,names in rgb:
        code = code.strip('#')
        x,y,z = int(code[0:2],base = 16),int(code[2:4],base = 16),int(code[4:],base = 16)
        mlab.points3d(x, y, z, scale_factor=10, color=(x/255, y/255,z/255))
    mlab.show()
    

