#Given an array of integers, return a new array such that each element at 
#index i of the new array is the product of all the numbers in the original 
#array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output 
#would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
#the expected output would be [2, 3, 6].

#Follow-up: what if you can't use division?

#create new list for output
#create a holder variable to i[0]
#take out i[0] from the original array and put in holder
#Do the multiplication and put result in new list
#Add back in i[0] but to end of oringal list
#Do again for length of list

input_list = [1,2,3,4,5]
#input_list = [1,2,3]

i_holder = ''
output_list = []
sum_list = 0
list_num = 0

for numbers in input_list:
  i_holder = input_list[0]
  input_list.pop(0)
  for numbers_left in input_list:
    try:
      sum_list = sum_list + (input_list[list_num] * input_list[list_num+1])
      list_num = list_num + 1
      output_list.append(sum_list)
    except:
      input_list.append(i_holder)
print(sum_list)