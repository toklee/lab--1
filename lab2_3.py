with open('books.csv') as a:
    spisok = a.readlines()

tabl = []
for i in range(len(spisok)):
    tabl.append(spisok[i].split(';'))
k = 1

for num in range(1,len(tabl)):
    if k < 21:
        print(num, tabl[num][3], '<', tabl[num][1], '>', tabl[num][6])
        k += 1