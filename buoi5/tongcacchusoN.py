# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:21:18 2024

@author: TranThiNgocNi_23712091
"""

N=int(input("Nhập vào số nguyên dương có 2 chữ số: "))
if 10<=N<=99:
    hangchuc=N//10
    hangdonvi=N%10
    tong=hangchuc+hangdonvi
    print("Tổng các chữ số của N là: ",tong)