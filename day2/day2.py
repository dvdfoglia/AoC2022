import os
d="day2"
dname = os.path.dirname(os.path.abspath(__file__))

paper=2
scissors=3
lost=0
draw=3
win=6
r1="A"
p1="B"
s1="C"
r1="X"
p1="Y"
s1="Z"


def read_input():
    f = dname+"/"+d+".txt"
    input = open(f,'r')
    i = input.read().splitlines()
    input.close()
    return i

data=read_input()

for i in data:
    play=i.split()
    print(play)