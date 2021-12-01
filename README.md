- 業務の効率化で使用するプログラムです。

- 用途 1.既存のファイル名をリネームする。  
  2.リネームしたファイルを所定のフォルダに移動させる。


import os
import csv
from datetime import datetime
import time
import argparse
import pandas as pd
import pathlib
import glob
from janome.tokenizer import Tokenizer

# pandasにてCSVファイルからFAX番号を抽出
df = pd.read_csv('C:/Users/OSAKACL27/Desktop/before/sample.csv', sep=',')
list_sample = df['FAX'].to_list()
print(list_sample)

# glob.globで指定のフォルダ内のファイル名を抽出、basenameにて拡張子を外す
for f in glob.glob('C:/Users/OSAKACL27/Desktop/before/*pdf'):
    basename_without_ext = os.path.splitext(os.path.basename(f))[0]
    print(basename_without_ext)

# if A in B にてB内にAが含まれているか確認
if basename_without_ext in list_sample:
    print('true')
else:
    print('false')
  
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
