def isPalindrome(num):
    finalnum=num
    n=p=0
    while(num!=0):
        p=num%10
        n=n*10+p
        num=num//10
    if(finalnum==n):
        return 1;
    else:
        return 0;
    
#main
    
num=(float(input("Enter the number:")))
res=isPalindrome(num)
if(res==1):
    print("The entered number is a is a palindrome!\n")
else:
    print("The entered number is not a palindrome!\n")