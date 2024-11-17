for i in range(5,0,-1):
  
    v=64
    for j in range(5-i):
        print(" ",end="")
    for k in range(2*i-1):
        v+=1
        print(chr(v),end="")
    print()