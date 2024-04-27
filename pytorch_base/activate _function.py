# -*- coding:utf-8 -*-
# /usr/bin/python
'''
------------------------------------------------------------
@File Name      :  activate _function.py
@Run Script     :  python  activate _function.py
@Envs           :  pip install 
------------------------------------------------------------
@Author         :  yanerrol,13075851954
@CodeStyle      :  standard, readable, maintainable and portable!
------------------------------------------------------------
@Description     PyCharm
    The system service manages hostname.
------------------------------------------------------------
@History
    v1.0    yanerrol,  2024/4/26 23:21
------------------------------------------------------------
'''
__author__ = 'yanerrol'

import torch

elu = torch.nn.ELU()
input  = torch.randn(2)
output = elu(input)
print(input,output)

# hardshrink
m = torch.nn.Hardshrink()
input  = torch.randn(2)
output = m(input)
print(input,output)

# hardsigmoid
m = torch.nn.Hardsigmoid()
input  = torch.randn(2)
output = m(input)
print(input,output)

# hardtanh
m = torch.nn.Hardtanh(-2,2)
input  = torch.randn(2)
output = m(input)
print(input,output)

# hardswish
m = torch.nn.Hardswish()
input  = torch.randn(2)
output = m(input)
print(input,output)

# LeakyReLU
m = torch.nn.LeakyReLU(0.1)
input  = torch.randn(2)
output = m(input)
print(input,output)

# logSigmoid
m = torch.nn.LogSigmoid()
input  = torch.randn(2)
output = m(input)
print(input,output)

# PreLU
m = torch.nn.PReLU()
input  = torch.randn(2)
output = m(input)
print(input,output)

# ReLU
m = torch.nn.ReLU()
input  = torch.randn(2)
output = m(input)
print(input,output)

# RReLU
m = torch.nn.RReLU()
input  = torch.randn(2)
output = m(input)
print(input,output)

# Sigmoid
m = torch.nn.Sigmoid()
input  = torch.randn(2)
output = m(input)
print(input,output)

# Tanh
m = torch.nn.Tanh()
input  = torch.randn(2)
output = m(input)
print(input,output)

# Softmax
m = torch.nn.Softmax(dim=1)
input  = torch.tensor([-0.9])
print(input)
output = m(input)
print(input,output)

# Softmin
m = torch.nn.Softmin(dim=1)
input  = torch.tensor([-0.9])
print(input)
output = m(input)
print(input,output)


