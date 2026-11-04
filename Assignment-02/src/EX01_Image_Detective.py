# Import Path for reliable file and folder paths.
from pathlib import Path

# Import Pillow classes for image processing and statistics.
from PIL import Image, ImageStat, ExifTags


# ============================================================
# STEP 1: DEFINE PROJECT PATHS
# ============================================================

# Get the folder where this Python file is located.
script_dir = Path(__file__).resolve().parent

# Get the Assignment-02 folder.
assignment_dir = script_dir.parent

# Define the input image folder.
input_dir = assignment_dir / "images" / "input"

# Define the output image folder.
output_dir = assignment_dir / "images" / "output"

# Create the output folder if it does not already exist.
output_dir.mkdir(parents=True, exist_ok=True)

# Define the complete path of the original input image.
image_path = input_dir / "original_photo.jpg"

# Define the output path for the greyscale image.
grayscale_output_path = output_dir / "grayscale_image.png"


# ============================================================
# STEP 2: CHECK WHETHER INPUT IMAGE EXISTS
# ============================================================

# Check whether the required input image exists.
if not image_path.exists():
    raise FileNotFoundError(
        f"Input image was not found:\n{image_path}\n"
        "Please place original_photo.jpg inside Assignment-02/images/input/"
    )


# ============================================================
# STEP 3: OPEN THE ORIGINAL IMAGE
# ============================================================

# Open the original photograph using Pillow.
image = Image.open(image_path)


# ============================================================
# PART A: IMAGE ATTRIBUTES AND METADATA
# ============================================================

print("\n========== PART A: IMAGE ATTRIBUTES ==========\n")

# Display the complete input image path.
print("Image Path:", image_path)

# Display image width.
print("Width:", image.width, "pixels")

# Display image height.
print("Height:", image.height, "pixels")

# Display image format such as JPEG or PNG.
print("Format:", image.format)

# Display image colour mode such as RGB, RGBA, or L.
print("Colour Mode:", image.mode)

# Display image bands.
print("Bands:", image.getbands())


# ============================================================
# STEP 4: CHECK EXIF METADATA
# ============================================================

print("\n========== EXIF METADATA ==========\n")

# Retrieve EXIF metadata from the original image.
exif_data = image.getexif()

# Check whether EXIF metadata exists.
if exif_data:

    print("EXIF metadata found.")

    # Create a dictionary to store readable EXIF information.
    readable_exif = {}

    # Convert numeric EXIF tag IDs into readable names.
    for tag_id, value in exif_data.items():

        # Get the readable tag name.
        tag_name = ExifTags.TAGS.get(tag_id, tag_id)

        # Store the tag and its value.
        readable_exif[tag_name] = value

    # Define useful EXIF fields to search for.
    useful_fields = [
        "Make",
        "Model",
        "DateTime",
        "DateTimeOriginal",
        "ExposureTime",
        "FNumber",
        "ISOSpeedRatings",
        "FocalLength"
    ]

    # Count the number of meaningful EXIF fields displayed.
    fields_found = 0

    # Search for useful EXIF fields.
    for field in useful_fields:

        # Check whether the field exists.
        if field in readable_exif:

            # Display the field and its value.
            print(field + ":", readable_exif[field])

            # Increase the counter.
            fields_found += 1

            # Stop after displaying three meaningful fields.
            if fields_found >= 3:
                break

    # Report if EXIF exists but useful selected fields are unavailable.
    if fields_found == 0:
        print(
            "EXIF metadata exists, but the selected meaningful fields "
            "were not found."
        )

else:

    # Report honestly if no EXIF metadata exists.
    print("No EXIF metadata was found in the image.")


# ============================================================
# STEP 5: CHECK ANIMATION INFORMATION
# ============================================================

print("\n========== ANIMATION INFORMATION ==========\n")

# Check whether the image is animated.
# False is used if the attribute is unavailable.
is_animated = getattr(image, "is_animated", False)

# Get the number of frames.
# A normal photograph is treated as one frame.
number_of_frames = getattr(image, "n_frames", 1)

# Display animation information.
print("Is Animated:", is_animated)
print("Number of Frames:", number_of_frames)


# ============================================================
# PART B: STATISTICAL ANALYSIS
# ============================================================

print("\n========== PART B: STATISTICAL ANALYSIS ==========\n")


# ============================================================
# STEP 6: CONVERT IMAGE TO GREYSCALE
# ============================================================

