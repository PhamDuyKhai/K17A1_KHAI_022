a=int(input("nhập số:"))
s=0
for i in range(1,a):
    if a%i==0:
        s+=i
if a==s:
    print(a,"là số hoàn hảo")
else:
    print(a,"không là số hoàn hảo")