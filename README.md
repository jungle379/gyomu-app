- 業務の効率化で使用するプログラムです。（内容などは完成後更新予定）

import os
import csv
from datetime import datetime
import time
import argparse
import pandas as pd
import pathlib
import glob

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

# pandasにてcsvファイルからFAX番号を抽出
df = pd.read_csv('C:/Users/OSAKACL27/Desktop/before/sample.csv', sep=',')
df.head(3)
print(df.head(3))

# pathlibにてサーバ上のPDFファイルのファイル名を抽出
p_temp = pathlib.Path('C:/Users/OSAKACL27/Desktop/before').glob('*pdf')
for p in p_temp:
    print(p.name)

# 上記で抽出したデータを比較し、合致したデータのみをリネームする


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

# # ログ採取
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
