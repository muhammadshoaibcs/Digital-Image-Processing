
# Exercise 3: RGB to Grayscale Conversion
# This program converts an RGB color into a single grayscale intensity value.
# It uses the average method specified in the assignment.


# Define a function named rgb_to_grayscale that accepts three RGB components.
def rgb_to_grayscale(red, green, blue):

    # Add the red, green, and blue component values together.
    total = red + green + blue

    # Calculate the average of the three RGB component values.
    gray_value = total / 3

    # Convert the average into an integer and return the grayscale value.
    return int(gray_value)


# Test the function using white (255, 255, 255).
print(rgb_to_grayscale(255, 255, 255))  # Expected output: 255

# Test the function using black (0, 0, 0).
print(rgb_to_grayscale(0, 0, 0))  # Expected output: 0

# Test the function using red (255, 0, 0).
print(rgb_to_grayscale(255, 0, 0))  # Expected output: 85
