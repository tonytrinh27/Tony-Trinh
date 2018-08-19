import os
import sys
import argparse


curdir = os.getcwd()


parser = argparse.ArgumentParser()
parser.add_argument("keywords", nargs='*')
# parser.add_argument("file", nargs='+')

# case = argparse.ArgumentParser()
parser.add_argument("--case-sensitive", dest="key", action = "store_true")
parser.add_argument("--hidden", dest="hid", action = "store_true")

args = parser.parse_args()
# case1 = case.parse_args()



for dirpath, dirnames, filenames in os.walk(curdir):
    file_show = [f for f in filenames if not f[0] == '.']
    for file in file_show:
        with open(file) as line:
            count = 0
            for text in line:
                count += 1
                if len(args.keywords) == 1:
                    if not args.hid:
                        if args.keywords[0] in text.lower():
                            str_text = ''
                            key = ''
                            arr = ''
                            for j in args.keywords[0]:
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

                elif len(args.keywords) == 2:
                    if not args.key:
                        if args.keywords[0] in text.lower():
                            if args.keywords[1] == file:
                                str_text = ''
                                key = ''
                                arr = ''
                                for j in args.keywords[0]:
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
                                print(args.keywords[1])
                                print(a + ":" + str_text.replace(arr,arr1))
                            if args.keywords[1] == ".":
                                str_text = ''
                                key = ''
                                arr = ''
                                for j in args.keywords[0]:
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
                    if args.key:
                        if args.keywords[0] in text and args.keywords[1] == file:
                            str_text = ''
                            key = ""
                            arr = ''
                            for j in args.keywords[0]:
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
                            print(args.keywords[1])
                            print(a + ":" + str_text.replace(arr,arr1))

    for files in filenames:
        with open(files) as lines:
            count = 0
            for texts in lines:
                count += 1
                if args.hid and len(args.keywords) == 1:
                    if args.keywords[0] in texts.lower():
                        str_text = ''
                        key = ''
                        arr = ''
                        for j in args.keywords[0]:
                            key += j
                        for i in range(len(texts)):
                            arr1 = ''
                            co = 0
                            if texts[i].lower() == key[0].lower():
                                arr = texts[i]
                                while len(arr) < len(key):
                                    co += 1
                                    arr += texts[i+co]
                            if arr.lower() == key.lower():
                                arr1 += '\033[30;43m' + arr + '\033[0m' + ''
                            str_text += texts[i] + ''
                        a = '\033[1;33m' + str(count) + '\033[0m'
                        print(a + ":" + str_text.replace(arr,arr1))
