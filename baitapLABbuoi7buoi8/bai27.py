# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 00:30:26 2024

@author: TranThiNgocNi_23712091
"""

#Hình chữ nhật
a=int(input("Nhập cạnh a: "))
b=int(input("Nhập cạnh b: "))
cv=(a+b)*2
print("Chu vi hình chữ nhật là: ",cv)
S=a*b
print("Diện tích hình chữ nhật là: ",S)

#Hình vuông
a=int(input("Nhập độ dài cạnh a: "))
cv=a*4
print("Chu vi hình vuông là: ",cv)
S=a*a
print("Diện tích hình vuông là: ",S)

#Hình tròn
import math
R=int(input("Nhập vào bán kính của hình: "))
cv=2*math.pi*R
print("Chu vi hình tròn là : ",cv)
S=math.pi*R**2
print("Diện tích hình tròn là: ",S)
