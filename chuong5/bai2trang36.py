# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:52:20 2024

@author: Admin
"""

#Viết hàm kiểm tra để phát hiện chuỗi nhập vào có phải là một e-mail hay không?
#Ø Chú ý: Nếu là các e-mail xuất phát từ Gmail, Yahoo, Hotmail, Outlook… (gọi
#tắt là tập luật tên miền e-mail) thì trước ký tự @ là một chuổi tối thiểu 6 ký tự,không khoảng trắng và ký tự đặc biệt.
#Ø Khảo sát và tìm thêm các tên miền e-mail để bổ sung vào tập luật giới hạn trên.
import re
#Tập hợp các tên miền phổ biến
common_domains={"gmail.com","yahoo.com","hotmail.com","outlook.com"}
#Biểu thức chính quy kiểm tra các định dạng email cơ bản
regex=r"^[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+$"
#Nhập địa chỉ email thường dùng
email=input("Nhập địa chỉ email của bạn: ")
#Kiểm tra email có khớp với chính quy không
if re.match(regex,email):
    #Tách teeb người dùng và tên miền
    username,domain=email.split("@")
    
    #Kiểm tra tên người dùng và tên miền
    if len(username)>=6 and domain in common_domains:
        print(f"{email} là một địa chỉ email hợp lệ và thuộc các tên miền phổ biến")
    else:
        print(f"{email} là một địa chỉ email hợp lệ nhưng không thuộc các tên miền phổ biến")
else:
    print(f"{email} không phải là một địa chỉ email hợp lệ")
    