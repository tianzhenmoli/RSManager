#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from psd_tools import PSDImage


def psd2png(abs_dir_path, file_list):
    """
        psd文件转化为png图片
    :param abs_dir_path: psd文件所在绝对路径
    :param file_list: 一个包含psd文件名的列表，可以处理多个psd文件转化
    :return: 成功返回True, 失败False
    """
    if abs_dir_path and file_list:
        if os.path.isdir(abs_dir_path):
            os.chdir(abs_dir_path)
            for psd in file_list:
                str_tmp = psd + '.png'
                try:
                    psd_image = PSDImage.open(psd)
                    image = psd_image.compose()
                    image.save(str_tmp)
                except Exception as e:
                    print('Error: psd2png,', e)
                    return False
            return True
        else:
            print('psd2png: 目录不存在 --', abs_dir_path)
    else:
        print('psd2png: 函数需要两个非空参数，但获取了空值')