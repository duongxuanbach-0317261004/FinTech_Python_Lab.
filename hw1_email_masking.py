# hw1_email_masking.py.

print("--- MASKING EMAIL KHÁCH HÀNG ---")
# 1. Nhập địa chỉ email
email = input("Nhập địa chỉ email: ")
 
# 2. Dùng split("@") để tách tên đăng nhập và tên miền
username, domain = email.split("@")
 
# 3. Trích xuất 3 ký tự đầu tiên của tên đăng nhập bằng Slicing
first_3_chars = username[0:3]
 
# 4. Ghép 3 ký tự đầu + "***@" + tên miền
masked_email = first_3_chars + "***@" + domain
 
# In kết quả
print(f"Email đã che: {masked_email}")
 
