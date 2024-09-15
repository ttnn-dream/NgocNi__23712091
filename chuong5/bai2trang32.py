# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:21:51 2024

@author: Admin
"""

#Viết chương trình tạo một danh sách tự động các số chẵn nguyên
#từ 2020 đến 3838.
#1. Tạo danh sách các số chia hết cho 9 từ danh sách thu được.
#2. Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng 1 tab.
danhsach=[i for i in range(2020,3838) if i%2==0 and i%9==0 ]
ketqua="\t".join(map(str, danhsach))
print(ketqua)
