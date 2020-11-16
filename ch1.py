"""This chapter just introduces me to python and to numpy"""
from numpy import *

a = random.rand(4, 4)
m = mat(a)

print(a)
print(m*m.I)
print(m*m.I - eye(4))
