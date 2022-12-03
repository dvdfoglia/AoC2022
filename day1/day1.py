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
data=read_input()
for t in data:
    #print(elf)
    if t == "":
        elf=elf+1
        tot_cal.append(0)
    else:
        cal=int(t)
        tot_cal[elf]=tot_cal[elf]+cal

print(max(tot_cal))