import re

with open('day1_input.txt', 'r') as file:
    input_array  = file.readlines()

def dayone_mod (input_array):
    final_array = []
    
    for line in input_array:
        # get first digit
        first_num = re.search(r'(\d|one|two|three|four|five|six|seven|eight|nine)',line).group()
        
        # get last digit
        last_num = re.search(r'(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)',line[::-1]).group()
        
        # convert num to digit 
        number_dict = {'one':'1', 
                       'two':'2', 
                       'three':'3', 
                       'four':'4', 
                       'five':'5', 
                       'six':'6', 
                       'seven':'7', 
                       'eight':'8', 
                       'nine':'9'}
        
        if first_num in number_dict:
            first_num = number_dict[first_num]
            
        if last_num[::-1] in number_dict:
            last_num = number_dict[last_num[::-1]]
            
        # get result
        result = int(first_num + last_num)
        final_array.append(result)
        
    return sum(final_array)

  dayone_mod(input_array)
