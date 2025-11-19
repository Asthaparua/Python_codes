# def count_digits(n):
#     if n < 10:
#         return 1
#     return 1 + count_digits(n // 10)
# N = int(input("Enter a number: "))
# print("Number of digits:", count_digits(abs(N)))


# GIVEN AN ARRAY ELEMENT EVERY ELEMENT REPEAT TWICE ACCEPT ONE NUMBER FIND THAT UNIQUE NUMBER.
arr = [2, 3, 4, 3, 2]
ans=0 
# 
for i in range(len(arr)):
    ans=ans^arr[i]
print(ans)