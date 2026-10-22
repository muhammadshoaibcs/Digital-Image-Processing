# Optional Challenge: Create a Small RGB Image
# This program creates a 3 x 3 RGB image using a nested Python list.
# Each pixel is represented by an RGB tuple.


# Create the first row of the image.
# The row contains Red, Green, and Blue pixels.
row_1 = [
    (255, 0, 0),      # Red pixel.
    (0, 255, 0),      # Green pixel.
    (0, 0, 255)       # Blue pixel.
]


# Create the second row of the image.
# The row contains White, Black, and Yellow pixels.
row_2 = [
    (255, 255, 255),  # White pixel.
    (0, 0, 0),        # Black pixel.
    (255, 255, 0)     # Yellow pixel.
]


# Create the third row of the image.
# The row contains Cyan, Magenta, and Grey pixels.
row_3 = [
    (0, 255, 255),    # Cyan pixel.
    (255, 0, 255),    # Magenta pixel.
    (128, 128, 128)   # Grey pixel.
]


# Create the complete 3 x 3 image using a nested list.
# Each item in this list represents one row of the image.
image = [
    row_1,
    row_2,
    row_3
]


# Print a heading before displaying all pixels.
print("Pixels in the 3 x 3 RGB image:")


# Use the outer loop to go through each row in the image.
for row in image:

    # Use the inner loop to go through each pixel inside the current row.
    for pixel in row:

        # Print the current RGB pixel tuple.
        print(pixel)

    # Print a blank line after each row to make the output easier to read.
    print()


# Access the pixel at row 2, column 3.
# Python starts indexing from 0, so row 2 uses index 1 and column 3 uses index 2.
selected_pixel = image[1][2]


# Print the pixel located at row 2, column 3.
print("Pixel at row 2, column 3:", selected_pixel)