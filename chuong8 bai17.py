a=int(input("nhập số a:"))
b=int(input("nhập số b:"))
i=1
if a>b:
    for i in range(1,a+1):
        s=b*i
        if s%a==0 and s%b==0:
         print("BCNN=",s)
        break
if a<b:
    for i in range(1,b+1):
        s=a*i
        if s%a==0 and s%b==0:
         print("BCNN=",s)
         break