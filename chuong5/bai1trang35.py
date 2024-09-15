# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:30:42 2024

@author: Admin
"""
#Từ một chuỗi str_input được nhập vào từ bàn phím. Hãy viết lệnh thực hiện các chức năng sau:
#Ø Tính độ dài chuỗi.
#Ø Đếm và in các ký tự đặc biệt: ! @ # $ % ^ & * ( ) - = + . /
#Ø Đếm và in các ký tự chữ cái từ [a-z]
#Ø Đếm và in các ký tự chữ số từ [0-9]
#Ø Đếm và in các ký tự chữ [A-Z]

chuoi=input("Nhập vào một chuỗi: ")
dodai=len(chuoi)
print("Độ dài của chuỗi: ",dodai)

kytu="! @ # $ % ^ & * ( ) - = + . /"
kq=sum(1 for i in chuoi if i in kytu)
print("Số các ký tự đặt biệt là: ",kq)

a_z=sum(1 for i in chuoi if i.islower())
print("Các ký tự từ [a-z] là:", a_z)

khong_chin = sum(1 for i in chuoi if i.isdigit())
print("Các ký tự chữ số từ [0-9]: ",khong_chin)

A_Z=sum(1 for i in chuoi if i.isupper())
print("Các ký tự chữ [A-Z]: ",A_Z)


