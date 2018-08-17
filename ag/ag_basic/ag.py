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
                            for j in args.keywords:
                                key += j
                            for i in range(len(text)):
                                arr = ''
                                co = 0
                                
                            #     if text[i] == key[0]:
                            #         arr = text[i]
                            #         while len(arr) < len(key):
                            #             co += 1
                            #             arr += text[i+co]
                            #     if arr == key:
                            #         str_text += '\033[30;43m' + arr + '\033[0m' + ''
                            #     else:
                            #         str_text += text[i] + ''
                            # a = '\033[1;33m' + str(count) + '\033[0m'
                            # print(a + ":" + str_text)
                if not args.key:
                    if args.keywords in text.lower():
                        if args.file == file:
                            str_text = ''
                            key = set([])
                            for i in range(len(text)):
                                for j in args.keywords:
                                    key.add(j)
                                if text[i].lower() in key:
                                    str_text += '\033[30;43m' + text[i] + '\033[0m' + ''
                                else:
                                    str_text += text[i] + ''
                            a = '\033[1;33m' + str(count) + '\033[0m'
                            print(a + ":" + str_text)
