import sys


def cat():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        text_file = open(filename, "r")
        text = text_file.read()
        text_file.close()
        return text
    else:
        str = "Give me a file to read"
        return str
# print(cat())


def cat2():
    if len(sys.argv) > 2:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
        text_file1 = open(filename1, "r")
        text_file2 = open(filename2, "r")
        text1 = text_file1.read() + text_file2.read()
        text_file1.close()
        text_file2.close()
        return text1
    else:
        str = "Give me two files to read from"
        return str
# print(cat2())

import sys
from random import randint


def generate_numbers(filename, n):

    l1 = []
    while len(l1) < n:
        l1.append(randint(0, 1000))
    for i in range(len(l1)):
        l1[i] = str(l1[i])
    txtf = open(filename, "w")
    txtf.write(" ".join(l1))
    txtf.close()

#print (generate_numbers("numbers.txt", 10))


def sum_numbers(filename):
    f1 = open(filename, "r")
    f = f1.read().split(" ")
    for i in range(len(f)):
        f[i] = int(f[i])
    f1.close()
    return sum(f)
# print(sum_numbers("numbers.txt"))

import os


def duhs():
    try:
        os.listdir(sys.argv[1])
    except FileNotFoundError as error:
        print(error)
    size = 0
    l = os.listdir(sys.argv[1])
    for i in range(len(l)):
        size += os.path.getsize(sys.argv[1] + "/" + l[i])
    size = size * (10**(-3))
    return size

# print(duhs())
