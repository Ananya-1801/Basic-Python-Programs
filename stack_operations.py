##data structure refers to the data collection with well defined operations and behaviour or properties
#stack is a linear data structure which is implemented in LIFO manner.

def isEmpty(stack1):
    if stack1==[]:
        return "True"
    else:
        return "False"

def Push(stack1,item):
    stack1.append(item)
    top=len(stack1)-1

def Pop(stack1):
    if stack1==[]:
        return "Underflow"
    else:
        item=stack1.pop()
        if len(stack1)==0:
            top=None
        else:
            top=len(stack1)-1
        return item

def Peek(stack1):
    if isEmpty(stack1):
        return "Underflow"
    else:
        top=len(stack1)-1
        print(stack1[top],"<--top")

def Display(stack1):
    if isEmpty(stack1):
        return "Underflow"
    else:
        top=len(stack1)-1
        for a in range(top-1,-1,-1):
            print(a)

#main


Stack=[]
top=None

ch=='Y'
while ch=='Y':
    print("STACK OPERATIONS")
    print("1.PUSH")
    print("2.POP")
    print("3.PEEK")
    print("4.DISPLAY")
    print("5.EXIT")
    choice=int(input("Enter the your choice(1-5):"))
    if choice==1:
        item=int(input("Enter data:"))
        Push(Stack,item)
    elif choice==2:
        item=Pop(Stack)
        if item=="Underflow":
            print("Underflow")
        else:
            print(item)
    elif choice==3:
        item=Peek(Stack)
        if item=="Underflow":
            print("Underflow")
        else:
            print(item)
    elif choice==4:
        Display(Stack)
    elif choice==5:
        break
    else:
        print("Invalid choice")
    ch=input("DO YOU WANT TO PROCEED(Y/N):")
