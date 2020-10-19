import pandas as pd
import glob
import os
import numpy as np

all_files = glob.glob(os.path.join("*.csv"))#遍历当前目录下的所有以.csv结尾的文件
all_data_frame = []
row_count = 0
for file in all_files:
    data_frame = pd.read_csv(file,encoding='ISO-8859-1')
    all_data_frame.append(data_frame)
data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=True, sort=True)
data_frame_concat.to_csv("rollingsales_newyork.csv", index=False, encoding="utf-8")
