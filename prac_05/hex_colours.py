COLORS = {
    "AliceBlue": "#F0F8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Bisque": "#FFE4C4",
    "Black": "#000000",
    "BlanchedAlmond": "#FFEBCD",
    "Blue": "#0000FF"
}

while True:
    color_name = input("Enter a color name (or press Enter to quit): ").capitalize()
    if color_name == "":
        break
    elif color_name in COLORS:
        print(f"The hexadecimal code for {color_name} is {COLORS[color_name]}")
    else:
        print("Invalid color name")