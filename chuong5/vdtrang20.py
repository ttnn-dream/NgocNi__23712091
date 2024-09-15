# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:24:28 2024

@author: Admin
"""

count=0
n=int(input("Nhập vào số lần cần lặp: "))
while (count<n):
    print("Lần lặp thứ: ",count+1, "\t Biến đếm: ",count)
    count=count+1
else:
    print("\n Thực hiện lệnh trong else, do: ",
          "\ncount= ",count, "\nn= ",n,
          "\nbool(count<n)= ",bool(count<n))
    