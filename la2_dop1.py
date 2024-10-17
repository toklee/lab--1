with open('books-en.csv') as a:
    spisok = a.readlines()
tabl = []

for i in range(len(spisok)):
    tabl.append(spisok[i].split(';'))
publishers = []

for izdat in range(1,len(tabl)):
    if not(tabl[izdat][4] in publishers):
        publishers.append(tabl[izdat][4])
print(publishers)

