with open('books.csv') as a:
    spisok = a.readlines()
tabl = []

for i in range(len(spisok)):
    tabl.append(spisok[i].split(';'))
#print(tabl[0][3])
#print(tabl[0][7])
AUTOR = input()

for num in range(len(tabl)):
    if tabl[num][3] == AUTOR and float(tabl[num][7]) < 150:
        print(tabl[num][3],"<",tabl[num][1],">","Цена :",tabl[num][7])