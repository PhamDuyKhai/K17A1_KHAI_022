from datetime import datetime
import calendar
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
now = datetime(nam,thang,ngay)
print("Ngày tháng năm vừa nhập:", now.strftime("%d-%m-%Y"))
nam_nhuan = calendar.monthrange(nam, 2)
if nam_nhuan[1] == 29:
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không là năm nhuận.")
thu = calendar.weekday(nam,thang,ngay)
if thu == 0:
    print(now.strftime("%d-%m-%Y"), "là thứ Hai")
elif thu == 1:
    print(now.strftime("%d-%m-%Y"), "là thứ Ba")   
elif thu == 2:
    print(now.strftime("%d-%m-%Y"), "là thứ Tư")   
elif thu == 3:
    print(now.strftime("%d-%m-%Y"), "là thứ Năm")   
elif thu == 4:
    print(now.strftime("%d-%m-%Y"), "là thứ Sáu")   
elif thu == 5:
    print(now.strftime("%d-%m-%Y"), "là thứ Bảy")   
elif thu == 6:
    print(now.strftime("%d-%m-%Y"), "là Chủ nhật")   
print(f"Số ngày trong tháng {thang} là {calendar.monthrange(nam, thang)[1]}")