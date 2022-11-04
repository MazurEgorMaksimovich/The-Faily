import os

def print_docs(directory):
    a = list((os.walk(directory)))
    for i in a:
        print(*i)

print_docs('The_Faily-7')