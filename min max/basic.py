# import csv
# f=open("piyush.csv","w",newline="")
# w=csv.writer(f)
# for i in range(3):
#     name=input("enter the name")
#     marks=int(input("enter the marks: "))
        # sturec=[name,marks]
        # w.writerow(sturec)
        # print(file.read())
        # f.close()
import pickle
fh=open("piyush.dat","w")
for i in range(2):
    name=input("enter the name: ")
    pickle.dump(name,fh)
fh.close()