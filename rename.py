import os
import pandas as pd
import glob

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