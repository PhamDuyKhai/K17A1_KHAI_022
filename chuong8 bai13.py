a=int(input("nhập số n:"))
A=0
B=0
C=1
D=1
E=0
F=0
for i in range(1,a):
    if i%2!=0:
        A+=i
print("A=",A)
for i in range(1,a):
    if i%2==0:
        B+=i
print("B=",B)     
for i in range(1,a):
    if i%2!=0:
        C*=i
print("C=",C)
for i in range(1,a):
    if i%3==0:
        D*=i
print("D=",D)
for i in range(2,a):
    if a%i==0:
     E+=i
print("E=",E)
for i in range(1, a+1):
    if i%2!=0:
        F+=1/i
    elif i%2==0:
        F-=1/i
print("F=",F)