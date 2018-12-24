#Given an array of integers, find the first missing positive integer in linear
#time and constant space. In other words, find the lowest positive integer that
#does not exist in the array. The array can contain duplicates and negative
#numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
#give 3.

#input = [1, 2, 0]
#input = [3, 4, -1,1]
input = [2,4,5]

input.sort()
for number in input:
  if number < 0:
    input.remove(number)
counter = 1
while True:
    if counter in input:
        counter = counter +1
    else:
        print("The answer is..." + str(counter))
        break
