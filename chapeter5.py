"""functions to solve the exercices in chapeter 5 Conditionals and recursion of the book"""
from swampy import  TurtleWorld

#Exercise 5.1
#1
def check_fermat(a,b,c,n):
    if n>2:
        if ((a**2)+(b**2))==c**2:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No,that didn't work.")
#2
def prompt():
    a = input("enter value of a :\n")
    b = input("enter value of b :\n")
    c = input("enter value of c :\n")
    n = input("enter value of n :\n")
    check_fermat(int(a),int(b),int(c),int(n))
    
#Exercise 5.2
#1
def is_triangle(a,b,c):
    if (a+b<c)or(a+c<b)or(b+c<a):
        print("NO!!")
    else:
        print("Yes!")
#2
def triangle():
    a = int(input("enter first value:\n"))
    b = int(input("enter second value:\n"))
    c = int(input("enter last value:\n")) 
    is_triangle(int(a),int(b),int(c))

#Exercise 5.3
#1
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
        
#2
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
