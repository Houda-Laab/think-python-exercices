import random
def cumulative_sum(t):
    c = t[0]
    res = [t[0]]
    for i in range(1,len(t)):
        c += t[i]
        res.append(c)
    return res
def chop(t):
    del t[0]
    del t[-1]
def middle(t):
    t2 = t[1:-1]
    return t2
def is_sorted(t):
    s = t[:]
    s.sort()
    if s[:] == t[:]:
        return True
    return False
def is_anagram(word1,word2):
    t1 = list(word1.lower())
    t2 = list(word2.lower())
    t1.sort()
    t2.sort()
    if t1 == t2:
        return True
    return False
def has_duplicates(t):
    s = t[:]
    s.sort()
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            return True
    return False
def remove_duplicates(t):
    s = t[:]
    s.sort()
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            del s[i-1]
    return s
s = []
for i in range(23):
    s = s + [str(random.randint(1,12)) + "_" + str(random.randint(1,30))]
s.sort()
print(s)
print(has_duplicates(s))