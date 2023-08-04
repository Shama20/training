a=int(input("Enter a number"))
prime=[2,3]
i=3
if(0<a<3):
    print(a,' Prime Number is :',prime[a-1])
elif(a>2):
    while (True):
        i+=1
        status = True
        for j in range(2,int(i/2)+1):
            if(i%j==0):
                status = False
                break
        if(status==True):
            prime.append(i)
        if(len(prime)==a):
            break
    print(a,' Prime Number is :', prime[a-1])
else:
    print('Invalid! ')