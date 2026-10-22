# Excercise 01: RGB Pixel Values and Percentage Conversion
# This program stores RGB color values and converts each value into a percentage.
# Store the red color component value in the variable 'red'.
Red = 255

# Store the green color component value in the variable 'green'.
Green = 128

# Store the blue color component value in the variable 'blue'.
Blue = 0


# Create an RGB tuple containing the red, green, and blue values.
rgb = (Red, Green, Blue)


# Print the complete RGB tuple.
print("RGB:", rgb)


# Convert the red value into a percentage using the formula:
# Percentage = (Value / 255) * 100
Red_Percentage = (Red / 255) * 100


# Convert the green value into a percentage using the same formula.
Green_Percentage = (Green / 255) * 100


# Convert the blue value into a percentage using the same formula.
Blue_Percentage = (Blue / 255) * 100


# Print the red percentage rounded to two decimal places.
print(f"Red: {Red_Percentage:.2f}%")


# Print the green percentage rounded to two decimal places.
print(f"Green: {Green_Percentage:.2f}%")


# Print the blue percentage rounded to two decimal places.
print(f"Blue: {Blue_Percentage:.2f}%")