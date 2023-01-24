fin = open(r"C:\Users\Admin\AppData\Local\Programs\Python\Python311\swampy\words.txt")
import nltk
from nltk.corpus import cmudict
def store_word(fin):
    dictionary = dict()
    i  = 0
    for c in fin:
        l  = c.strip('\n')
        dictionary[l] = [i+1]
        i = i+1
    return dictionary
def histogram(s):
    d = dict()
    for c in s:
        l = c.strip('\n')
        d[l] =d.get(l,0)+d.get(l, 1)
    return d

def print_hist(h):
    l =list( h.keys())
    l.sort()
    for c in l:
        print(c, h[c])
def reverse_lookup(d, v):
    l = []
    for k in d:
        if d[k] == v:
            l = l + [k]
    return v
def invert_dict1(d):
    inverted = {}
    for key, value in d.items():
        inverted.setdefault(value, []).append(key)
    return inverted  
def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv 
def has_duplicate(d):
    for k in d:
        if len([d[k]])!=1:
            return True
    return False
def rotate_word(word,code):
    nword = word.strip()
    result = " "
    for c in nword:
        a = ord(c)+code
        result = result+chr(a)
    return result.strip()
def all_rotate(fin):
    t = []
    s = histogram(fin)
    for n in s:
        l = n.strip('\n')
        for i in range(1,24):
            r = rotate_word(l,i)
            if r in s:
                t.append([r,l])
    return t
def find_homophones(word):
    d = cmudict.dict()
    homophones = []
    for w in d.keys():
        if word not in d.keys():
            return homophones
        elif word != w and d[word] == d[w]:
            homophones.append(w)
    return homophones
def puzzler_homophones(fin):
    """answer of exercice 11.9 the puzzler
    """
    t = []
    for c in fin:
        word = c.strip('\n')
        word1 = word[1:]
        word2 = word[0]+word[2:]
        homophones = find_homophones(word)
        if (word1 in homophones) and (word2 in homophones):
            t.append([word])
    return t
