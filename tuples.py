import random
fin = open(r"C:\Users\Admin\AppData\Local\Programs\Python\Python311\swampy\words.txt")
def sumall(*args):
    summ = 0
    for a in args:
        summ = summ + a
    return summ
def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word),random.random()))
    t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res
def most_frequent(s):
    d = dict()
    for c in s:
        d[c] =d.get(c,0)+d.get(c, 1)
    t = d.items()
    print(t)
#exercice 12.4
def anagrams(fin):
    d = dict()
    for c in fin:
        l = c.strip('\n')
        t = tuple(sorted(tuple(l)))
        if t not in d.keys():
            d[t] = [l]
        else:
            d[t].append(l)
    u = []
    k = []
    for c in d.keys():
        u.append(len(d[c]))
        k.append(d[c])
    combined_list = zip(u, k)
    sorted_combined_list = sorted(combined_list, reverse=True)
    print( sorted_combined_list)

    return d
def word_distance(w1,w2):
    count = 0
    assert len(w1) == len(w2)
    for c1,c2 in zip(w1,w2):
        if c1 != c2:
            count += 1
    return count
def metathesis_pair(d):
    """d is a dictionary of anagrams"""
    y = dict()
    for c1 in d.keys():
        for i in range(len(d[c1])):
            if len(d[c1])>1:
                for j in range(i+1,len(d[c1])):
                    if word_distance(d[c1][i],d[c1][j])==2:
                        y[c1] = [d[c1][i]]
                        y[c1].append(d[c1][j])
    return y
def wordon2(word):
    if len(word) >= 1:
        new_word = word[:int(len(word)/2)]+word[int(len(word)/2)+1:]
        return new_word
def children(word):
    new_words = [word]
    new_word = word
    while len(new_word)>=1:
        new_words.append(new_word)
        new_word = wordon2(word)
    return new_words
def histogram(s):
    d = dict()
    for c in s:
        l = c.strip('\n')
        d[l] =d.get(l,0)+d.get(l, 1)
    return d
def reducible(fin):
    #go see tst.py this is not so right
    d = dict()
    lin = histogram(fin)
    for c in lin:
        print(c)
        if len(c)>1:
            t = children(c)
            print(t)
            if len(t) >= 1 :
                for i in t:
                    n = list(c).sort()
                    if i+'\n' in fin:
                        print("d")
                        d[n] = d.get(c,[])
                        print("d")
                        d[n].append(i)
                        print(d)
    return d
reducible(fin)          
                
                
                