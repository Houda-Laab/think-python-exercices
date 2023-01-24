fin = open(r"C:\Users\Admin\AppData\Local\Programs\Python\Python311\swampy\words.txt")
print(fin)
def has_no_e(word):
    return word.count('e') == 0
def avoids(word,forbiden_letters):
    for c in forbiden_letters:
        if word.count(c) != 0:
            return False
    return True
def uses_all(word,letters):
    for c in word:
        if letters.count(c) == 0:
            return False
    for c in letters:
        if word.count(c) == 0:
            return False
    return True
def uses_only(word,letters):
    err = False
    for j in word:
        for c in letters:
            if c == j:
                err = True
        if err == False:
            return False
        err = False
    return True
def is_abecedarian(word):
    for c in range(len(word)-2):
        if ord(word[c])>ord(word[c+1]):
            return False
    return True
def is_three_c_couble_let(word):
    correct = 0
    nb = 0
    for c in range(0,len(word)-1,2):
        if word[c] == word[c+1]:
            nb = nb + 1
            correct = 1
            if nb == 3:
                return True
        else:
            nb = 0
            correct = 0
    return False
def is_palindrome(word):
    if len(word)==2 or len(word)==3:
        return word[0] == word[-1]
    else:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False 
def is_reversible(n1,n2):
    num1 = str(n1)
    num2 = str(n2)
    if num1[0] == num2[-1]:
        if num1[-1] == num2[0]:
            return True
    return False
count = 0
p = 0
#Exercise 9.8
for i in range(100000,999999):
    num = str(i)
    if is_palindrome(num[2:]):
        dig = i + 1
        num = str(dig)
        if is_palindrome(num[1:]):
            dig = dig + 1
            num = str(dig)
            if is_palindrome(num[1:-2]):
                dig = dig + 1
                num = str(dig)
                if is_palindrome(num):
                    print(i)
# the number we're looking for is 199999/200000/2000001/2000002
#Exercise 9.9
for i in range(10,90):
    for j in range(20,99):
        if is_reversible(i,j) :
            if count == 0:
                prevj = j
                previ = i 
                diff = j - i
                count = count+1
                print(i,j)
                print("\n")
            else :
                if j - i== diff :
                    prevj = j
                    previ = i
                    count = count + 1
                    print(i, j)
print(count)
# the man's age is 67 and his mom is 76 :)
