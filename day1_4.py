n = int(input())
c=0
a= int(input())
m=a
for i in range(1,n):
    a= int(input())
    if(m<a):
         c=c+1
         m=a
print(c)