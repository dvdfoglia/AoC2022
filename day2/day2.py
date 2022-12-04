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
class draw3:
    p2_loose="X"
    p2_draw="Y"
    p2_win="Z"


def read_input():
    f = dname+"/"+d+".txt"
    input = open(f,'r')
    i = input.read().splitlines()
    input.close()
    return i
def rule1(x,y):
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
                case draw2.s2:
                    return scissors+win
        case draw1.s1:
            match y:
                case draw2.r2:
                    return rock+win
                case draw2.p2:
                    return paper
                case draw2.s2:
                    return scissors+draw

def rule2(x,y):
    match x:
        case draw1.r1:
            match y:
                case draw3.p2_draw:
                    return rock+draw
                case draw3.p2_win:
                    return paper+win
                case draw3.p2_loose:
                    return scissors
        case draw1.p1:
            match y:
                case draw3.p2_loose:
                    return rock
                case draw3.p2_draw:
                    return paper+draw
                case draw3.p2_win:
                    return scissors+win
        case draw1.s1:
            match y:
                case draw3.p2_win:
                    return rock+win
                case draw3.p2_loose:
                    return paper
                case draw3.p2_draw:
                    return scissors+draw


data=read_input()

for i in data:
    play=i.split()
    p2_points=p2_points+rule1(play[0],play[1])

print(p2_points)
p2_points=0

for i in data:
    play=i.split()
    p2_points=p2_points+rule2(play[0],play[1])

print(p2_points)