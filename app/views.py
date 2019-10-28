#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import time
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from RSManager.settings import Resource_DIRS, Download_DIRS
from django.http import FileResponse
from app.conf import Dirs_Num
from app.utils.tree import show_dir, show_left_tree
from app.utils.psd import psd2png
from app.utils.zip import SuperZip
from app.utils.handle import ajax_url_handle
from app.utils.response import BaseResponse


def index(request):
    tree_dict = show_left_tree()
    return render(request, 'base/index.html', {'left_dirs': tree_dict})


@csrf_exempt
def show_multilayer_dir(request, **kwargs):
    dir_name_list = ['dir' + str(i) for i in range(1, int(Dirs_Num))]
    abs_path_list = []
    for item in dir_name_list:
        try:
            if kwargs[item]:
                abs_path_list.append(kwargs[item])
        except Exception as e:
            pass
    str_tmp = os.sep
    cur_dir = str_tmp.join(abs_path_list)
    tree_dict = show_left_tree()
    ret_dict = show_dir(abs_path_list)
    d_dict = {}
    for n in range(len(abs_path_list)):
        d_dict[str(n)] = abs_path_list[n]
    return render(request, 'photo/mult_dir_pictures.html',
                  {
                      'left_dirs': tree_dict,
                      'dir_data': ret_dict['dirs'],
                      'file_data': ret_dict['files'],
                      'pic_data': ret_dict['素材资源'],
                      'psd_data': ret_dict['psd'],
                      'current_dir': cur_dir,
                      'bread_tree': d_dict,
                  })


@csrf_exempt
def zip_download(request):
    response = BaseResponse()
    files_list, url = [], ''
    if request.method == "POST":
        files_list = request.POST.getlist('names[]', None)
        url = request.POST.get('url', None)
    if files_list and url:
        down_abs_dir = os.path.join(Resource_DIRS, str(url))  # 需要下载的文件所在目录
        zipfilename = str(time.time()) + '.zip'   # 最终zip包的名称，自定义
        abs_down_path = os.path.join(Download_DIRS, zipfilename)  # 生成zip包的绝对路径
        zipfile = SuperZip()
        zip_ret = zipfile.zip_file_dir(abs_down_path, down_abs_dir, files_list)
        if zip_ret:
            response.data = zipfilename
            return HttpResponse(json.dumps(response.__dict__))
        else:
            response.status = False
    else:
        response.status = False
        return HttpResponse(json.dumps(response.__dict__))


@csrf_exempt
def downloadfile(request, zname):
    abs_down_path = os.path.join(Download_DIRS, zname)
    file = open(abs_down_path, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(zname)
    return response


@csrf_exempt
def psd_to_png(request):
    response = BaseResponse()
    files_list, url = [], ''
    if request.method == "POST":
        files_list = request.POST.getlist('names[]', None)
        url = request.POST.get('url', None)
    if files_list and url:
        down_abs_dir = os.path.join(Resource_DIRS, str(url))  # 需要转换文件所在目录
        try:
            psd2png(down_abs_dir, files_list)
        except Exception as e:
            response.status = False
            response.message = 'Error psd_to_png'
    return HttpResponse(json.dumps(response.__dict__))


@csrf_exempt
def web_change_dir(request):
    url, dirname, dirid = '', '', ''
    response = BaseResponse()
    if request.method == "POST":
        url = request.POST.get('url', None)
        dirname = request.POST.get('dir', None)
        dirid = request.POST.get('id', None)
    if url and dirname:
        ret = ajax_url_handle(str(url), str(dirname), dirid)
    elif url and dirid:
        ret = ajax_url_handle(str(url), dirname, int(dirid))
    else:
        ret = None
    if ret:
        response.data = ret
    else:
        response.status = False
    return HttpResponse(json.dumps(response.__dict__))






