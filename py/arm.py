num=453
temp=num
arm=0
while(temp!=0):
    r=temp%10
    arm=arm+r*r*r
    temp=temp/10
    if arm==num:
        print("no is armstrong")
    else:
        print("not a strong no")