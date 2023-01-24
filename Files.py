"""functions to solve exercises in Chapter 14. Files"""
import os
import hashlib
import urllib.request
import gzip
import shelve

##Exercice 14.5 "the secret"
def zipcode():
    
    zipcode = input("enter zipcode: ")

    url = 'http://uszip.com/zip/' + zipcode
    conn = urllib.request.urlopen(url)
    file = conn.fp
    file = file.read()
    file = file.decode()
    file = file.split('\n')

    for line in range(len(file)):
    
        myline= file[line].strip()
        if "is the zip code for" in myline: 
            s = file[line+1].strip()
            s = s.replace('<',' ')
            s = s.replace('>',' ')
            t = s.split()
            word = t[2]
            if t[-1] != ',':
                word +=" " +t[3]
            print('the name of the town is : '+word)
        if 'Total population' in myline:
            s = myline.replace('<',' ')
            s = s.replace('>',' ')
            t = s.split()
            for i in range(len(t)):
                if t[i] == 'population':
                    word = t[i+3]
            print("the total population of this area is:"+word)
            break

    conn.close()
t = []
def walk(dir):
    """a function that walks through a directory and returns a list its files 

    Args:
        dir (str): path to the directory

    Returns:
        list: files in the directory
    """
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            t.append(path)
        else:
            walk(path)
    return t
#Exercice 14.6
#1
def files(dirctr,type = '.mp3'): 
    """a function that walks through a directory and returns a list its mp3 files  

    Args:
        dirctr (str): path to the directory
        type (str): the extention of the files 

    Returns:
        list:path to the files in the directory that are from the given type
    """
    t = []  
    for fn in walk(dirctr):
        name,ext = os.path.splitext(fn)
        if ext == type:
            t.append(str(os.path.abspath(fn)))
    return t
#2
def duplicates(t):
    """a function that looks for the duplicated files 

    Args:
        t (list): list of paths to the files in a directory (generated with files())
    """
    v =[]
    d = dict()
    for path in t:
        print(path)
        # Open the file in binary mode
        file = open(path, 'rb')
        # create a new md5 object
        md5 = hashlib.md5()
        chunkfile = file.read(4096)
        md5.update(chunkfile)
        if md5.hexdigest() in d:
            d[md5.hexdigest()].append(path)
            v.append(d[md5.hexdigest()])
        else:             
            d[md5.hexdigest()] = [path]
    return v        
#Exercice 14.7
def read_actors():
    db = shelve.open("my_database")
    with gzip.open("actors.list.gz", "rt", encoding='utf-8') as temp:
        next(temp)
        next(temp)
        actors_list = temp.read()
    with gzip.open("actresses.list.gz", "rt", encoding='utf-8') as f:
        actresses_list = f.read()
    actors_list = actors_list.split('\n')
    for line in actors_list:
        t = line.split('\t') 
        print(line)
        print(t[0])
        if t[0] in db:
            db[t[0]].append(t[1])
        else:
            db[t[0]] = [t[1]]
    for line in actresses_list:
        t = line.split('\t')
        if t[0] in db:
            db[t[0]].append(t[1])
        else:
            db[t[0]] = [t[1]]
    return db
    
print(read_actors())





