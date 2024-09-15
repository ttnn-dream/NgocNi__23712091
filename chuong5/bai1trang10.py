# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:13:55 2024

@author: Admin
"""

#Viết chương trình tính giai thừa của một số cho trước n (nguyên
#dương) được nhập từ bàn phím.
#S = n! = 1.2.3...n
n=int(input("Nhập vào một số nguyên dương: "))
S=1
for i in range(1,n+1):
    S*=i
print("Giai thừa của n là: ",S)
