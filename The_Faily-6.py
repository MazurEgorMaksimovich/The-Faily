Legitim_Partii = ['1', '2', '3', '4', '5', '6', -1]

f = open("The_Faily-6.txt", "r", encoding="UTF-8")
a = f.read().split()
f.close()

A = {}
for i in a:
    j = i
    if j not in Legitim_Partii:
        j = -1
    j = int(j)
    print(j)
    A[j] = A.get(j, 0) + 1
w = []
for i, j in sorted(A.items()):
    w.append((-j, i))
k = []
for j, i in sorted(w):
    if i != -1:
        s = 'Партия №' + str(i) + '        '
    else:
        s = 'Испорченые бланки'
    k.append(s + ' | ' + str(-j) + ' | ' + str(-j*(100 / len(a))) + '%')
for _ in k:
    print(_)