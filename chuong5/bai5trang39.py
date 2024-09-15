# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:10:52 2024

@author: Admin
"""

import random
#Khởi tạo số lượng người chơi ngẫu nhiên từ 8 đến 20
soluong=random.randint(8,20)
choices=["Kéo","Búa","Bao"]
#Tạo danh sách người chơi
players=[]
for i in range(soluong):
    player={'name': f"Người chơi {i+1} ",'choice':None}
    players.append(player)
#Máy cũng chọn ngẫu nhiên
may=random.choice(choices)
print(f"Máy chọn: {may}\n")
#Mỗi người chơi chọn ngẫu nhiên và xác định kết quả
for player in players:
    player['choice'] = random.choice(choices)
    #Xác định kết quả
    if player['choice']== may:
        result="Hòa"
    elif (player['choice']== "Kéo" and may== "Bao") or\
         (player['choice']== "Búa" and may== "Kéo") or\
         (player['choice']== "Bao" and may== "Búa"):
             result="Thắng"
    else:
        result="Thua"
    print(f"{player['name']} chọn {player['choice']}- {result}")
         