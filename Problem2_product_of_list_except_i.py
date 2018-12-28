#Given an array of integers, return a new array such that each element at 
#index i of the new array is the product of all the numbers in the original 
#array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output 
#would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
#the expected output would be [2, 3, 6].

#Follow-up: what if you can't use division?

#Plan
#1 - Set up loop for each number in the list whereby it:
        #a)removes the number and puts in the holder
        #b) replaces the number into the list at the end at the end of the
        #    loop

#2 - While the number is out, use list comprehension to get a product of all
        #numbers in the array
        
#3 - while the number is out, add the product to a new array which will become
        #the answer

#----

#input_list = [1,2,3,4,5]
input_list = [1,2,3]

i_holder = ''
output_list = []
sum_list = 0
list_num = 0

for numbers in input_list:
  i_holder = input_list[0]
  input_list.pop(0)
    
  result = 1
  for x in input_list:
      result *= x
  output_list.append(result)  
  
  input_list.append(i_holder)
print(output_list)