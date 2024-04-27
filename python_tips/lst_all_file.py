# -*- coding:utf-8 -*-
# /usr/bin/python
'''
------------------------------------------------------------
@File Name      :  lst_all_file.py
@Run Script     :  python  lst_all_file.py
@Envs           :  pip install 
------------------------------------------------------------
@Author         :  yanerrol,13075851954
@CodeStyle      :  standard, readable, maintainable and portable!
------------------------------------------------------------
@Description     PyCharm
    The system service manages hostname.
------------------------------------------------------------
@History
    v1.0    yanerrol,  2024/4/27 09:51
------------------------------------------------------------
'''
__author__ = 'yanerrol'


import os
def get_all_file_path(root_dir):
    '''获取路径下所有的文件地址'''
    file_list = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file  not in  ".DS_Store":
                file_full_path = os.path.join(root,file)
                file_list.append(file_full_path)
    return file_list

if __name__=="__main__":
    print(get_all_file_path("../"))