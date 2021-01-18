import os
import time
import sys
import warnings
warnings.filterwarnings("ignore")


def play(txtPath, FPS=10):
    files = os.listdir(txtPath)   # 读入文件夹
    num_png = len(files) -1
    for txt_count in range(num_png):
        os.system('cat ' + txtPath + '/' +str(txt_count) + '.txt')
        time.sleep(1.0/FPS)

path = sys.argv[1]
FPS = float(sys.argv[2])
play(path, FPS)