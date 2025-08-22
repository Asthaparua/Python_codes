a=int(input("enter a no."))
sum=0
while(a>0):
    d=a%10
    a=a//10
    sum +=d
print(sum)