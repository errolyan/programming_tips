# -*- coding:utf-8 -*-
# /usr/bin/python
'''
------------------------------------------------------------
@File Name      :  gpu_cpu
@Run Script     :  python  gpu_cpu
@Envs           :  pip install 
------------------------------------------------------------
@Author         :  yanerrol,13075851954
@CodeStyle      :  standard, readable, maintainable and portable!
------------------------------------------------------------
@Description     PyCharm
    The system service manages hostname.
------------------------------------------------------------
@History
    v1.0    yanerrol,  2024/4/26 23:16
------------------------------------------------------------
'''
__author__ = 'yanerrol'
import  torch
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

print(device)