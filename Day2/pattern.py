i=input("Enter: ")
a=0
b=0
for p in i:
    if p=='*':
        a+=1
    elif p=='#':
        b+=1
print(a-b)