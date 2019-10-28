#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import zipfile


class SuperZip(object):

    def zip_file_dir(self, zipname, abs_dir, file_dir_list):
        """
        压缩目录和文件，同时压缩目录和文件，也可以仅为目录或文件
        :param zipname: 压缩后生成的压缩包名，绝对路径
        :param abs_dir:
        :param file_dir_list:
        :return:
        """
        if zipname and abs_dir and file_dir_list:
            if os.path.isdir(abs_dir):
                os.chdir(abs_dir)
                filelist = []
                for item in file_dir_list:
                    if os.path.isfile(item):
                        filelist.append(item)
                    else:
                        for root_path, dirs, files in os.walk(item):
                            for file_name in files:
                                filelist.append(os.path.join(root_path, file_name))
                try:
                    with zipfile.ZipFile(zipname, 'w') as f:
                        for i in filelist:
                            f.write(i)
                    return True
                except Exception as e:
                    print('Error:', e)
            else:
                print('create_zip_file args error')
        else:
            print('create_zip_file args error')

    def unzip_file(self, zipfile_abs_path, unzip_abs_path):
        """
        解压文件到指定目录，目录不存在则创建，重复文件直接覆盖
        :param zipfile_abs_path: 压缩包的绝对路径
        :param unzip_abs_path: 解压目录的绝对路径
        :return: True or False
        """
        if os.path.exists(zipfile_abs_path):
            if not os.path.exists(unzip_abs_path):
                os.makedev(unzip_abs_path, 755)
            try:
                un_zip_obj = zipfile.ZipFile(zipfile_abs_path)
                un_zip_obj.extractall(path=unzip_abs_path)
                un_zip_obj.close()
                return True
            except Exception as e:
                print('Error:', e)
        else:
            print('Error: zip_file_path not exists!')

    def test(self):
        print("Info: Custom ZipFile Class")


if __name__ == '__main__':
    obj = SuperZip()
    obj.test()


