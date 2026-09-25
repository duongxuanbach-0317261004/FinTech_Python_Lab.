print("----- CHIA TIỀN HÓA ĐƠN -----")
# Nhập thông tin hóa đơn
X = float(input("Nhập tổng hóa đơn (X): "))
Y = float(input("Nhập % tip cho nhân viên (Y): "))
N = int(input("Nhập số người chia (N): "))
 
# Tính toán các thành phần
tip_amount = X * (Y / 100)
total_with_tip = X + tip_amount
per_person = round(total_with_tip / N)
 
# Hiển thị hóa đơn
print("\n----- CHI TIẾT HÓA ĐƠN -----")
print(f"Tổng hóa đơn        : {round(X):,} VND")
print(f"Tiền tip ({Y:.0f}%) : +{round(tip_amount):,} VND")
print("-" * 30)
print(f"Tổng cộng           : {round(total_with_tip):,} VND")
print(f"Số người chia       : {N}")
print("-" * 30)
print(f"MỖI NGƯỜI PHẢI TRẢ  : {per_person:,} VND")
