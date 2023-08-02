m=-999
a=999
for i in range(5):
    
    e= int(input("Enter 5 numbers: "))
    if(e<a):
        b=a
        a=e
    if(e>m):
        ma=m
        m=e
    
print("second min: ",b)
print("second max: ",ma)