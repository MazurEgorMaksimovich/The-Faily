def longest_words(file):
    f = open(file, "r", encoding="UTF-8")
    a = f.read().split()
    f.close()

    m = 0
    s = []
    for i in a:
        n = 0
        for j in i:
            n += 1
        if n > m:
            m = n
            s = []
            s.append(i)
        elif n == m:
            s.append(i)
    print(*s)

longest_words("The_Faily-8.txt")