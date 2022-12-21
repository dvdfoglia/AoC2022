import os
d="day11"
dname = os.path.dirname(os.path.abspath(__file__))
data={}

def read_input():
    f = dname+"/"+d+".txt"
    with open(f) as file:
        return file.readlines()

def load_data():
    for i in read_input():
        if i=="\n": pass
        else:
            tmpList=i.replace(":","").replace(",","").split()
            if tmpList[0]=="Monkey":
                tmpM=tmpList[0]+tmpList[1]
                data[tmpM]={"Items" : [], "Operation" : [] , "Test" : [], "True" : [], "False" : [], "Count" : 0}
            if tmpList[0]=="Starting": del tmpList[0:2]; data[tmpM]["Items"]=list(map(int, tmpList))
            if tmpList[0]=="Operation": del tmpList[0:4]; data[tmpM]["Operation"] = tmpList
            if tmpList[0]=="Test": data[tmpM]["Test"] = int(tmpList[3])
            if len(tmpList) > 1 and tmpList[1]=="true": data[tmpM]["True"] = "Monkey"+tmpList[5]
            if len(tmpList) > 1 and tmpList[1]=="false": data[tmpM]["False"] = "Monkey"+tmpList[5]
    return data

def inspection(items,op,w,test_all):
    tlist=[]
    if w==1: ops = {"+": (lambda x,y: (x+y)%test_all), "*": (lambda x,y: x*y%test_all)}
    else: ops = {"+": (lambda x,y: (x+y)/w), "*": (lambda x,y: x*y/w)}
    for i in items:
        if op[1]=="old": tlist.append(int(ops[op[0]](i,i)))
        else: tlist.append(int(ops[op[0]](i,int(op[1]))))
    return tlist

def throw(k,items,test,ifTrue,ifFalse):
    for i in items:
        data[k]["Count"]+=1
        if i % test == 0:
            data[ifTrue]["Items"].append(i)
        else: 
            data[ifFalse]["Items"].append(i)
    data[k]["Items"].clear()

def play(w,test_all):
    for k, v in data.items():
        data[k]["Items"]=inspection(v["Items"],v["Operation"],w,test_all)
        throw(k,list(v["Items"]),v["Test"],v["True"],v["False"])

def result(data,part):
    c=0
    res=0
    data = dict(sorted(data.items(), key=lambda x: x[1]['Count'],reverse=True))
    for k,v in data.items():
        if res==0: res=v["Count"]
        else: res*=v["Count"]
        c+=1
        if c==2: break
    print(part,res)

def main():
    load_data()
    test_all=1
    for k,v in data.items():
        test_all*=v["Test"]
    for i in range(20):
        play(3,test_all)
    result(data,"Part1")
    load_data()
    for i in range(10000):
        play(1,test_all)
    result(data,"Part2")
main()