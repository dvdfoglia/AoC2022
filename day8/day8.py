import os
d="day8"
dname = os.path.dirname(os.path.abspath(__file__))
data=[]
max={}
maxR={}
res={}
visible=0
maxScore=0

def read_input():
    f = dname+"/"+d+".txt"
    with open(f) as file:
        return file.readlines() 

#Create nested array
for i in read_input():
    data.append([int(x) for x in [*i.rstrip()]])

#Calc visibility from Top and Left
cX=0
cY=0

for x in data:
    cY=0
    for y in x:
        pos=str(cX)+"_"+str(cY)
        res[pos]={"isVisibleT" : False, "isVisibleL" : False, "isVisibleB" : False , "isVisibleR" : False}
        #isVisibleL=False
        if "maxX"+str(cX) not in max.keys(): max["maxX"+str(cX)]=-1
        if "maxY"+str(cY) not in max.keys(): max["maxY"+str(cY)]=-1
        if y > max["maxX"+str(cX)]:
            max["maxX"+str(cX)] = y
            res[pos]["isVisibleL"]=True
        if y > max["maxY"+str(cY)]:    
            max["maxY"+str(cY)] = y
            res[pos]["isVisibleT"]=True
        cY+=1
    cX+=1


#Calc visibility from Bottom and Right
data.reverse()

cX=len(data)-1
for x in data:
    cY=len(x)-1
    x.reverse()
    for y in x:
        pos=str(cX)+"_"+str(cY)
        if "maxX"+str(cX) not in maxR.keys(): maxR["maxX"+str(cX)]=-1
        if "maxY"+str(cY) not in maxR.keys(): maxR["maxY"+str(cY)]=-1
        if y > maxR["maxX"+str(cX)]:
            maxR["maxX"+str(cX)] = y
            res[pos]["isVisibleR"]=True
        if y > maxR["maxY"+str(cY)]:    
            maxR["maxY"+str(cY)] = y
            res[pos]["isVisibleB"]=True
        cY-=1
    cX-=1


#Resolve part1
for k, v in res.items():
    if v["isVisibleT"] or v["isVisibleL"] or v["isVisibleB"] or v["isVisibleR"]:
        visible+=1

print("Part1", visible)

data=[]

#Part 2

#Create nested array
for i in read_input():
    data.append([int(x) for x in [*i.rstrip()]])

cX=0
cY=0
endX=len(data[0])
endY=len(data)
res={}

#Calc score
for y in data:
    cX=0
    for x in y:
        scoreN = 0; scoreL = 0; scoreB = 0; scoreR = 0
        pos=str(cX)+"_"+str(cY)
        res[pos]={"scoreR" : 0, "scoreD" : 0, "scoreL" : 0 , "scoreU" : 0}
        for z in range(cX+1,endX): 
            if x > data[cY][z]: res[pos]["scoreR"]+=1
            elif x <= data[cY][z]: res[pos]["scoreR"]+=1; break
            else: break
        for z in range(cY+1,endY): 
            if x > data[z][cX]: res[pos]["scoreD"]+=1
            elif x <= data[z][cX]: res[pos]["scoreD"]+=1; break
            else: break
        for z in range(cX-1,-1,-1): 
            if x > data[cY][z]: res[pos]["scoreL"]+=1
            elif x <= data[cY][z]: res[pos]["scoreL"]+=1; break
            else: break
        for z in range(cY-1,-1,-1):
            if x > data[z][cX]: res[pos]["scoreU"]+=1
            elif x <= data[z][cX]: res[pos]["scoreU"]+=1; break
            else: break
        cX+=1
    cY+=1

#Calc tot score
for k, v in res.items():
    if v["scoreR"]*v["scoreD"]*v["scoreL"]*v["scoreU"] > maxScore:
        maxScore = v["scoreR"]*v["scoreD"]*v["scoreL"]*v["scoreU"]

print("Part2", maxScore)