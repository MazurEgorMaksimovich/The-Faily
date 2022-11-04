A = []
l = 0

f = open("The_Faily-5.txt", "r", encoding="UTF-8")
for i in f:
    a = i.split()
    A.append(a)
f.close()

for a in A:
    for i in a:
        if i == '0':
            l += 1
print(l)

n, m = [int(x) for x in input().split()]
a = A[n-1][m-1]
if a == '0':
    print('Место свободно.')
elif a == '1':
    print('Место занято.')
else:
    print('Произошла неизвестная ошибка.')