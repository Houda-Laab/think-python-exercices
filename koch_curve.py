from swampy import  TurtleWorld

def koch(t,length):
    if length<3:
        TurtleWorld.fd(t,length)
        return
    else: 
        koch(t,length/3)
        TurtleWorld.lt(t,60)
        koch(t,length/3)
        TurtleWorld.rt(t,120)
        koch(t,length/3)
        TurtleWorld.lt(t,60)
        koch(t,length/3)
def snowflake(t,length):
    for i in range(4):
        koch(t,length)
        TurtleWorld.rt(t,90)
    
world =  TurtleWorld.TurtleWorld()
bob =  TurtleWorld.Turtle()
bob.delay = 0.0001
snowflake(bob,400)

print(bob)
TurtleWorld.wait_for_user()
