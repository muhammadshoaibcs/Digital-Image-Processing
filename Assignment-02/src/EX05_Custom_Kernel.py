"""Optional Advanced Challenge: 3x3 custom sharpening convolution using Pillow.
"""

# Import Path so file locations do not depend on the terminal directory.
from pathlib import Path

# Import Pillow modules for images, filters, comparison, and labels.
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps, ImageStat


# ============================================================
# STEP 1: DEFINE INPUT AND OUTPUT PATHS
# ============================================================

# Find the folder where this script is saved (Assignment-02/src).
script_dir = Path(__file__).resolve().parent

# Move one directory up to Assignment-02.
assignment_dir = script_dir.parent

# Use the same original photograph as Exercises 1-4.
input_path = assignment_dir / "images" / "input" / "original_photo.jpg"

# Keep optional-challenge outputs separate from required exercises.
output_dir = assignment_dir / "images" / "output" / "Advanced-Challenge"

# Create the output directory if necessary.
output_dir.mkdir(parents=True, exist_ok=True)

# Stop with a clear message if the input file is absent.
if not input_path.is_file():
    raise FileNotFoundError(f"Original photograph not found: {input_path}")


# ============================================================
# STEP 2: PREPARE THE IMAGE
# ============================================================

# Open the photograph and correct possible phone-camera EXIF rotation.
with Image.open(input_path) as source_image:
    oriented_image = ImageOps.exif_transpose(source_image)

    # Convert to RGB because Pillow's Kernel filter supports RGB images.
    rgb_image = oriented_image.convert("RGB")

# Resize and crop to 400x300, matching the previous exercise's dimensions.
reference_image = ImageOps.fit(
    rgb_image,
    size=(400, 300),
    method=Image.Resampling.LANCZOS,
    centering=(0.5, 0.5),
)

# Save the unfiltered reference for visual comparison.
reference_image.save(output_dir / "00_reference.png")


# ============================================================
# STEP 3: DESIGN THREE CUSTOM 3x3 SHARPENING KERNELS
# ============================================================

# Mild sharpening: centre = 3; direct neighbours = -0.5.
# Sum of weights: 3 - (4 * 0.5) = 1.
mild_kernel_values = (
    0, -0.5, 0,
    -0.5, 3, -0.5,
    0, -0.5, 0,
)

# Main custom sharpening kernel: centre = 5; neighbours = -1.
# Sum of weights: 5 - 4 = 1.
custom_kernel_values = (
    0, -1, 0,
    -1, 5, -1,
    0, -1, 0,
)

# Strong sharpening: centre = 7; neighbours = -1.5.
# Sum of weights: 7 - (4 * 1.5) = 1.
strong_kernel_values = (
    0, -1.5, 0,
    -1.5, 7, -1.5,
    0, -1.5, 0,
)

# Create the custom filters; scale=1 preserves the specified weights.
mild_filter = ImageFilter.Kernel(
    size=(3, 3), kernel=mild_kernel_values, scale=1, offset=0
)
custom_filter = ImageFilter.Kernel(
    size=(3, 3), kernel=custom_kernel_values, scale=1, offset=0
)
strong_filter = ImageFilter.Kernel(
    size=(3, 3), kernel=strong_kernel_values, scale=1, offset=0
)


# ============================================================
# STEP 4: APPLY EACH FILTER TO THE SAME REFERENCE IMAGE
# ============================================================

# Apply our three custom kernels independently.
mild_image = reference_image.filter(mild_filter)
custom_image = reference_image.filter(custom_filter)
strong_image = reference_image.filter(strong_filter)

# Apply Pillow's built-in SHARPEN filter to the same reference.
builtin_image = reference_image.filter(ImageFilter.SHARPEN)

# Save every result separately for comparison and the Word report.
mild_image.save(output_dir / "01_custom_mild.png")
custom_image.save(output_dir / "02_custom_sharpen.png")
strong_image.save(output_dir / "03_custom_strong.png")
builtin_image.save(output_dir / "04_pillow_sharpen.png")


# ============================================================
# STEP 5: CALCULATE A DESCRIPTIVE PIXEL-CHANGE METRIC
# ============================================================

def mean_absolute_change(original, filtered):
    """Average absolute RGB channel change versus the same input image.

    This measures how much a filter changes pixels, NOT image quality.
    """
    difference = ImageChops.difference(original, filtered)
    means = ImageStat.Stat(difference).mean  # One mean for R, G and B.
    return sum(means) / len(means)


print("\n========== OPTIONAL CUSTOM KERNEL CHALLENGE ==========")
print("Original file:", input_path.name)
print("Reference dimensions:", reference_image.size)
print("\nFilter                      Mean absolute RGB change")
print("----------------------------------------------------")

# Compare how strongly each method modifies pixel values.
for label, result in [
    ("Mild custom kernel", mild_image),
    ("Main custom kernel", custom_image),
    ("Strong custom kernel", strong_image),
    ("Pillow built-in SHARPEN", builtin_image),
]:
    change = mean_absolute_change(reference_image, result)
    print(f"{label:<28}{change:>10.4f}")

print("\nNote: More pixel change does NOT automatically mean better sharpness.")


# ============================================================
# STEP 6: CREATE A COMPARISON GRID FOR THE WORD REPORT
# ============================================================

# Set a header height above each image for a readable label.
label_height = 28

# Make a 2x2 comparison grid (two columns, two rows).
comparison_grid = Image.new(
    "RGB", (400 * 2, (300 + label_height) * 2), "white"
)

# Prepare the four images to compare side by side.
panels = [
    ("Original reference", reference_image),
    ("Custom sharpening 3x3", custom_image),
    ("Pillow SHARPEN", builtin_image),
    ("Strong custom sharpening", strong_image),
]

# Draw panel labels and paste each image into its grid position.
draw = ImageDraw.Draw(comparison_grid)
for index, (label, panel_image) in enumerate(panels):
    col = index % 2
    row = index // 2
    x = col * 400
    y = row * (300 + label_height)
    draw.text((x + 8, y + 8), label, fill="black")
    comparison_grid.paste(panel_image, (x, y + label_height))

# Save the image grid for easy insertion into Word.
comparison_grid.save(output_dir / "05_comparison_grid.png")


# ============================================================
# STEP 7: PRINT THE FINAL SUMMARY
# ============================================================

print("\nMain 3x3 custom sharpening kernel:")
print(" 0  -1   0")
print("-1   5  -1")
print(" 0  -1   0")
print("\nGenerated files: 5 separate images + 1 comparison grid")
print("Output directory:", output_dir)
print("\n========== EXPERIMENT COMPLETED ==========")
