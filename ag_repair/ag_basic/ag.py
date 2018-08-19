import os
import sys
import argparse


curdir = os.getcwd()


parser = argparse.ArgumentParser()
parser.add_argument("keywords", metavar = "k", type=str)
parser.add_argument("file", metavar = "f")
parser.add_argument("--case-sensitive", dest="key", action = "store_true" )
args = parser.parse_args()



for dirpath, dirnames, filenames in os.walk(curdir):
    for file in filenames:
        with open(file) as line:
            count = 0
            for text in line:
                count += 1
                if args.key:
                    if sys.argv[1] == "--case-sensitive":
                        if args.keywords in text and args.file == file:
                            str_text = ''
                            key = ""
                            arr = ''
                            for j in args.keywords:
                                key += j
                            for i in range(len(text)):
                                arr1 = ''
                                co = 0
                                if text[i] == key[0]:
                                    arr = text[i]
                                    while len(arr) < len(key):
                                        co += 1
                                        arr += text[i+co]
                                if arr == key:
                                    arr1 += '\033[30;43m' + arr + '\033[0m' + ''
                                str_text += text[i] + ''
                            a = '\033[1;33m' + str(count) + '\033[0m'
                            print(a + ":" + str_text.replace(arr,arr1))
                if not args.key:
                    if args.keywords in text.lower():
                        if args.file == file:
                            str_text = ''
                            key = ''
                            arr = ''
                            for j in args.keywords:
                                key += j
                            for i in range(len(text)):
                                arr1 = ''
                                co = 0
                                if text[i].lower() == key[0].lower():
                                    arr = text[i]
                                    while len(arr) < len(key):
                                        co += 1
                                        arr += text[i+co]

                                if arr.lower() == key.lower():
                                    arr1 += '\033[30;43m' + arr + '\033[0m' + ''
                                str_text += text[i] + ''

                            a = '\033[1;33m' + str(count) + '\033[0m'
                            print(a + ":" + str_text.replace(arr,arr1))


# def check_line(key, text):
#     cout = 0
#     for i in text:
#         for j in key:
#             if key[0] == i:
#                 while True:
#                     cout += 1
#                     if key[cout] == key[0]:
#                         cout += 1
#                         if key[cout] == j:
#                             return True
#     return False

# print(check_line(args.keywords, "syhHTsZMewAUTgcAsqakpa"))
