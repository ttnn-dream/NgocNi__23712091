# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 00:07:40 2024

@author: TranThiNgocNi_23712091
"""

gio=int(input("Nhập vào giờ: "))
phut=int(input("Nhập vào phút: "))
giay=int(input("Nhập vào giây: "))
if 0<=gio<=23 and 0<=phut<=59 and 0<=giay<=59:
    print("Giờ hợp lệ")
else:
    print("Không hợp lệ")