# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:31:22 2024

@author: TranThiNgocNi_23712091
"""

soxe=input("Nhập vào số xe của bạn: ")
tong=sum(int(chuso) for (chuso) in (soxe))
hangchuc=tong//10
hangdonvi=tong%10
sonut=hangchuc+hangdonvi
print(f"Vậy xe có {sonut} nút")