import string
from matplotlib import scale
import matplotlib.pyplot as plt
fin = open(r"book.txt", encoding='utf-8')
def freq(fin):
    d = dict()
    t = []
    for l in fin:
        t = l.split()
        for w in t:
            w = w.strip(string.punctuation + string.whitespace)
            w = w.lower()
            d[w] = d.get(w,0) + 1
    return d
def rank(d):
    t = list(d.values())
    t.sort(reverse = True)
    rf = [(r+1, f) for r, f in enumerate(t)]
    return rf
    
def plot_word(rf):
    rank,fr = zip(*rf)
    plt.clf()
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rank, fr, 'r-', linewidth=3)
    plt.show()
d = freq(fin)
f = rank(d)
plot_word(f)
