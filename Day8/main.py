numbers = []
for i in range(5):
   num = int(input(f"{i+1}-enter an integer: "))

   numbers.append(num)
print(numbers)
sum = sum(numbers)
print(f"the sum of the number in this liset is: {sum}")
average = sum/len(numbers)
print(f"the average is:{round(average,2)}")
largest = max(numbers)
print(f"the largest number in this list is: {largest} ")

