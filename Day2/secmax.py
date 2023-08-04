m1=-999
m2=999
for i in range(5):
    a= int(input("Enter number: "))
    if(a<m2):
        min=m2
        m2=a
    if(a>m1):
        max=m1
        m1=a
print("Second min: ",min)
print("Second max: ",max)