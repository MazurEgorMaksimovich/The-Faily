def isnumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

f = open("The_Faily-1.txt", "r", encoding="UTF-8")
a = []
i = 0
for item in f:
    if isnumeric(item):
        i += float(item)
        a.append(float(item))
a_max = max(a)
f.close()

i = str(i)
if i[-2::] == ".0":
    i = float(i)
    i = int(i)
a_max = str(a_max)

if a_max[-2::] == ".0":
    a_max = float(a_max)
    a_max = int(a_max)

f = open("The_Faily-1.txt", "a", encoding="UTF-8")
f.write(str(i) + "\n")
f.write(str(a_max) + "\n")
f.close()