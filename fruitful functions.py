import math
def compare(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1
def hypotenuse(a,b):
    """returns the Hypotenuse of a right triangle

    Args:
        a (float): length of the first leg of the triangle
        b (float): length of the second leg of the triangle
    """
    c2 = a**2 + b**2
    c = math.sqrt(c2)
    return c
def is_between(x, y, z):
    return (x<=y)and(z>=y)
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    sum = x + y + z
    pow = b(sum)**2
    return pow
def ack(m,n):
    if m==0:
        return n+1
    elif (m>0):
        if (n==0):
            return ack((m-1),1)
        elif n > 0:
            return ack((m-1),ack(m,(n-1)))
        else:
            return
    else:
        return
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def is_palindrome(word):
    if len(word)==2 or len(word)==3:
        return first(word) == last(word)
    else:
        if first(word) == last(word):
            return is_palindrome(middle(word))
        else:
            return first(word) == last(word)
def  is_power(a,b):
    if a==1:
        return True
    if b == 1:
        return a == 1
    if a%b == 0:
        return is_power(a/b,b)
    else:
        return False       
def  gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)  
def square_root(a):
    if a>1:
        x = a-1
    else:
        x = 1
    while True:
        y = (x + a/x) / 2
        if abs(y-math.sqrt(a))< 0.1:
            break
    return y
def test_square_root():
    for i in range(9):
        a = square_root(i)
        b = math.sqrt(i)
        print (str(i)+" "*15+ str(a)+ " "*15+str(b)+" "*15+str(abs(a-b))+"\n")
def eval_loop():
    while True:
        inp = input('>>')
        if inp == 'done':
            break
        print(eval(inp))
def back_word(word):
    index = 1
    while index<len(word):
        print(word[-index])  
        index = index + 1  
    print(word[0])   
    
def rotate_word(word,code):
    nword = word.strip()
    result = " "
    for c in nword:
        a = ord(c)+code
        result = result+chr(a)
    return result.strip()
print(rotate_word('cheer',7))

