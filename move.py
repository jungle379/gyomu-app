import os
import glob
import shutil

def file_move(move_path):
  for x in glob.iglob('C:\\移動元パス\\**', recursive=True):
    for y in glob.iglob(move_path+'**', recursive=True):
      if os.path.isfile(x) and x[x.rfind('\\')+1:x.rfind(' 第')] == y[y.rfind('\\')+1:y.rfind(' 第')]:
        shutil.move(x, move_path+x[x.rfind('\\')+1:])
        print(x, 'を 【', move_path, '】へ移動しました')

file_move('C:\\移動先パス1\\')
file_move('C:\\移動先パス2\\')

input(
'''
Enterキーを押してください
'''
)
