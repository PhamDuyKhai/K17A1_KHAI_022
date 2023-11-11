a=int(input("nhập năm:"))
if (a%400==0) or ((a%4==0) and (a%100!=0)):
    print("năm",a,"là năm nhuận")
else:
    print("năm",a,"không phải năm nhuận")