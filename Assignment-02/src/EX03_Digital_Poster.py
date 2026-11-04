
# ============================================================
# EXERCISE 03: IMAGE DESIGN STUDIO - DIGITAL POSTER
# Subject: Digital Image Processing
# Library: Pillow (Image and ImageOps)
# ============================================================

# Import Path for managing input and output file paths.
from pathlib import Path

# Import Image for opening and saving photographs.
from PIL import Image

# Import ImageOps for image composition and colour processing.
from PIL import ImageOps


# ============================================================
# STEP 1: DEFINE PROJECT DIRECTORIES
# ============================================================

# Get the directory containing this Python file.
script_dir = Path(__file__).resolve().parent

# Locate the Assignment-02 directory.
assignment_dir = script_dir.parent

# Define the input image directory.
input_dir = assignment_dir / "images" / "input"

# Define a separate output folder for Exercise 03.
output_dir = assignment_dir / "images" / "output" / "Exercise-03"

# Create the output directory if it does not exist.
output_dir.mkdir(parents=True, exist_ok=True)

# Define the original photograph's path.
image_path = input_dir / "original_photo.jpg"

# Check whether the input photograph exists.
if not image_path.is_file():
    raise FileNotFoundError(
        f"Input photograph was not found: {image_path}"
    )


# ============================================================
# STEP 2: OPEN THE ORIGINAL PHOTOGRAPH
# ============================================================

# Open the photograph using Pillow.
with Image.open(image_path) as source_image:

    # Respect the EXIF orientation stored by a phone camera.
    corrected_image = ImageOps.exif_transpose(source_image)

    # Convert the photograph to RGB mode.
    original_image = corrected_image.convert("RGB")

# Display the original image information.
print("\n========== ORIGINAL IMAGE ==========\n")

print("Image Name:", image_path.name)
print("Original Size:", original_image.size)
print("Colour Mode:", original_image.mode)


# ============================================================
# STEP 3: DEFINE POSTER SETTINGS
# ============================================================

# Set the required output size to 512 x 512 pixels.
poster_size = (512, 512)

# Choose a dark background for the padded version.
background_colour = (28, 35, 48)

# Use high-quality Lanczos resampling.
resampling_method = Image.Resampling.LANCZOS

# Display the target dimensions.
print("\nTarget Poster Size:", poster_size)


# ============================================================
# PART A: ASPECT RATIO AND IMAGE COMPOSITION
# ============================================================

print("\n========== PART A: IMAGE COMPOSITION ==========\n")


# ============================================================
# STEP 4: VERSION A - PRESERVE THE ENTIRE PHOTOGRAPH
# ============================================================

# Resize the image to fit inside a square canvas.
# Preserve the whole photograph and its aspect ratio.
# Fill unused space with the chosen background colour.
padded_image = ImageOps.pad(
    original_image,
    size=poster_size,
    method=resampling_method,
    color=background_colour,
    centering=(0.5, 0.5)
)

# Save the padded image before creative colour processing.
padded_image.save(
    output_dir / "01_padded_original.png"
)

# Display composition information.
print("Version A: ImageOps.pad()")
print("Output Size:", padded_image.size)
print("Entire Original Image Preserved: Yes")


# ============================================================
# STEP 5: VERSION B - FILL THE ENTIRE SQUARE CANVAS
# ============================================================

# Crop the original photograph to a square composition.
# Resize the cropped result to exactly 512 x 512 pixels.
# Use centred cropping.
fitted_image = ImageOps.fit(
    original_image,
    size=poster_size,
    method=resampling_method,
    centering=(0.5, 0.5)
)

# Save the fitted image before creative colour processing.
fitted_image.save(
    output_dir / "02_fitted_original.png"
)

# Display composition information.
print("\nVersion B: ImageOps.fit()")
print("Output Size:", fitted_image.size)
print("Entire Canvas Filled: Yes")
print("Original Image Cropped: Yes")


