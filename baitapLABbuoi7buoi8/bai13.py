# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:13:31 2024

@author: TranThiNgocNi_23712091
"""

ngay=int(input("Nhập ngày: "))
thang=int(input("Nhập tháng: "))
nam=int(input("Nhập năm: "))
#a) Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/1990)
print(f"{ngay}/{thang}/{nam}")
#b) Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/90)
print(f"{ngay}/{thang}/{str(nam)[-2:]}")
#c) Năm/tháng/ngày (Nhập 20 8 1990 thì xuất 1990/8/20)
print("{nam}/{thang}/{ngay}")



