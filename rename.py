import os
import pandas as pd
import glob

# pandasにてCSVファイルからFAX番号を抽出
# ''間には絶対パス＋読み込むcsvファイルのファイル名を入れる
df = pd.read_csv('//LANDISK-A52D12/share/scanfile/before/sample.csv', sep=',', dtype=object)
list_sample = df['FAX'].to_list()
print(list_sample)

# glob.globで指定のフォルダ内のファイル名を抽出、basenameにて拡張子を外す
for f in glob.glob('//LANDISK-A52D12/share/scanfile/before/*.pdf'):
    # 拡張子の切り取り
    basename_without_ext = os.path.splitext(os.path.basename(f))[0]
    b = basename_without_ext[0:10]

    # if A in B にてB内にAが含まれているか確認。合致したものについては担当の名前を追記
    # 変数後の[]にて、FAX番号のみ文字列にて抽出
    if b in list_sample:
        print('true')
        path = '//LANDISK-A52D12/share/scanfile/before/'
        os.rename(f,os.path.join(path,basename_without_ext + "_山田.pdf"))
    else:
        print('一覧とFAX番号が一致しませんでした。')
