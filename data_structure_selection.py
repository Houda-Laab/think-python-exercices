import string
import random
fin = open(r"book.txt", encoding='utf-8')
def lines(fin):
    res = []
    for line in fin:
        l = line.replace('-',' ')
        word = l.strip(string.whitespace).lower()
        res += word.split()
    return res
def process_file(filename):
    h = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, h)
    return h
def process_line(line, h):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        h[word] = h.get(word, 0) + 1
def randm(t):
    for i in range(10):
        print(random.choice(t),end = ' ')

def words(t):
    d = dict()
    cr = dict()
    for c in range(len(t)-1):
        d[t[c]] = d.get(t[c],[])
        d[t[c]].append(t[c+1])
    for k in d.keys():
        for i in range(len(d[k])):
            if d[k].count(d[k][i]) > 20 :
                cr[k] = cr.get(k,[])
                if  d[k][i] not in cr[k]:
                    cr[k].append( d[k][i])
        if k not in cr.keys():
            cr[k] = [max(set(list(d[k])), key=d[k].count)]
                
    return cr
def random_word(h):
    k = random.choice(list(h.keys()))
    v = random.choice(h[k])
    print(k,end='')
    for i in range(100):
        v = random.choice(h[k])
        print(' '+v+' ',end='')
        k = v
    
#print('friend '+cr['friend'][random.randint(0,len(cr['friend']))]+ 'free ' + cr['free'][random.randint(0,len(cr['free']))])
        
