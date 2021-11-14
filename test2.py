import pathlib
import shutil
import datetime

#今日の日付
yyyymmdd = datetime.date.today().strftime('%Y%m%d')
#移動元フォルダから条件に一致するファイル名を取得
#リストで受け取りたいのでキャストする
p_tmp = list(pathlib.Path('移動元フォルダ').glob(f'{yyyymmdd}*.csv'))
'''リスト化するところを ↑ に修正
p_tmp = pathlib.Path('移動元フォルダ').glob(f'{yyyymmdd}*.csv')
p = [p for p in p_tmp]
''' 
dest = '移動先フォルダ'
#ファイル移動
for source in p_tmp:
    shutil.move(str(source), dest) 