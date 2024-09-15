# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:14:04 2024

@author: Admin
"""

#Tạo một danh sách tự động các số chẵn nguyên và chia hết cho 5
#từ 2018 đến 2828
danhsach=[i for i in range(2018,2828) if i%2==0 and i%5==0 ]
print(danhsach)