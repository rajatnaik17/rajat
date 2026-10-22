numbers=[]
print("enter 10 numbers:")
for i in range(10):
    user_input=input("enter the numbers")
    numbers.append(float(user_input))
total_sum=sum(numbers)
print("the sum is:",total_sum)

