def ShiftLeft(N):
        L=eval(input("Enter a list:"))
        l1=len(L)
        while N>0:
                for i in range(l1):
                        g=L[i]
                        L.pop(i)
                        L.append(g)
                        return(L)
                N+=1

t=int(input("Enter the number of elements:"))
print(ShiftLeft(t))
