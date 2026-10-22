# Exercise 04: Calculate Bitmap Storage Size
# This program calculates the raw pixel-data storage required 
# for different image formats using image dimensions and bits per pixel.


# Store the image width in pixels.
width = 640

# Store the image height in pixels.
height = 480


# Calculate the total number of pixels in the image.
total_pixels = width * height


# Store the number of bits used for one bilevel black-and-white pixel.
bilevel_bits_per_pixel = 1

# Store the number of bits used for one greyscale pixel.
grayscale_bits_per_pixel = 8

# Store the number of bits used for one RGB pixel.
rgb_bits_per_pixel = 24

# Store the number of bits used for one RGBA pixel.
rgba_bits_per_pixel = 32


# Calculate the storage required for the bilevel image in bytes.
# The total number of bits is divided by 8 because 8 bits = 1 byte.
bilevel_storage = (total_pixels * bilevel_bits_per_pixel) // 8


# Calculate the storage required for the greyscale image in bytes.
grayscale_storage = (total_pixels * grayscale_bits_per_pixel) // 8


# Calculate the storage required for the RGB image in bytes.
rgb_storage = (total_pixels * rgb_bits_per_pixel) // 8


# Calculate the storage required for the RGBA image in bytes.
rgba_storage = (total_pixels * rgba_bits_per_pixel) // 8


# Print the total number of pixels in the image.
print(f"Total pixels: {total_pixels:,}")


# Print the storage required for the bilevel image.
print(f"Bilevel: {bilevel_storage:,} bytes")


# Print the storage required for the greyscale image.
print(f"Greyscale: {grayscale_storage:,} bytes")


# Print the storage required for the RGB image.
print(f"RGB: {rgb_storage:,} bytes")


# Print the storage required for the RGBA image.
print(f"RGBA: {rgba_storage:,} bytes")