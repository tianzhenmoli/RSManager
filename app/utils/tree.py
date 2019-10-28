#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from RSManager.settings import Resource_DIRS
from app.conf import Pic_Types


def show_left_tree():
    """
    获取左侧列表目录
    :return: 目录名称列表
    """
    dir_data = []
    os.chdir(Resource_DIRS)
    for root, dirs, files in os.walk("."):
        dir_data = dirs
        break
    return dir_data


def show_dir(abs_path_list):
    """
    获取绝对路径目录下的所有文件名和目录名称
    :param abs_path_list: 有序列表中可以依序拼接为本地的目录结构
    :return: 一个包含所有文件类型的字典
    """
    ret_dict = {}
    str_tmp = os.sep
    abs_path = str_tmp.join(abs_path_list)
    if abs_path == 'root':
        file_dir = Resource_DIRS
    else:
        file_dir = os.path.join(Resource_DIRS, abs_path)
    try:
        os.chdir(file_dir)
        for root, dirs, files in os.walk('.'):
            ret_dict['dirs'] = dirs
            pic_list, file_list, psd_list = [], [], []
            for item in files:
                end_list = item.split('.')
                if end_list[-1] in Pic_Types:
                    pic_list.append(item)
                elif end_list[-1] == 'psd':
                    psd_list.append(item)
                else:
                    file_list.append(item)
            ret_dict['files'], ret_dict['素材资源'], ret_dict['psd'] = file_list, pic_list, psd_list
            break
    except Exception as e:
        print('Error:', e)
    return ret_dict




