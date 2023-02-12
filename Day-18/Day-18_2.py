import colorgram

# Extract 6 colors from an image.
rgb_colors=[]
colors = colorgram.extract('download.jpg', 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)

color_list = [(230, 227, 225), (229, 223, 226), (217, 227, 220), (195, 172, 121), (222, 227, 232), (157, 97, 59), (185, 159, 52), (9, 53, 77), (125, 37, 25), (55, 33, 27), (110, 69, 85), (118, 162, 175), (27, 118, 164), (74, 35, 43), (85, 138, 67), (10, 62, 44), (71, 153, 130), (121, 35, 40), (182, 98, 82), (207, 202, 146)]
# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)
hsl = first_color.hsl # e.g. (230, 255, 203)
proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
red = rgb[0]
red = rgb.r
saturation = hsl[1]
saturation = hsl.s
