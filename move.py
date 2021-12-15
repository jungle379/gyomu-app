import os
import pandas as pd
import glob
import schedule
from time import sleep
from datetime import datetime,date
import shutil

# ここから実行内容

def task():
    # pandasにてCSVファイルからFAX番号を抽出
    df = pd.read_csv('//***/**/scanfile/before/sample.csv', sep=',', dtype=object)
    list_sample = df['FAX'].to_list()
    # print(list_sample)

    # glob.globで指定のフォルダ内のファイル名を抽出、basenameにて拡張子を外す
    for f in glob.glob('//***/**/scanfile/before/*.pdf'):
        # 拡張子の切り取り
        basename_without_ext = os.path.splitext(os.path.basename(f))[0]
        b = basename_without_ext[0:10]

        # if A in B にてB内にAが含まれているか確認。合致したものについては担当の名前を追記
        # 変数後の[]にて、FAX番号のみ文字列にて抽出
        if b in list_sample:
            print('true')
            path = '//***/**/scanfile/before/'
            os.rename(f,os.path.join(path,"山田_" + basename_without_ext + ".pdf" ))
        else:
            print('一覧とFAX番号が一致しませんでした。')

    # 「名前_」を抽出してフォルダ間を移動させる
    directory_pdf = "//***/**/scanfile/before/山田_*.pdf"
    for path in glob.glob(directory_pdf):
        print( path )
        
    sourcepath='//***/**/scanfile/before/'
    source = os.listdir('//***/**/scanfile/before/')
    destinationpath = '//***/**/scanfile/after/'
    
    for files in source:
        if files.startswith('山田_'):
            shutil.move(os.path.join(sourcepath,files), os.path.join(destinationpath,files))

# ここまで自動で起動する内容

# 周期の設定値
schedule.every(30).seconds.do(task)

year = date.today().year
month = date.today().month
hour = 19
minute = 0
second = 0
set_until_time = datetime(year,month,date.today().day,hour,minute,second)

while datetime.now() < set_until_time:
    schedule.run_pending()
    sleep(1)

