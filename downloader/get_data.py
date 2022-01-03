"""
功能：根据 csv 文件下载数据
语法：
"""
import urllib.request
import os
import sys

def download_and_extract(filepath, save_dir):
    """根据给定的URL地址下载文件

    Parameter:
        filepath: list 文件的URL路径地址
        save_dir: str  保存路径
    Return:
        None
    """
    for url, index in zip(filepath, range(len(filepath))):
        filename = url.split('/')[-1]
        save_path = os.path.join(save_dir, filename)
        urllib.request.urlretrieve(url, save_path)
        sys.stdout.write('\r>> Downloading %.1f%%' % (float(index + 1) / float(len(filepath)) * 100.0))
        sys.stdout.flush()
    print('\nSuccessfully downloaded')

import csv
with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    for row in reader:
        download_and_extract([row[2]], '.')
        # print(row)