n=int(input())
l=0
r=100
mid=-1
cnt=0
while mid!=n:
    mid=int((l+r)/2)
    cnt+=1
    if mid>n:
        print(f"{mid} 大")
        r=mid
    elif mid<n:
        print(f"{mid} 小")
        l=mid+1
print(f"{n} 正确")

print(f"最终猜了{cnt}次")
