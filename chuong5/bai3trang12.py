# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:25:47 2024

@author: Admin
"""

#Viết chương trình có thể tạo danh sách:
#• Số lượng các phần tử được chọn ngẫu nhiên từ 20 đến 30.
#• Các giá trị bình phương của các số thực được chọn ngẫu nhiên
#từ 18 đến 99.

import random
r1=random.randint(20,30)
binhphuong=[random.uniform(18, 99)**2 for _ in range(r1)]
print(binhphuong)
