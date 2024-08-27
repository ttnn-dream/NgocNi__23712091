# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:58:51 2024

@author: TranThiNgocNi_23712091
"""

#Giải và biện luận phương trình bậc nhất: ax + b = 0
a=float(input("Nhập vào số a: "))
b=float(input("Nhập vào số b: "))
if a==0 and b==0:
    print("Phương trình có vô số nghiệm")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm")
else:
    x=-b/a
    print("Phương trình có nghiệm: ",x)