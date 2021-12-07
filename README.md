- 業務の効率化で使用するプログラムです。

- 用途  
  1.既存のファイル名をリネームする。  
  2.リネームしたファイルを所定のフォルダに移動させる。
import os
import csv
import argparse
import pandas as pd
import pathlib
import glob

# pandasにてCSVファイルからFAX番号を抽出
df = pd.read_csv('C:/Users/OSAKACL27/Desktop/before/sample.csv', sep=',', dtype=object)
list_sample = df['FAX'].to_list()

# glob.globで指定のフォルダ内のファイル名を抽出、basenameにて拡張子を外す
for f in glob.glob('C:/Users/OSAKACL27/Desktop/before/*.pdf'):
    # 拡張子の切り取り
    basename_without_ext = os.path.splitext(os.path.basename(f))[0]
    b = basename_without_ext[0:10]
    l = list_sample

    l_even = [s for s in l if s.startswith(b)]


# if A in B にてB内にAが含まれているか確認。合致したものについては担当の名前を追記
# 変数後の[]にて、FAX番号のみ文字列にて抽出
# if basename_without_ext[0:10] in list_sample:
#     print('true')
# os.rename(f,os.path.join(path,basename_without_ext + "_森野.pdf"))
# else:
#     print('一覧とFAX番号が一致しませんでした。')
