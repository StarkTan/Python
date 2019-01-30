"""
将目标文件夹中的py文件编译成pyc文件
"""
import os
import shutil
import compileall


def do_change(path):
    for i in os.listdir(path):
        cur_path = os.path.join(path, i)
        if i == '__pycache__':
            for j in os.listdir(cur_path):
                if j.endswith('pyc'):
                    shutil.move(os.path.join(cur_path, j), os.path.join(path, j.replace('.cpython-36', '')))
                else:
                    os.remove(os.path.join(cur_path, j))
            os.removedirs(cur_path)
        elif i.endswith('py') and os.path.isfile(cur_path):
            os.remove(cur_path)
        elif not os.path.isfile(cur_path):
            do_change(cur_path)
        else:
            continue


dir_path = os.path.join(os.getcwd(), "test\\compile")

if os.path.exists(os.path.join(dir_path, 'test.pyc')):
    os.remove(os.path.join(dir_path, 'test.pyc'))

# 创建测试文件
open(os.path.join(dir_path, 'test.py'), 'w').close()
# 编译文件夹下的所有py文件
compileall.compile_dir(dir_path)
do_change(dir_path)
print(os.path.exists(os.path.join(dir_path, 'test.pyc')))
