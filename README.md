- 業務の効率化で使用するプログラムです。

- 用途  
  1.既存のファイル名をリネームする。  
  2.リネームしたファイルを所定のフォルダに移動させる。
# import os
# import glob
# import shutil

# def file_move(move_path):
#   # ()内で\\**の手前までを変える(絶対パス)
#   for x in glob.iglob('C:\\Users\\OSAKACL27\\Desktop\\before\\**', recursive=True):
#     for y in glob.iglob(move_path+'**', recursive=True):
#       # rfind('')内を移動させるファイル名に変更する
#       if os.path.isfile(x) and x[x.rfind('\\')+1:x.rfind('')] == y[y.rfind('\\')+1:y.rfind('')]:
#         shutil.move(x, move_path+x[x.rfind('\\')+1:])
#         print(x, 'を 【', move_path, '】へ移動しました')

# # ()内のパスを変更する(絶対パス)
# file_move('C:\\Users\\OSAKACL27\\Desktop\\after\\')


# def file_move2(move_path2):
#   for x in glob.iglob('C:\\Users\\OSAKACL27\\Desktop\\hoge\\**', recursive=True):
#     for y in glob.iglob(move_path2+'**', recursive=True):
#       if os.path.isfile(x) and x[x.rfind('\\')+1:x.rfind('例題')] == y[y.rfind('\\')+1:y.rfind('例題')]:
#         shutil.move(x, move_path2+x[x.rfind('\\')+1:])
#         print(x, 'を 【', move_path2, '】へ移動しました')

# file_move2('C:\\Users\\OSAKACL27\\Desktop\\huga\\')


import shutil, glob, os

#Prints all text files in directory
directory_pdf = "//LANDISK-A52D12/share/scanfile/before/山田_*.pdf"
for path in glob.glob(directory_pdf):
    print( path )
    
sourcepath='//LANDISK-A52D12/share/scanfile/before/'
source = os.listdir('//LANDISK-A52D12/share/scanfile/before/')
destinationpath = '//LANDISK-A52D12/share/scanfile/after/'
for files in source:
    if files.startswith('山田_'):
        shutil.move(os.path.join(sourcepath,files), os.path.join(destinationpath,files))
    # else:
    #     print('No files with .txt extension to move!')



input(
'''
データの移動が完了しました。Enterキーを押してください
'''
)
