import os
from datetime import datetime
import pandas as pd
import glob
from janome.tokenizer import Tokenizer

# pandasにてCSVファイルからFAX番号を抽出
df = pd.read_csv('C:/Users/OSAKACL27/Desktop/before/sample.csv', sep=',')
list_sample = df['FAX'].to_list()
print(list_sample)

# glob.globで指定のフォルダ内のファイル名を抽出、basenameにて拡張子を外す
for f in glob.glob('C:/Users/OSAKACL27/Desktop/before/*.pdf'):
    basename_without_ext = os.path.splitext(os.path.basename(f))[0]
    print(basename_without_ext[0:10])

# if A in B にてBのリスト内にファイル:Aが含まれているか確認。合致したものについては後方に名前を追記
# 変数後の[]にて、FAX番号のみ文字列にて抽出
if basename_without_ext[0:10] in list_sample:
    print('true')
    path = 'C:/Users/OSAKACL27/Desktop/before'
    os.rename(f,os.path.join(path,basename_without_ext + "_森野.pdf"))
else:
    print('一覧とFAX番号が一致しませんでした。')
  
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
