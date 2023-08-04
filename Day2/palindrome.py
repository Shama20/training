n=int(input("Enter a number: "))
m=n
sum = 0
while n!=0:
    digit = n%10
    sum=sum*10+digit
    n=n//10

if m==sum:
    print("Is a  Palindrome")
else:
    print("Not a palindrome")