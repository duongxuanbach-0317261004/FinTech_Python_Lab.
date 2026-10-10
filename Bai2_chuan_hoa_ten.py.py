# Bài 2: Chuẩn hóa Dữ liệu Khách hàng (Xử lý chuỗi)
 
# Dữ liệu giả lập (tên khách hàng chưa chuẩn hóa)
ten_khach_hang = " dƯơNG XuâN báCh "
 
# Dùng strip() để loại bỏ khoảng trắng thừa ở hai đầu,
# lower() để đưa toàn bộ về chữ thường,
# rồi title() để viết hoa chữ cái đầu mỗi từ
ten_chuan_hoa = ten_khach_hang.strip().lower().title()
 
# In kết quả
print(f"Tên gốc        : '{ten_khach_hang}'")
print(f"Tên đã chuẩn hóa: '{ten_chuan_hoa}'")
