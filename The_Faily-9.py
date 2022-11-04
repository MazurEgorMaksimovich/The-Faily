import os
import shutil

def print_docs(directory):
    print(directory)
    a = list((os.walk(directory)))
    for i in a:
        for j in i[1::]:
            for l in j:
                print("   " + l)

def operations(directory):
    oper = [i for i in input().split()]
    if oper[0] == 'copy':
        copy(oper[1], oper[2])
    elif oper[0] == 'move':
        move(oper[1], oper[2])
    elif oper[0] == 'del':
        pop(oper[1])
    elif oper[0] == 'exit':
        exit()
    else:
        exit()

def copy(file, directory):
    shutil.copy(file, directory)
    operations(input())

def move(file, directory):
    shutil.move(file, directory)
    operations(input())

def pop(file):
    os.remove(file)
    operations(input())

def exit():
    print('bye')

print_docs("The_Faily-9")
operations("The_Faily-9")