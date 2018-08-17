# !/usr/bin/env ipython3
import os
import glob
import re
import sys


# list_file = ['file2.txt', 'file1.txt']
list_file = glob.glob("*")
list_file_hidden = glob.glob(".*")


find_word = sys.argv[1:]
len_find = len(find_word)


key_in_file = []
key_in_file_hidden = []
key1 = []
key2 = []


for file in list_file_hidden:
    with open(file, 'r') as line:
        for text in line:
            for n in find_word:
                if n in text.lower():
                    key_in_file_hidden.append(n)


for file in list_file:
    with open(file, 'r') as line:
        for text in line:
            for n in find_word:
                if n in text:
                    key_in_file.append(n)


for i in key_in_file:
    if len_find == 1 and sys.argv[1] == i:
        key1.append(sys.argv[1])
    elif len_find == 2:
        key2.append(sys.argv[1:3])


def first(list_file, find_word):
    if len_find == 1 and sys.argv[1] in key_in_file:
        for file in list_file:
            print('\033[1;32m' + file + '\033[0m')
            with open(file, 'r') as line:
                count = 0
                for text in line:
                    count += 1
                    word = sys.argv[1]
                    if word in text.lower():
                        str_text = ''
                        for i in text.split():
                            if i.lower() == word:
                                str_text += '\033[30;43m' + i + '\033[0m' + ' '
                            else:
                                str_text += i + ' '
                        a = '\033[1;33m'+ str(count) + '\033[0m'
                        b = '\033[30;43m' + str_text + '\033[0m'
                        print(a + ":" + b)
                print()
    if len_find == 2 and sys.argv[2] in key_in_file and sys.argv[1] == "--case-sensitive":
        for file in list_file:
            print('\033[1;32m' + file + '\033[0m')
            with open(file, 'r') as line:
                count = 0
                for text in line:
                    count += 1
                    word = sys.argv[2]
                    if word in text:
                        str_text = ''
                        for i in text.split():
                            if i.lower() == word:
                                str_text += '\033[30;43m' + i + '\033[0m' + ' '
                            else:
                                str_text += i + ' '
                        a = '\033[1;33m'+ str(count) + '\033[0m'
                        b = '\033[30;43m' + str_text + '\033[0m'
                        print(a + ":" + b)
                print()
    if len_find == 2 and sys.argv[1] in key_in_file and sys.argv[2] == ".":
        for file in list_file:
            print('\033[1;32m' + file + '\033[0m')
            with open(file, 'r') as line:
                count = 0
                for text in line:
                    count += 1
                    word = sys.argv[1]
                    if word in text.lower():
                        str_text = ''
                        for i in text.split():
                            if i.lower() == word:
                                str_text += '\033[30;43m' + i + '\033[0m' + ' '
                            else:
                                str_text += i + ' '
                        a = '\033[1;33m'+ str(count) + '\033[0m'
                        b = '\033[30;43m' + str_text + '\033[0m'
                        print(a + ":" + b)
                print()
    if len_find == 2 and sys.argv[1] in key_in_file and sys.argv[2] in list_file:
        for file in list_file:
            if sys.argv[2] == file:
                with open(file, 'r') as line:
                    count = 0
                    for text in line:
                        count += 1
                        word = sys.argv[1]
                        if word in text.lower():
                            str_text = ''
                            for i in text.split():
                                if i.lower() == word:
                                    str_text += '\033[30;43m' + i + '\033[0m' + ' '
                                else:
                                    str_text += i + ' '
                            a = '\033[1;33m'+ str(count) + '\033[0m'
                            b = '\033[30;43m' + str_text + '\033[0m'
                            print(a + ":" + b)
    if len_find == 2 and sys.argv[2] in key_in_file_hidden and sys.argv[1] == "--hidden":
        for file in list_file_hidden:
            print('\033[1;32m' + file + '\033[0m')
            with open(file, 'r') as line:
                count = 0
                for text in line:
                    count += 1
                    word = sys.argv[2]
                    if word in text.lower():
                        str_text = ''
                        for i in text.split():
                            if i.lower() == word:
                                str_text += '\033[30;43m' + i + '\033[0m' + ' '
                            else:
                                str_text += i + ' '
                        a = '\033[1;33m'+ str(count) + '\033[0m'
                        b = '\033[30;43m' + str_text + '\033[0m'
                        print(a + ":" + b)
                print()



first(list_file, find_word)
