# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:16:20 2024

@author: Admin
"""

#Sử dụng vòng lặp for để lặp từ 0 đến 100 và in ra tổng
#của tất cả các số chẵn và tổng của tất cả các số lẻ.
T_chan=0
T_le=0
for i in range(101):
    if i%2==0:
        T_chan+=i
    else:
        T_le+=i
print("Tổng các số chẵn là: ",T_chan)
print("Tổng các số lẻ là: ",T_le)
        
    