# Bài 3: Trích xuất Dữ liệu Giao dịch Tài chính (Xử lý chuỗi, Ép kiểu, Điều kiện)
 
print("--- TRÍCH XUẤT DỮ LIỆU GIAO DỊCH ---")
# Nhập mã giao dịch, VD: "GD001-5000000-VND"
ma_giao_dich = input("Nhập mã giao dịch: ")
 
# Tìm vị trí 2 dấu "-" để xác định phần số tiền nằm giữa
vi_tri_dau = ma_giao_dich.find("-")
vi_tri_cuoi = ma_giao_dich.rfind("-")
 
# Dùng string slicing để trích xuất phần số tiền (dạng chuỗi)
so_tien_str = ma_giao_dich[vi_tri_dau + 1:vi_tri_cuoi]
 
# Ép kiểu chuỗi sang số nguyên (int)
so_tien = int(so_tien_str)
 
print(f"Số tiền giao dịch trích xuất được: {so_tien:,} VND")
 
# Dùng cấu trúc rẽ nhánh if/else để kiểm tra điều kiện
if so_tien >= 5000000:
    print("Giao dịch cần xác thực OTP")
else:
    print("Giao dịch thành công")
