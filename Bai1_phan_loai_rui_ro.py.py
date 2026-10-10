# Bài 1: Phân loại Hạn mức Rủi ro Tín dụng (Cấu trúc rẽ nhánh)
 
def phan_loai_khach_hang(diem_credit):
    """
    Nhận vào điểm tín dụng (số nguyên từ 300 đến 850)
    và trả về phân hạng rủi ro tương ứng.
    """
    if diem_credit >= 750:
        return "Rủi ro Thấp - Duyệt tự động"
    elif diem_credit >= 600:
        return "Rủi ro Trung bình - Cần thẩm định"
    else:
        return "Rủi ro Cao - Từ chối cấp tín dụng"
 
 
# Chương trình chính
print("--- PHÂN LOẠI HẠN MỨC RỦI RO TÍN DỤNG ---")
diem_credit = int(input("Nhập điểm tín dụng (300 - 850): "))
ket_qua = phan_loai_khach_hang(diem_credit)
print(f"Kết quả phân loại: {ket_qua}")
