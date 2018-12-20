#Given an array of integers, find the first missing positive integer in linear
#time and constant space. In other words, find the lowest positive integer that
#does not exist in the array. The array can contain duplicates and negative
#numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
#give 3.

#Plan
#1)For loop to look at each integer
#2)If its postive run function to check if its the lowest so far
#3)If its zero or negative skip over
#4)Decision:
#5)    Separate decision function
       #Is lowest +1 in the input array?
               #Yes - add 1 to lowest and try again 
               #No - return lowest as the result
def main():
    
    input = [3,4,-1,1]
    lowest = 0

    def lowest_check(number, lowest):
        if number <= 0:
            return lowest
        else:
            if number > lowest:
                if lowest == 0:
                    lowest = number
                    return lowest
                else:
                    return lowest
            else:
                return lowest
    
    def decision_check(lowest_number):
    
        if lowest_number in input == 1:
            lowest_number = lowest_number + 1    
            decision_check
        else:
            return lowest_number
    
    for number in input:
        new_low = lowest_check(number,lowest)
        lowest = new_low
        
    answer = decision_check(lowest)
    print(answer)

if __name__ == "__main__":
    main()


