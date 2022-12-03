import os
d="day2"
dname = os.path.dirname(os.path.abspath(__file__))

rock=1
paper=2
scissors=3
lost=0
draw=3
win=6
p2_points=0

class draw1:
    r1="A"
    p1="B"
    s1="C"
class draw2:
    r2="X"
    p2="Y"
    s2="Z"


def read_input():
    f = dname+"/"+d+".txt"
    input = open(f,'r')
    i = input.read().splitlines()
    input.close()
    return i
def def_win(x,y):
    match x:
        case draw1.r1:
            match y:
                case draw2.r2:
                    return rock+draw
                case draw2.p2:
                    return paper+win
                case draw2.s2:
                    return scissors
        case draw1.p1:
            match y:
                case draw2.r2:
                    return rock
                case draw2.p2:
                    return paper+draw
                case s2:
                    return scissors+win
        case draw1.s1:
            match y:
                case draw2.r2:
                    return rock+win
                case draw2.p2:
                    return paper
                case draw2.s2:
                    return scissors+draw

data=read_input()

for i in data:
    play=i.split()
    p2_points=p2_points+def_win(play[0],play[1])

print(p2_points)