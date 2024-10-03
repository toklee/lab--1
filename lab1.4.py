a=open('sequence.txt').readlines()
f=[]
for element in a:
    f.append(float(element))
otr=0
pol=0
for i in range(len(f)):
    if f[i]>=0:
        pol+=1
    else:
        otr+=1
print(">0","\x1b[48;5;212m "*((pol*100)//len(f)),"\x1b[m",round((pol*100)/len(f),2),"%")
print("<0","\x1b[48;5;194m "*((otr*100)//len(f)),"\x1b[m",round((otr*100)/len(f),2),"%")