import os
d="day7"
dname = os.path.dirname(os.path.abspath(__file__))
ls=False
wd=[0,"/"]
fileD={}
dirSize={}
res=0

def read_input():
    f = dname+"/"+d+".txt"
    with open(f) as file:
        return file.readlines()

def cd(c,l,w):
    match c:
        case "..": 
            if l>0: l-=1; w.pop()
        case "/": l=0; w=["/"]
        case _: l+=1; w.append(c)
    return l,w

def pathExist(x):
    for k,v in fileD.items():
        print(v)

#create fileD dict 
for i in read_input():
    x=i.split()
    if x[0]=="$":
        match x[1]:
            case "ls": ls=True
            case "cd":
                ls=False
                wd=cd(x[2],wd[0],wd[1])
    else:
        if ls:
            if x[0] != "dir": 
                path="/".join(wd[1]).replace("//","/")
                if len(path)==1: pathL=[path]
                else: pathL=[path[0]]; pathL.extend(path[1:].split("/"))
                file=path+x[1]
                fileD[file] = {"filename" : file, "filesize" : x[0], "path" : pathL}

#Calc dir Size
for k, v in fileD.items():
    wd=""
    for x in v["path"]:
        wd+=x+"/" if x!="/" else x
        if wd not in dirSize.keys(): dirSize[wd]=0
        dirSize[wd]+= int(v["filesize"])

#Calc solution part1
for k, v in dirSize.items():
    if v<=100000:
        res+=v

print(f"Part1", res)

#Part2

diskSpace=70000000
neededSpace=30000000
unusedSpace=diskSpace-dirSize["/"]
minToBeDeleted=neededSpace-unusedSpace


for k,v  in sorted(dirSize.items(), key=lambda x:x[1]):
    if v>=minToBeDeleted:
        print(f"Part2", v)
        break