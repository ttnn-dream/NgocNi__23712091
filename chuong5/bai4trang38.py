# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:07:06 2024

@author: Admin
"""

import random
luachonnguoi=input("Mời bạn nhập lựa chọn: ")
luachonmay=random.choice(["Kéo","Búa","Bao"])
print(f"Máy chọn: {luachonmay}")
if luachonnguoi==luachonmay:
    print("Hòa")
elif (luachonnguoi=="Kéo" and luachonmay=="Bao") or\
    (luachonnguoi=="Búa" and luachonmay=="Kéo") or\
    (luachonnguoi=="Bao" and luachonmay=="Búa"):
        print("Người thắng")
else:
    print("Máy thắng")
    