import os
import pandas as pd
import glob

# pandasにてCSVファイルからFAX番号を抽出
df = pd.read_csv('/Users/morinohiroki/Desktop/test/sample.csv', sep=',', dtype=object)
list_sample = df['FAX'].to_list()
print(list_sample)

# glob.globで指定のフォルダ内のファイル名を抽出、basenameにて拡張子を外す
for f in glob.glob('/Users/morinohiroki/Desktop/test/*.jpg'):
    # 拡張子の切り取り
    basename_without_ext = os.path.splitext(os.path.basename(f))[0]
    b = basename_without_ext[0:10]
    print(b)

# if A in B にてB内にAが含まれているか確認。合致したものについては担当の名前を追記
# 変数後の[]にて、FAX番号のみ文字列にて抽出
if basename_without_ext[1:10] in list_sample:
    print('true')
    path = '/Users/morinohiroki/Desktop/test/'
    os.rename(f,os.path.join(path,basename_without_ext + "_山田.pdf"))
else:
    print('一覧とFAX番号が一致しませんでした。')
