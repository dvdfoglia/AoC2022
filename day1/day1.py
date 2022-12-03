import os
d="day1"
dname = os.path.dirname(os.path.abspath(__file__))

def read_input():
    f = dname+"/"+d+".txt"
    input = open(f,'r')
    i = input.read().splitlines()
    input.close()
    return i
elf=0
tot_cal=[0]
tot_cal3=0
data=read_input()
for t in data:
    #print(elf)
    if t == "":
        elf=elf+1
        tot_cal.append(0)
    else:
        cal=int(t)
        tot_cal[elf]=tot_cal[elf]+cal

print("Top1 sum ",max(tot_cal))

tot_cal.sort(reverse=True)
for i in range(0,3):
    tot_cal3=tot_cal3+tot_cal[i]
print("Top3 Sum ",tot_cal3)