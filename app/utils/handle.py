#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from RSManager.settings import Resource_DIRS


def ajax_url_handle(url, dirname, dirid):
    """
    处理ajax 传递的url，生成相应的url
    :param url: ajax 页面当前绝对路径
    :param dirname: 要进入目录的名称
    :param dirid: 要进入目录所在页面当前绝对路径的id值
    :return: 用于ajax 前端跳转的url
    """
    sep_str = os.sep
    url_tmp_list = url.split(sep_str)
    url_list = []
    for i in url_tmp_list:
        if i:
            url_list.append(str(i))
    if dirname:
        url_list.append(str(dirname))
    if dirid:
        nid = int(dirid) + 1
        url_list = url_list[:nid]
    abs_tmp_path = sep_str.join(url_list)
    local_abs_path = os.path.join(Resource_DIRS, abs_tmp_path)
    if os.path.isdir(local_abs_path):
        url_path_tmp = '/'.join(url_list)
        url_path = '/resources/' + url_path_tmp
        return url_path
    else:
        print('ajax_url : not dir')
        return None




