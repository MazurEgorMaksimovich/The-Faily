f = open("The_Faily-1.txt", "w", encoding="UTF-8")
f.write("\n".join(str(x) for x in input().split()) + "\n")
f.close()