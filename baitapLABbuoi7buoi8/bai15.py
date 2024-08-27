# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:22:48 2024

@author: TranThiNgocNi_23712091
"""
a=float(input("Nhập vào số a: "))
b=float(input("Nhập vào só b: "))
bt1=(a+b)/(a**1/3+b**1/3)
bt2=(a*b)**1/3
bt3=a**1/3 
bt4=b**1/3
ketqua=(bt1-bt2)/(bt3-bt4)**2
print("Kết quả của biểu thức là: ",ketqua)
