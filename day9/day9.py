import os
d="day9"
dname = os.path.dirname(os.path.abspath(__file__))
data=[]
h=[0,0]
t=[0,0]
knots={"H" : [0,0], "T" : [0,0]}
touchT=set()

def read_input():
    f = dname+"/"+d+".txt"
    with open(f) as file:
        return file.readlines() 

for i in read_input():
    i=i.strip().replace(" ","")
    data.append([[*i][0],int(i.lstrip('UDRL'))])

def moveK(kB,kA):
    dX=abs(kB[0]-kA[0])
    dY=abs(kB[1]-kA[1])
    if dX <=1 and dY <=1:
        pass
    elif dX > 1 and dY > 1:
        kA = [kB[0]-1 if kB[0]>kA[0] else kB[0]+1, kB[1]-1 if kB[1]>kA[1] else kB[1]+1]
    else:
        if dX > 1:
            kA[1]=kB[1]
            if kB[0]>kA[0]: kA[0]=kB[0]-1
            else: kA[0]=kB[0]+1
        if dY > 1:
            kA[0]=kB[0]
            if kB[1]>kA[1]: kA[1]=kB[1]-1
            else: kA[1]=kB[1]+1
    return kA
    
touchT=set()

for i in data:
    if i[0] == "U": 
        for y in range(0,i[1]):
            knots["H"][1]+=1
            knots["T"]=moveK(knots["H"],knots["T"])
            touchT.add("x"+str(knots["T"][0])+"y"+str(knots["T"][1]))
    if i[0] == "D":
        for y in range(0,i[1]):
            knots["H"][1]-=1
            knots["T"]=moveK(knots["H"],knots["T"])
            touchT.add("x"+str(knots["T"][0])+"y"+str(knots["T"][1]))
    if i[0] == "R":
        for x in range(0,i[1]):
            knots["H"][0]+=1
            knots["T"]=moveK(knots["H"],knots["T"])
            touchT.add("x"+str(knots["T"][0])+"y"+str(knots["T"][1]))
    if i[0] == "L":
        for x in range(0,i[1]):
            knots["H"][0]-=1
            knots["T"]=moveK(knots["H"],knots["T"])
            touchT.add("x"+str(knots["T"][0])+"y"+str(knots["T"][1]))

print("Part1", len(touchT))

#Part2
touchT=set()
knots={"H" : [0,0]}
for i in range(1,10):
    knots[i]=[0,0]

for i in data:
    if i[0] == "U": 
        for y in range(0,i[1]):
            knots["H"][1]+=1
            knots[1]=moveK(knots["H"],knots[1])
            for k in range(2,10):
                knots[k]=moveK(knots[k-1],knots[k])
            touchT.add("x"+str(knots[9][0])+"y"+str(knots[9][1]))
    if i[0] == "D":
        for y in range(0,i[1]):
            knots["H"][1]-=1
            knots[1]=moveK(knots["H"],knots[1])
            for k in range(2,10):
                knots[k]=moveK(knots[k-1],knots[k])
            touchT.add("x"+str(knots[9][0])+"y"+str(knots[9][1]))
    if i[0] == "R":
        for x in range(0,i[1]):
            knots["H"][0]+=1
            knots[1]=moveK(knots["H"],knots[1])
            for k in range(2,10):
                knots[k]=moveK(knots[k-1],knots[k])
            touchT.add("x"+str(knots[9][0])+"y"+str(knots[9][1]))
    if i[0] == "L":
        for x in range(0,i[1]):
            knots["H"][0]-=1
            knots[1]=moveK(knots["H"],knots[1])
            for k in range(2,10):
                knots[k]=moveK(knots[k-1],knots[k])
            touchT.add("x"+str(knots[9][0])+"y"+str(knots[9][1]))

print("Part2",len(touchT))