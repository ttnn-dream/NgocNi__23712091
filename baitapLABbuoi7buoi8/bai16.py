# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:26:48 2024

@author: TranThiNgocNi_23712091
"""

gio=int(input("Nhập giờ: "))
phut=int(input("Nhập phút: "))
giay=int(input("Nhập giây: "))
tonggiay=gio*3600+ phut*60+giay
print("Tổng giây tính được là: ",tonggiay)