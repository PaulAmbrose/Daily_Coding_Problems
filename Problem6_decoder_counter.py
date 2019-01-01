#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#You can assume that the messages are decodable. For example, '001' is not allowed.

#Steps:
    #(DONE)#Create a way of automating a dictionary with all the letters and numbers in
    #Take a message input number string of x numbers
    #Split out the possible combination of numbers from the the input number string
        #?This is the bit im not sure about...#https://stackoverflow.com/questions/15586047/given-an-encoded-message-count-the-number-of-ways-it-can-be-decoded
    #Look up the split numbers in the dictionary created
    #Count the possible combinations and return the values for checking


#print(ord("b"))
#print(chr(97))

def create_code_dict():
    code_dict = {}
    for number in range(97,123):
        code_dict[chr(number)] = number
    return code_dict

code_dict = create_code_dict()
code = input("Please enter a code using digits only >> ")
print("The code entered for analysis is " + str(code))
print("The dictionary created for this is " + str(code_dict))