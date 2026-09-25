print("----- TÍNH TỶ SUẤT SINH LỜI (ROI-Return on Investment) -----")
# Nhập thông tin đầu tư
initial_investment = float(input("Nhập tổng vốn ban đầu: "))
final_value = float(input("Nhập tổng giá trị bán ra: "))
 
# Tính toán các thành phần
net_profit = final_value - initial_investment
roi_percent = (net_profit / initial_investment) * 100
 
# Hiển thị kết quả
print("\n----- KẾT QUẢ ĐẦU TƯ -----")
print(f"Vốn ban đầu          : {round(initial_investment):,} VND")
print(f"Giá trị bán ra       : {round(final_value):,} VND")
print("-" * 30)
print(f"Lợi nhuận ròng       : {round(net_profit):,} VND")
print(f"Tỷ lệ ROI            : {roi_percent:.2f}%")
