# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:43:18 2024

@author: TranThiNgocNi_23712091
"""

a=int(input("Nhập vào số a: "))
b=int(input("Nhập vào số b: "))
c=int(input("Nhập vào số c: "))
#Giả định số lớn nhất là a
solonnhat=a
if b>solonnhat:
    solonnhat=b
if c>solonnhat:
    solonnhat=c
print("Vậy số lớn nhất là: ",solonnhat)