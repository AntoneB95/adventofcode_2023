import re

with open('day2_input.txt', 'r') as file:
    input_array  = file.readlines()

def daytwo (input_array):
    # set cube counts
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14
    # set result counter  
    result = 0

    for idx,game in enumerate(input_array):
        possible = True
        # split game into turns
        turns = game.split(';')
      
        # check if game is possible
        for turn in turns:
            # check reds
            try:
                red = int(re.search(r'(\d+) red', turn).group(1))
            except:
                red = 0
            if red > red_cubes:
                possible = False
              
            # check greens
            try:
                green = int(re.search(r'(\d+) green', turn).group(1))
            except:
                green = 0
            if green > green_cubes:
                possible = False
                
            # check blues
            try:
                blue = int(re.search(r'(\d+) blue', turn).group(1))
            except:
                blue = 0
            if blue > blue_cubes:
                possible = False
                
        # if passed, add game to final_result
        if possible:
            result = result + (idx+1)
        
    # return result
    return result

print(daytwo(input_array))
