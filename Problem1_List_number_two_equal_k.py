#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

k = 15
list = [1,2,3,14]

#function1 - number at i + number at 1, equal k? number at 2, 3, 4 etc etc
#function2 - move number at i + 1 to position 0, run function 1

def run_check():
  test_number = list[0]
  list.pop(0)
  test1 = "no"
  for i in list:
    if (i + test_number) == k:
      test1 = "yes"
  list.append(test_number)
  if test1 == "yes":
    return "yes"
  else:
    return "no"

for numbers in range(0,len(list)+1):
  test = run_check()   
print(test)