glas = ['а', 'о', 'у', 'э', 'и', 'я', 'ё', 'ю', 'е', 'ы']
soglas = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
ЪУЪ = ['ь', 'ъ']
glas_k = 0
soglas_k = 0

f = open("The_Faily-4.txt", "r", encoding="UTF-8")
for i in f:
    print(i, end='')
f.close()

f = open("The_Faily-4.txt", "r", encoding="UTF-8")
s = f.read().lower().split()
for i in s:
    if i[0] in glas:
        glas_k += 1
    if i[0] in soglas:
        soglas_k += 1
print('\n')
print('Количество слов, начинающихся на гласную ---- ' + str(glas_k))
print('Количество слов, начинающихся на согласную ---- ' + str(soglas_k))
f.close()