with open('books-en.csv') as a:
    spisok = a.readlines()
tabl = []

for i in range(len(spisok)):
    tabl.append(spisok[i].split(';'))
popular = []

for num in range(1,len(tabl)):
    popular.append(int(tabl[num][-2]))
MAXPOP = max(popular)
count = 0

for nazv in range(1,len(tabl)):
    if count<20 and int(tabl[nazv][-2]) == MAXPOP:
        print(tabl[nazv][1])
        count+=1

