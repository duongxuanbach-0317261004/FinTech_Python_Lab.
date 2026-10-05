# hw2_promo_code.py

print("----- MÁY PHÁT SINH MÃ ƯU ĐÃI -----")

# 1. Nhập họ tên đầy đủ
full_name = input("Nhập họ tên đầy đủ: ")
 
# 2. Nhập năm sinh
birth_year = input("Nhập năm sinh: ")
 
# 3. Dùng split() để lấy từ cuối cùng (Tên)
first_name = full_name.split()[-1]
 
# Dùng Slicing [0:3] và upper() để lấy 3 chữ cái đầu và viết hoa
# (Nếu tên ngắn hơn 3 ký tự, slicing tự động lấy toàn bộ tên)
name_code = first_name[0:4].upper()
 
# Nối chuỗi bằng F-strings để tạo mã ưu đãi
promo_code = f"{name_code}-{birth_year}-VIP"
 
# In kết quả
print(f"Mã ưu đãi của bạn là: {promo_code}")
 
