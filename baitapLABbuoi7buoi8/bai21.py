# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:54:26 2024

@author: TranThiNgocNi_23712091
"""

S=int(input("Nhập vào số bất kì: "))
so_chuoi={0:"Không",1:"Một",2:"Hai",3:"Ba",4:"Bốn",5:"Năm",6:"Sáu",
          7:"Bảy",8:"Tám", 9:"Chín"}
if 0<=S<=9 :
    print(so_chuoi[S])
else:
    print("Không đọc được")