# Convert the original image to 8-bit greyscale.
gray_image = image.convert("L")

# Save the greyscale image as PNG.
gray_image.save(grayscale_output_path)

# Confirm the output location.
print("Greyscale image created successfully.")
print("Greyscale Image Saved To:", grayscale_output_path)


# ============================================================
# STEP 7: CALCULATE HISTOGRAM
# ============================================================

# Calculate the greyscale histogram.
histogram = gray_image.histogram()

# Display the number of histogram bins.
print("\nHistogram Bins:", len(histogram))


# ============================================================
# STEP 8: CALCULATE IMAGE STATISTICS
# ============================================================

# Create an ImageStat object for the greyscale image.
statistics = ImageStat.Stat(gray_image)

# Calculate mean intensity.
mean_intensity = statistics.mean[0]

# Calculate median intensity.
median_intensity = statistics.median[0]

# Calculate standard deviation.
standard_deviation = statistics.stddev[0]

# Display statistical results.
print("Mean Intensity:", round(mean_intensity, 2))
print("Median Intensity:", round(median_intensity, 2))
print("Standard Deviation:", round(standard_deviation, 2))


# ============================================================
# STEP 9: CALCULATE TOTAL NUMBER OF PIXELS
# ============================================================

# Calculate total number of pixels.
total_pixels = gray_image.width * gray_image.height

# Display the total pixel count.
print("Total Pixels:", total_pixels)


# ============================================================
# STEP 10: CALCULATE PIXELS IN EACH INTENSITY RANGE
# ============================================================

# Count dark pixels in the range 0-63.
dark_pixels = sum(histogram[0:64])

# Count middle-intensity pixels in the range 64-191.
middle_pixels = sum(histogram[64:192])

# Count bright pixels in the range 192-255.
bright_pixels = sum(histogram[192:256])


# ============================================================
# STEP 11: CALCULATE PERCENTAGES
# ============================================================

# Calculate percentage of dark pixels.
dark_percentage = (dark_pixels / total_pixels) * 100

# Calculate percentage of middle-intensity pixels.
middle_percentage = (middle_pixels / total_pixels) * 100

# Calculate percentage of bright pixels.
bright_percentage = (bright_pixels / total_pixels) * 100

# Display intensity distribution.
print("\n========== INTENSITY DISTRIBUTION ==========\n")

print(
    "Dark Pixels (0-63):",
    dark_pixels,
    "|",
    round(dark_percentage, 2),
    "%"
)

print(
    "Middle Pixels (64-191):",
    middle_pixels,
    "|",
    round(middle_percentage, 2),
    "%"
)

print(
    "Bright Pixels (192-255):",
    bright_pixels,
    "|",
    round(bright_percentage, 2),
    "%"
)

# Verify that the three percentages approximately equal 100%.
total_percentage = (
    dark_percentage
    + middle_percentage
    + bright_percentage
)

print(
    "Total Percentage:",
    round(total_percentage, 2),
    "%"
)


# ============================================================
# STEP 12: CALCULATE IMAGE ENTROPY
# ============================================================

# Calculate greyscale image entropy.
image_entropy = gray_image.entropy()

# Display entropy value.
print("\nImage Entropy:", round(image_entropy, 4), "bits/pixel")


# ============================================================
# STEP 13: DISPLAY FINAL EXPERIMENT SUMMARY
# ============================================================

print("\n========== EXPERIMENT SUMMARY ==========\n")

print("Original Image:", image_path.name)
print("Dimensions:", image.width, "x", image.height)
print("Format:", image.format)
print("Colour Mode:", image.mode)
print("Bands:", image.getbands())

print("\nMean Intensity:", round(mean_intensity, 2))
print("Median Intensity:", round(median_intensity, 2))
print("Standard Deviation:", round(standard_deviation, 2))

print("\nDark Percentage:", round(dark_percentage, 2), "%")
print("Middle Percentage:", round(middle_percentage, 2), "%")
print("Bright Percentage:", round(bright_percentage, 2), "%")

print("Entropy:", round(image_entropy, 4), "bits/pixel")

print("\nOutput Image:", grayscale_output_path)

print("\n========== EXPERIMENT COMPLETED ==========")


# ============================================================
# STEP 14: CLOSE IMAGE FILES
# ============================================================

# Close the original image file.
image.close()

# Close the greyscale image object.
gray_image.close()