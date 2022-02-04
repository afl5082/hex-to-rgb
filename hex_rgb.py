
'''
    1. Takes two hexidecimal inputs from user prompt
    2. converts to RGB and computes the mean of the two inputs
    3. Returns(prints) RBG mean back into hexidecimal format
'''

hex1_input = input('Enter hex color 1: ').lstrip('#')
hex2_input = input('Enter hex color 2: ').lstrip('#')

def mean_rgb_from_hex(hex1,hex2):
    rgb_mean = ()
    for i in (0,2,4):
        #converts slices of hexidecimal string into int with base 16
        rgb1 = int(hex1[i:i+2],16)
        rgb2 = int(hex2[i:i+2],16)

        mean = (rgb1 + rgb2) / 2 
        rgb_mean += (round(mean),)
    return rgb_mean

def rgb_to_hex(rgb):
    hex = '%02x%02x%02x' % rgb
    return hex


rgb_mean = mean_rgb_from_hex(hex1_input,hex2_input)
new_hex = rgb_to_hex(rgb_mean)

print(new_hex)
