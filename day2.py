import re

with open('day2_input.txt', 'r') as file:
    input_array  = file.readlines()

## PART ONE ##
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


## PART TWO ##
def daytwo_mod (input_array):
    result = 0
    
    for game in input_array:
        max_red = max_green = max_blue = 0
        
        #split game into turns
        turns = game.split(';')
        
        for turn in turns:
            # check reds
            try:
                red = int(re.search(r'(\d+) red', turn).group(1))
            except:
                red = 0
            if red > max_red:
                max_red = red
            # check greens
            try:
                green = int(re.search(r'(\d+) green', turn).group(1))
            except:
                green = 0
            if green > max_green:
                max_green = green
            # check blues
            try:
                blue = int(re.search(r'(\d+) blue', turn).group(1))
            except:
                blue = 0
            if blue > max_blue:
                max_blue = blue
                
        # calculate result
        result = result + (max_red * max_green * max_blue)
        
    return result

## RESULTS
print(daytwo(input_array))
print(daytwo_mod(input_array))