# ============================================================
# PART B: CREATIVE COLOUR PROCESSING
# ============================================================

print("\n========== PART B: COLOUR PROCESSING ==========\n")


# ============================================================
# STEP 6: VERSION A - CLASSIC DUOTONE POSTER
# ============================================================

# Convert the padded square image into grayscale.
grayscale_image = ImageOps.grayscale(padded_image)

# Map grayscale values into a warm duotone palette.
# Dark pixels become dark brown.
# Bright pixels become warm cream.
classic_poster = ImageOps.colorize(
    grayscale_image,
    black=(43, 34, 39),
    white=(245, 220, 178)
)

# Save the first completed 512 x 512 poster.
classic_poster.save(
    output_dir / "03_final_classic_poster.png"
)

# Display processing details.
print("Version A - Classic Exhibition Poster")
print("Techniques: Grayscale + Colorize")
print("Size:", classic_poster.size)
print("Mode:", classic_poster.mode)


# ============================================================
# STEP 7: VERSION B - CYBERPUNK GRAPHIC POSTER
# ============================================================

# Enhance the contrast of the cropped photograph.
contrast_image = ImageOps.autocontrast(
    fitted_image,
    cutoff=1
)

# Reduce the number of colour levels per RGB channel.
# Retain 3 bits per channel instead of 8 bits.
posterized_image = ImageOps.posterize(
    contrast_image,
    bits=3
)

# Convert the posterized image to grayscale.
cyberpunk_gray = ImageOps.grayscale(posterized_image)

# Apply a three-colour Cyberpunk palette.
# Shadows become dark blue.
# Midtones become purple/magenta.
# Highlights become cyan.
cyberpunk_poster = ImageOps.colorize(
    cyberpunk_gray,
    black=(14, 18, 57),
    mid=(188, 42, 168),
    white=(99, 239, 245)
)

# Save the second completed 512 x 512 poster.
cyberpunk_poster.save(
    output_dir / "04_final_cyberpunk_poster.png"
)

# Display processing details.
print("\nVersion B - Cyberpunk Poster")
print("Techniques: Autocontrast + Posterize + Colorize")
print("Size:", cyberpunk_poster.size)
print("Mode:", cyberpunk_poster.mode)


# ============================================================
# STEP 8: VERIFY OUTPUT FILES
# ============================================================

print("\n========== OUTPUT VERIFICATION ==========\n")

# Define the four images generated by the experiment.
output_files = [
    "01_padded_original.png",
    "02_fitted_original.png",
    "03_final_classic_poster.png",
    "04_final_cyberpunk_poster.png"
]

# Open each output image and verify its size and mode.
for filename in output_files:

    # Define the complete output file path.
    file_path = output_dir / filename

    # Open the saved image for validation.
    with Image.open(file_path) as result:

        # Display the saved file information.
        print(filename)
        print("  Dimensions:", result.size)
        print("  Mode:", result.mode)

        # Check whether the saved image is exactly 512 x 512.
        assert result.size == poster_size, (
            f"Incorrect dimensions in {filename}"
        )


# ============================================================
# STEP 9: DISPLAY FINAL SUMMARY
# ============================================================

print("\n========== EXPERIMENT SUMMARY ==========\n")

print("Original Photograph:", image_path.name)
print("Original Dimensions:", original_image.size)
print("Required Poster Dimensions:", poster_size)

print("\nVersion A: Classic Exhibition Poster")
print("Composition: ImageOps.pad()")
print("Colour Processing: Grayscale + Colorize")
print("Original Composition: Preserved")

print("\nVersion B: Cyberpunk Poster")
print("Composition: ImageOps.fit()")
print("Colour Processing: Autocontrast + Posterize + Colorize")
print("Original Composition: Cropped")

print("\nTotal Output Images:", len(output_files))
print("Output Directory:", output_dir)

print("\n========== EXPERIMENT COMPLETED ==========")
