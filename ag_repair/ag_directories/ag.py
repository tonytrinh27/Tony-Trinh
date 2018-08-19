import os
import sys
import argparse


curdir = os.getcwd()


parser = argparse.ArgumentParser()
group1 = parser.add_mutually_exclusive_group(required=True)
parser.add_argument("keywords", type=str)
parser.add_argument("file", type=str)
# group2 = parser.add_mutually_exclusive_group(required=True)
parser.add_argument("-2file", dest="fl", action = "store_true")
parser.add_argument("--case-sensitive", dest="key", action = "store_true" )
args = parser.parse_args()


file_flag = 0
for dirpath, dirnames, filenames in os.walk(curdir):
    for file in filenames:
        if file_flag == 1:
            print(file)
        with open(file) as line:
            count = 0
            for text in line:
                count += 1
                if args.key:
                    if args.fl:
                        if sys.argv[1] == "--case-sensitive":
                            if args.keywords in text and args.file == file:
                                file_flag = 1
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
                    if args.fl:
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
                    if not args.fl:
                        file_flag = 1
                        if args.keywords in text.lower():
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
