import os
import csv
from datetime import datetime
import time
import argparse
import pandas as pd
import pathlib
import glob
from janome.tokenizer import Tokenizer

# 引数の定義
# parser = argparse.ArgumentParser()
# parser.add_argument('-d', '--directory', help='the directory of the files to \
# be renamed. optional - if not provided, the script will ask for input')
# parser.add_argument('-f', '--fileNameCSV', help='the CSV file of name changes. \
# optional - if not provided, the script will ask for input')
# parser.add_argument('-m', '--makeChanges', help='Enter "true" to if the script \
# should actually rename the files (otherwise, it will only create a log of the \
# expected file name changes). optional - if not provided, the script will to \
# "false"')
# args = parser.parse_args()

# pandasにてCSVファイルからFAX番号を抽出
df = pd.read_csv('C:/Users/OSAKACL27/Desktop/before/sample.csv', sep=',')
list_sample = df['tel'].to_list()
print(list_sample)
# df.head()
# print(df.head())

# os.listdirにてフォルダ内部のファイル名を抽出
path = "../before"
files = os.listdir(path)
print(files)

if list_sample in files:
    print('true')
else:
    print('false')

# pathlibにてサーバ上のPDFファイルのファイル名を抽出
# p_temp = os.path('C:/Users/OSAKACL27/Desktop/before').glob('*')
# for p in p_temp:
#     print(p.name)
# t = Tokenizer()
# for file in files:
#  for files in t.tokenize(file):
#      file.append(file.surface)
#      print(files)
    
# 上記で抽出したデータを比較し、合致したデータのみをリネームする
# if df in [p_temp]:
#     print("true")
# else:
#     print("false")
#     for f in files:
#      os.rename(f, os.path.join(path, '森野_' + os.path.basename(f)))
# else :
#     print(df.head)


# 条件分岐
# if args.directory:
#     directory = args.directory
# else:
#     directory = input('Enter the directory of the files to be renamed: ')
# if args.fileNameCSV:
#     fileNameCSV = args.fileNameCSV
# else:
#     fileNameCSV = input('Enter the CSV file of name changes \
#     (including \'.csv\'): ')
# if args.makeChanges:
#     makeChanges = args.makeChanges
# else:
#     makeChanges = input('Enter "true" to if the script should actually rename \
#     the files (otherwise, it will only create a log of the expected file name \
#     changes): ')

# ログ採取
# startTime = time.time()
# f = csv.writer(open('renameLog' + datetime.now().strftime('%Y-%m-%d %H.%M.%S')
#                + '.csv', 'w'))
# f.writerow(['oldFilename'] + ['newFilename'])
# for root, dirs, files in os.walk(directory, topdown=True):
#     for file in files:
#         with open(fileNameCSV) as csvfile:
#             reader = csv.DictReader(csvfile)
#             for row in reader:
#                 oldFilename = row['file']
#                 newFilename = row['newFile']
#                 if file == oldFilename:
#                     print(oldFilename)
#                     oldPath = os.path.join(root, file)
#                     newPath = os.path.join(root, newFilename)
#                     f.writerow([oldPath] + [newPath])
#                     if makeChanges == 'true':
#                         os.rename(oldPath, newPath)
#                     else:
#                         print('log of expected file name changes created only, \
#                         no files renamed')

# # ログファイル作成
# elapsedTime = time.time() - startTime
# m, s = divmod(elapsedTime, 60)
# h, m = divmod(m, 60)
# print('Total script run time: ', '%d:%02d:%02d' % (h, m, s))
