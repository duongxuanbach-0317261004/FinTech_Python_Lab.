# Bài 4: Tính Lãi suất Tiết kiệm (Biến & Toán tử số học).
 
Chương trình nhập vào 3 thông tin: số tiền gốc, lãi suất năm (dạng số thập phân, ví dụ 0.06 ứng với 6%) và thời gian gửi
tính bằng năm. Sau đó tính tổng số tiền nhận được sau thời gian
gửi theo công thức lãi đơn:
 
    tong_tien = so_tien_goc * (1 + lai_suat_nam * thoi_gian)
 
print("--- TÍNH LÃI SUẤT TIẾT KIỆM ---")
 
# Nhập dữ liệu và ép kiểu phù hợp
so_tien_goc = float(input("Nhập số tiền gốc: "))
lai_suat_nam = float(input("Nhập lãi suất năm (vd: 0.06 cho 6%): "))
thoi_gian = int(input("Nhập thời gian gửi (năm): "))
 
# Tính tổng số tiền nhận được theo công thức lãi đơn
tong_tien = so_tien_goc * (1 + lai_suat_nam * thoi_gian)
 
# Hiển thị kết quả
print(f"\nSố tiền gốc        : {so_tien_goc:,.0f} VND")
print(f"Lãi suất năm       : {lai_suat_nam * 100:.1f}%")
print(f"Thời gian gửi      : {thoi_gian} năm")
print("-" * 30)
print(f"TỔNG TIỀN NHẬN ĐƯỢC: {tong_tien:,.0f} VND")
