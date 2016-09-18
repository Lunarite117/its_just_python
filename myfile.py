"""
#letter typer

import time
import random

random.seed(1)

text = "hey man, what's up?"
x = 0

for x in range(len(text)):
    r = random.uniform(.2,.6)
    print text[x],
    time.sleep(r)
"""
"""
#script that finds every possible (in dictionary.txt) word contained in user input

f = open('dictionary.txt','r')
pasta = raw_input('type out a word ')
tuna = "".join(sorted(list(set(pasta.lower()))))

for word in f:
    line = word.rstrip('\n')
    salmon = "".join(sorted(list(set(line.lower()))))
    if((salmon == tuna) & (pasta != line)):
        print line

"""
"""
#FINAL WORD SORTING SCRIPT (WORKS)

g = open('paragraph.txt','r')
x = 0

for word in g:
    oyster = word.replace(";","").replace(",","").replace(".","").lower()
    fish = sorted(list(set(oyster.split())))

for elem in fish:
    print x,elem
    x+=1
"""


#BUBBLE SORT!

import time
import os


i = 0  #increments for appending to list
a = 0
b = 1
temp = 0 #holds value for swap
v = 0 #for the display dots loop
n = open('somenumbers.txt','r')

numbers = list(n)
intlist= list([])

for elem in numbers:
    elem.lstrip("\n")
    intlist.append(int(numbers[i]))
    i=i+1

start_time = time.time()
while(sorted(intlist) != intlist):
    for elem in intlist:
        if(intlist[a] > intlist[b]):
            temp = intlist[b]
            intlist[b] = intlist[a]
            intlist[a] = temp
            a = a+1
            b = b+1

            if(b >= len(intlist)):
                    a = 0
                    b = 1
        else:  #if numbers are in order increment anyway to go to the next pair... and check to reset a and b count
            a = a+1
            b = b+1
            if(b >= len(intlist)):
                    a = 0
                    b = 1

    os.system('cls')
    v=0
    for elem in intlist:
        print(intlist[v],"-"*intlist[v])
        v = v+1
    print"========================="
elapsed_time = time.time() - start_time
print("time elapsed: ",elapsed_time)
print intlist
time.sleep(100)
