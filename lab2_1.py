a=open('books.csv').readlines()
tabl=[]
for i in range(len(a)):
    tabl.append(a[i].split(';'))
count=0
print(tabl[0][1])
for nazv in range(len(tabl)):
    if len(tabl[nazv][1])>30:
        count+=1
print(count)

