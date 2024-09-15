# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:11:21 2024

@author: Admin
"""

#Viết lệnh kiểm tra giá trị nhập vào từ bàn phím thỏa điều kiện thuộc
#[-99; 99]. Nếu không khỏa bắt người dùng nhập lại đến khi nào
#khỏa điều kiện.
N=int(input("Nhập vào một giá trị thuộc [-99;99]: "))
while N<-99 or N>99:
    N=int(input("Mời bạn nhập lại:"))
print("Giá trị đã nhập: ",N)
    