import pickle
fp=open("marks.dat","wb+")
n=int(input("Enter the number of records:"))
stu= {}
for i in range(n):
    rno=int(input("Enter the roll number:"))
    nm=input("Enter the name of the student:")
    mrk=float(input("Enter the marks of the student:"))
    stu['Roll number']=rno
    stu['Name']=nm
    stu['Marks']=mrk
    pickle.dump(stu,fp)
fp.close()

fp=open("marks.dat","rb")
temp={}
try:
    while True:
        reader=pickle.load(fp)
        print("\n")
        print(reader)
except:
    fp.close()
