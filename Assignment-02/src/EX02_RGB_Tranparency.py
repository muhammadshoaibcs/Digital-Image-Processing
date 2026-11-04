
# ============================================================
# EXERCISE 02: RGB CHANNEL REMIX AND TRANSPARENCY
# Subject: Digital Image Processing
# Library: Pillow (PIL)
# Theme: Cyberpunk Digital Artwork
# ============================================================

# Import Path to build reliable input and output file paths.
from pathlib import Path

# Import Image for opening, merging, and saving images.
from PIL import Image

# Import ImageOps for reversing the radial gradient.
from PIL import ImageOps


# ============================================================
# STEP 1: DEFINE INPUT AND OUTPUT PATHS
# ============================================================

# Locate the directory containing this Python script.
script_dir = Path(__file__).resolve().parent

# Locate the main Assignment-02 directory.
assignment_dir = script_dir.parent

# Define the directory containing original input photographs.
input_dir = assignment_dir / "images" / "input"

# Define a separate output directory for Exercise 02.
output_dir = assignment_dir / "images" / "output" / "Exercise-02"

# Automatically create the output directory if needed.
output_dir.mkdir(parents=True, exist_ok=True)

# Define the path to the original photograph.
image_path = input_dir / "original_photo.jpg"

# Confirm that the photograph exists before continuing.
if not image_path.is_file():

    # Stop the program with a helpful message if missing.
    raise FileNotFoundError(
        f"Input image not found: {image_path}"
    )


# ============================================================
# STEP 2: OPEN THE ORIGINAL PHOTOGRAPH
# ============================================================

# Open the original photograph using Pillow.
with Image.open(image_path) as source_image:

    # Convert the photograph to RGB and keep a separate copy.
    original_image = source_image.convert("RGB")

# Store the image dimensions for later operations.
image_width, image_height = original_image.size

# Display basic information about the input image.
print("\n========== ORIGINAL IMAGE ==========\n")
print("Input Image:", image_path.name)
print("Dimensions:", image_width, "x", image_height)
print("Colour Mode:", original_image.mode)

# Save a PNG copy for comparing all versions.
original_image.save(output_dir / "01_original_rgb.png")

print("Original RGB image saved successfully.")


# ============================================================
# PART A: RGB CHANNEL MANIPULATION
# ============================================================

print("\n========== PART A: RGB CHANNELS ==========\n")


# ============================================================
# STEP 3: SPLIT THE RGB CHANNELS
# ============================================================

# Separate the original image into three individual channels.
red_channel, green_channel, blue_channel = original_image.split()

# Display information about the separated channels.
print("Red Channel Mode:", red_channel.mode)
print("Green Channel Mode:", green_channel.mode)
print("Blue Channel Mode:", blue_channel.mode)

# Each individual channel has greyscale intensity values.
print("RGB channels separated successfully.")


# ============================================================
# STEP 4: SWAP THE RED AND BLUE CHANNELS
# ============================================================

# Original channel order is Red, Green, Blue.
# Swap Red and Blue to obtain Blue, Green, Red.
red_blue_swapped = Image.merge(
    "RGB",
    (blue_channel, green_channel, red_channel)
)

# Save the Red-Blue swapped version as PNG.
red_blue_swapped.save(
    output_dir / "02_red_blue_swapped.png"
)

# Confirm successful channel swapping.
print("Red and Blue channels swapped successfully.")
print("New Channel Order: B, G, R")


# ============================================================
# STEP 5: CREATE ANOTHER CREATIVE COLOUR VERSION
# ============================================================

# Rearrange the RGB channels into Green, Red, Blue order.
creative_colour = Image.merge(
    "RGB",
    (green_channel, red_channel, blue_channel)
)

# Save the alternative creative colour version.
creative_colour.save(
    output_dir / "03_creative_colour_remix.png"
)

# Display the new channel order.
print("Second creative colour variation created.")
print("New Channel Order: G, R, B")


# ============================================================
# PART B: RADIAL GRADIENT AND TRANSPARENCY
# ============================================================

print("\n========== PART B: TRANSPARENCY ==========\n")


# ============================================================
# STEP 6: GENERATE A GRAYSCALE RADIAL GRADIENT
# ============================================================

# Generate a radial grayscale gradient in L mode.
# The centre is dark and the edges are bright.
radial_gradient = Image.radial_gradient("L")

