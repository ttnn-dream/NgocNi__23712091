# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:26:11 2024

@author: TranThiNgocNi_23712091
"""

gio=int(input("Nhập giờ: "))
phut=int(input("Nhập phút: "))
giay=int(input("Nhập giây: "))
if 0<=gio<23 and 0<=phut<60 and 0<=giay<60:
    tonggiay=3600*gio+60*phut+giay
    print("Tổng giây là: ",tonggiay)