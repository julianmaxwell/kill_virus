__author__ = "boss"
__date__ = '2022/8/13 15:17'
import os
import time
import shutil
import subprocess
import sys
import sys
# sys.path.insert(0, r"d:\pyqt5_project_test\venv")
sys.path.insert(0, r" d:\python39\lib\site-packages ") #use this
# order = "D:\Python39\Scripts\pyinstaller -F D:\kill_virus\kill_program.py"
# order = "pyinstaller -F D:\kill_virus\kill_program.py"
# order = "pyinstaller -F kill_program.py"
order = "pyinstaller -F kill_program.py"
# order2 = "pip uninstall pyinstaller"
order2 = "pip install pyinstaller"
# order2 = "pip install upgrade"
# order_s = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="D:\kill_virus")
shutil.copy("kill_program.py", 'D:\Python39\Scripts\kill_program.py')
# shutil.copy("test2.py", r'D:\Python39\Scripts\test2.py')

order_s = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, cwd="D:\Python39\Scripts")
mm =order_s.stderr

out, err = order_s.communicate()
print(out.decode("gbk"))


print("err", err.decode("gbk"))

# order_s.stdin.write(b"y")
print("y input is ok")

shutil.copytree(r"D:\Python39\Scripts\dist", "D:\kill_virus\dist", dirs_exist_ok=True)

