with open ('sequence.txt') as a:
    sequence = a.readlines()
file = []
for element in sequence:
    file.append(float(element))
otr = 0
pol = 0
for el in range(len(file)):
    if file[el] >= 0:
        pol += 1
    else:
        otr += 1
print(">0", "\x1b[48;5;212m "*((pol*100)//len(file)), "\x1b[m",round((pol*100)/len(file), 2), "%")
print("<0", "\x1b[48;5;194m "*((otr*100)//len(file)), "\x1b[m",round((otr*100)/len(file), 2), "%")