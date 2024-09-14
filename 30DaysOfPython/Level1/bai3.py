# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:59:19 2024

@author: Admin
"""

#Dùng vòng lặp để vẽ hình số 1.
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()
    
i=0
while i<8:
    j=0
    while j<8:
        print("#",end=" ")
        j+=1
    print()
    i+=1
    