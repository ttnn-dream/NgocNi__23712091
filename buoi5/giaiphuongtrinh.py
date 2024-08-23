# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:05:32 2024

@author: Admin
"""

import math

a=float(input("Nhập a: " ))
b=float(input("Nhập b: "))
bt1=math.sqrt(a)-math.sqrt(b)
bt2=a**(1/4)-b**(1/4)
bt3=math.sqrt(a)+(a*b)**(1/4)
bt4=a**(1/4)+b**(1/4)

ketqua=(bt1/bt2)-(bt3/bt4)
print("Kết quả của biểu thức là: ",ketqua)