# Display the dimensions of the original gradient.
print("Original Gradient Size:", radial_gradient.size)


# ============================================================
# STEP 7: RESIZE THE GRADIENT
# ============================================================

# Resize the gradient to match the photograph dimensions.
radial_gradient = radial_gradient.resize(
    original_image.size,
    Image.Resampling.BICUBIC
)

# Save the resized normal radial gradient.
radial_gradient.save(
    output_dir / "04_radial_gradient.png"
)

# Confirm successful resizing.
print("Resized Gradient Size:", radial_gradient.size)


# ============================================================
# STEP 8: REVERSE THE GRADIENT DIRECTION
# ============================================================

# Invert the grayscale gradient.
# The centre becomes bright and the edges become dark.
inverted_gradient = ImageOps.invert(radial_gradient)

# Save the inverted gradient for comparison.
inverted_gradient.save(
    output_dir / "05_inverted_radial_gradient.png"
)

# Confirm the inversion operation.
print("Inverted radial gradient created.")


# ============================================================
# STEP 9: APPLY NORMAL RADIAL TRANSPARENCY
# ============================================================

# Create an RGBA copy of the original image.
normal_transparency = original_image.convert("RGBA")

# Use the normal radial gradient as the alpha channel.
# The centre becomes more transparent than the edges.
normal_transparency.putalpha(radial_gradient)

# Save the image as RGBA PNG.
normal_transparency.save(
    output_dir / "06_normal_transparency.png"
)

# Display the output image mode.
print("Normal Transparency Mode:", normal_transparency.mode)


# ============================================================
# STEP 10: APPLY INVERTED RADIAL TRANSPARENCY
# ============================================================

# Create another RGBA copy of the original image.
inverted_transparency = original_image.convert("RGBA")

# Apply the inverted radial gradient as the alpha channel.
# The centre remains visible while the edges fade.
inverted_transparency.putalpha(inverted_gradient)

# Save the inverted transparency image.
inverted_transparency.save(
    output_dir / "07_inverted_transparency.png"
)

# Display the output colour mode.
print("Inverted Transparency Mode:", inverted_transparency.mode)


# ============================================================
# CREATIVE CHALLENGE: CYBERPUNK DIGITAL ARTWORK
# ============================================================

print("\n========== CREATIVE CHALLENGE ==========\n")


# ============================================================
# STEP 11: PREPARE THE CYBERPUNK COLOUR VERSION
# ============================================================

# Start from the Red-Blue swapped photograph.
cyberpunk_image = red_blue_swapped.copy()

# Add more contrast to the image using Pillow ImageOps.
cyberpunk_image = ImageOps.autocontrast(
    cyberpunk_image,
    cutoff=1
)

# Convert the creative colour image into RGBA mode.
cyberpunk_image = cyberpunk_image.convert("RGBA")


# ============================================================
# STEP 12: APPLY INVERTED RADIAL TRANSPARENCY
# ============================================================

# Use the inverted gradient as the alpha channel.
# This produces a central-subject fading effect.
cyberpunk_image.putalpha(inverted_gradient)

# Save the final transparent creative artwork.
cyberpunk_image.save(
    output_dir / "08_final_cyberpunk_artwork.png"
)

# Display the final artwork properties.
print("Creative Theme: Cyberpunk")
print("Final Artwork Mode:", cyberpunk_image.mode)
print("Final Artwork Size:", cyberpunk_image.size)

# Confirm the artwork was saved.
print("Final Cyberpunk artwork saved successfully.")


# ============================================================
# STEP 13: DISPLAY EXPERIMENT SUMMARY
# ============================================================

print("\n========== EXPERIMENT SUMMARY ==========\n")

# Display input information.
print("Original Photograph:", image_path.name)
print("Image Size:", image_width, "x", image_height)

# Display the channel arrangements used.
print("Original Channels: R, G, B")
print("First Variation: B, G, R")
print("Second Variation: G, R, B")

# Display the transparency experiment details.
print("Normal Gradient: Transparent Centre")
print("Inverted Gradient: Fading Edges")

# Display the final artwork information.
print("Final Artwork Mode:", cyberpunk_image.mode)
print("Final Artwork Format: PNG")

# Display output destination.
print("Output Directory:", output_dir)

# Indicate completion.
print("\n========== EXPERIMENT COMPLETED ==========")
