# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 00:13:11 2024

@author: TranThiNgocNi_23712091
"""

#Câu a
a=int(input("Nhập vào số a: "))
b=int(input("Nhập vào số b: "))
c=int(input("Nhập vào số c: "))
if a>b:
    a,b=b,a
elif a>c:
    a,c=c,a
elif b>c:
    b,c=c,b
print("Các số từ nhỏ đến lớn: ", a,b,c)
    
#Câu b
N=int(input("Nhập vào số nguyên N: "))
digits=[int(d) for d in str(N)]
digits.sort()
ketqua=int(''.join(map(str,digits)))
print("Kết quả là: ",ketqua)

    