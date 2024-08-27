# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:31:15 2024

@author: TranThiNgocNi_23712091
"""
from datetime import timedelta
gio1=int(input("Nhập giờ 1: "))
phut1=int(input("Nhập phút 1: "))
giay1=int(input("Nhập giây 1: "))

gio2=int(input("Nhập giờ 2: "))
phut2=int(input("Nhập phút 2: "))
giay2=int(input("Nhập phút 2: "))

time1=timedelta(hours=gio1, minutes=phut1, seconds=giay1)
time2=timedelta(hours=gio2, minutes=phut2, seconds=giay2)

cong2gio= time1+time2
print("Cộng hai giờ ta được: ",cong2gio)
tru2gio=time1- time2
print("Trừ hai giờ ta được: ",tru2gio)