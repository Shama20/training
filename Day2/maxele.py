m1=999
m2=-999
for i in range(5):
    a= int(input("Enter number: "))
    m1 = min(m1, a)
    m2 = max(m2, a)
print("Minimum",m1)
print("Maximum",m2)
