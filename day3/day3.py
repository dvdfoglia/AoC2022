import os
from textwrap import wrap
d="day3"
dname = os.path.dirname(os.path.abspath(__file__))
priority=0
b=True

def read_input():
    f = dname+"/"+d+".txt"
    input = open(f,'r')
    i = input.read().splitlines()
    input.close()
    return i

data=read_input()

for i in data:
    rucksack=wrap(i,len(i)//2)
    b=True
    for item1 in wrap(rucksack[0],1):
        if b:
            for item2 in wrap(rucksack[1],1):
                if item1==item2:
                    if ord(item1)-96>0:
                        priority=priority+ord(item1)-96
                    else:
                        priority=priority+ord(item1)-38
                    b=False
                    break
        else:
            break
print(priority)