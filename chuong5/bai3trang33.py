# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:25:32 2024

@author: Admin
"""

#Người dùng nhập một giá trị nguyên n từ bàn phím, hãy viết
#chương trình để tạo ra một dict chứa các phần tử theo cấu trúc sau:
#i : i^i
#• i là số nguyên từ 1 đến n (bao gồm cả 1 và n)
#• In ra dict vừa tạo.
n=int(input("Nhập vào một giá trị nguyên: "))
dictt={i:i**i for i in range(1,n+1)}
print(dictt)
