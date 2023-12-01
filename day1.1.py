with open('day1_input.txt', 'r') as file:
    input_array  = file.readlines()

  def dayone (input_array):
    final_array = []
    
    for line in input_array:
        # get first digit
        for char in line:
            if char.isnumeric():
                first_digit = char
                break
                
        # get last digit
        for char in line[::-1]:
            if char.isnumeric():
                last_digit = char
                break
                
        # get result
        result = int(first_digit+last_digit)
        final_array.append(result)
        
    # get final result
    return sum(final_array)

  dayone(input_array)
