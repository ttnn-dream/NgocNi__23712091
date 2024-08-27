# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:37:25 2024

@author: TranThiNgocNi_23712091
"""
a=int(input("Nhập vào số nguyên a: "))
b=int(input("Nhập vào số nguyên b: "))
c=int(input("Nhập vào số nguyên c: "))
d=int(input("Nhập vào số nguyên d: "))
#Giả định số nhỏ nhất là a
sonhonhat=a
if b<sonhonhat:
    sonhonhat=b
if c<sonhonhat:
    sonhonhat=c
if d<sonhonhat:
    sonhonhat=d
print("Vậy số nhỏ nhất là: ",sonhonhat)
