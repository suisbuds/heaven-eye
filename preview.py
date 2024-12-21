import os
import subprocess

# 生成 home.py 文件
subprocess.run(["pyside6-uic", "home.ui", "-o", "ui/home.py"], check=True)

# 运行 main.py 文件
subprocess.run(["python3", "main.py"], check=True)