with open('books.csv') as a:
    spisok = a.readlines()
tabl = []

for i in range(len(spisok)):
    tabl.append(spisok[i].split(';'))
#print(tabl[0][1])

for number in range(len(tabl)):
    if len(tabl[number][1])>30:
        count += 1
print(count)