
import os
import shutil
import compileall
path = 'J://pyc_test/api'
compileall.compile_dir(path)
def do_change(path):
    for i in os.listdir(path):
        cur_path = os.path.join(path, i)
        if i=='__pycache__':
            for j in os.listdir(cur_path):
                if j.endswith('pyc'):
                    shutil.move(os.path.join(cur_path, j), os.path.join(path, j.replace('.cpython-36', '')))
                else:
                    os.remove(os.path.join(cur_path, j))
            os.removedirs(cur_path)
        elif i.endswith('py') and os.path.isfile(cur_path) :
            os.remove(cur_path)
        elif not os.path.isfile(cur_path):
            do_change(cur_path)
do_change(path)

import sys
sys.exit()