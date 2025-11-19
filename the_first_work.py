n=int(input())
a=50
cnt=0
while a!=n:
    a=int((a+n)/2)
    cnt+=1
    if a>n:
        print(f"{a} 大")
    elif a<n:
        print(f"{a} 小")
print(f"{n} 正确")

print(f"最终猜了{cnt}次")
