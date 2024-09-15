# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:25:57 2024

@author: Admin
"""

import re
#Nhập thông tin đăng nhập từ người dùng
username=input("Nhập tên đăng nhập: ")
password=input("Nhập mật khẩu: ")
#Kiểm tra username
if not 6<= len(username)<=24:
    print("Tên đăng nhập phải từ 6 đến 24 ký tự ")
elif not re.match(r"^[a-zA-z0-9]+$",username):
    print("Tên đăng nhập chỉ được chứa chữ cái và số")
#Kiểm tra password
else:
    if not 6<=len(password)<=24:
        print("Mật khẩu phải từ 6 đến 24 ký tự")
    elif not re.search(r"^[a-z]",password):
        print("Mật khẩu phải chứa ít nhất một chữ cái thường")
    elif not re.search(r"^[A-Z]",password):
        print("Mật khẩu phải chứa ít nhất một chữ cái hoa")
    elif not re.search(r"\d",password):
        print("Mật khẩu phải chứa ít nhất một số")
    elif not re.search(r"$#@",password):
        print("Mật khẩu phải chứa ít nhất một trong các ký tự đặc biệt: $ # @")
    else:
        print("Đăng nhập thành công")
        