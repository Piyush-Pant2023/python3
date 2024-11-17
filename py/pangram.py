list=[]
sentence="the quick brown fox jumps over the lazy dog"
for i in range(97,123):
    list.append (chra(i))
    for i in list:
     if i not in sentence:
     pangram = False
    if pangram==true:
    print("string is pangram")
    else:
    print("not a pangram")