# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:15:56 2024

@author: Admin
"""

#Viết lệnh kiểm tra giá trị nhập vào (phải là số thực) từ bàn phím
#thỏa điều kiện thuộc [-89.9; 88.8]. Nếu không khỏa bắt người dùng
#nhập lại đến khi nào khỏa điều kiện.
N=float(input("Nhập vào một số thực thuộc [-89.9;88.8]: "))
while N<-89.9 or N>88.8:
    N=float(input("Mời bạn nhập lại: "))
print("Giá trị bạn đã nhập là: ",N)
