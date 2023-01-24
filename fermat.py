"""just checking fermat's law :)"""
def check_fermat(a,b,c,n):
    if n>2:
        if ((a**n)+(b**n)==(c**n)):
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn’t work")
def prompt():
    a = int(input("enter value of A:\n"))
    b = int(input("enter value of B:\n"))
    c = int(input("enter value of C:\n"))
    n = int(input("enter value of n:\n"))
    check_fermat(a,b,c,n)

prompt()