# ============================================================
# EXERCISE 04: IMAGE RESTORATION CHALLENGE
# Question: Which filter works best?
# ============================================================

# Import built-in tools for reproducible random noise and file paths.
import random
from pathlib import Path

# Import Pillow modules for image transformation and evaluation.
from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps


# ============================================================
# STEP 1: DEFINE REPOSITORY FILE PATHS
# ============================================================

# Resolve the location of this Python file, regardless of terminal location.
script_dir = Path(__file__).resolve().parent

# The script is expected in Assignment-02/src/.
assignment_dir = script_dir.parent

# Use the same photograph from Exercises 01, 02 and 03.
input_path = assignment_dir / "images" / "input" / "original_photo.jpg"

# Keep all generated images in a separate Exercise 04 output folder.
output_dir = assignment_dir / "images" / "output" / "Exercise-04"
output_dir.mkdir(parents=True, exist_ok=True)

# Check the input file before attempting image processing.
if not input_path.is_file():
    raise FileNotFoundError(f"Cannot find input image: {input_path}")


# ============================================================
# STEP 2: DEFINE AN RGB MEAN SQUARED ERROR FUNCTION
# ============================================================

def calculate_mse(reference_image, processed_image):
    """Calculate RGB MSE across every pixel and colour channel."""

    # Both images must have the same dimensions and RGB colour mode.
    if reference_image.size != processed_image.size:
        raise ValueError("MSE requires images of identical dimensions.")
    if reference_image.mode != "RGB" or processed_image.mode != "RGB":
        raise ValueError("MSE requires both images to be in RGB mode.")

    # Calculate the absolute difference of corresponding RGB values.
    difference_image = ImageChops.difference(reference_image, processed_image)

    # For RGB, the histogram has 256 bins for each of three channels.
    difference_histogram = difference_image.histogram()

    # Sum (squared difference) x (frequency) across all colour channels.
    sum_squared_errors = 0
    for bin_index, pixel_count in enumerate(difference_histogram):
        difference_value = bin_index % 256
        sum_squared_errors += (difference_value ** 2) * pixel_count

    # The problem requires division by width x height x 3.
    total_colour_values = reference_image.width * reference_image.height * 3
    return sum_squared_errors / total_colour_values


# ============================================================
# PART A: GENERATE A REPRODUCIBLE SALT-AND-PEPPER IMAGE
# ============================================================

# Open the source photograph and handle camera EXIF orientation.
with Image.open(input_path) as source_image:
    correctly_oriented = ImageOps.exif_transpose(source_image)
    original_image = correctly_oriented.convert("RGB")

# Fit and crop to exactly 400 x 300, creating the clean reference.
image_size = (400, 300)
clean_image = ImageOps.fit(
    original_image,
    size=image_size,
    method=Image.Resampling.LANCZOS,
    centering=(0.5, 0.5)
)
clean_image.save(output_dir / "00_clean_reference.png")

# Exactly 3% of 120,000 source pixel positions will be selected.
noise_fraction = 0.03
total_pixels = clean_image.width * clean_image.height
number_of_noisy_pixels = round(total_pixels * noise_fraction)

# Fix the random-number seed to obtain the same noise on every run.
random.seed(42)

# Select distinct pixel positions (no pixel is selected twice).
selected_locations = random.sample(range(total_pixels), number_of_noisy_pixels)

# Copy the clean reference and modify only this separate copy.
noisy_image = clean_image.copy()
noisy_pixels = noisy_image.load()

# Replace each selected pixel with full black ('pepper') or white ('salt').
for pixel_index in selected_locations:
    x = pixel_index % clean_image.width
    y = pixel_index // clean_image.width
    if random.randint(0, 1) == 0:
        noisy_pixels[x, y] = (0, 0, 0)
    else:
        noisy_pixels[x, y] = (255, 255, 255)

# Save the noisy version for comparison with the clean reference.
noisy_image.save(output_dir / "01_noisy_salt_pepper.png")


# ============================================================
# PART B: APPLY FILTERS AND ONE IMAGE ENHANCEMENT
# ============================================================

# Median filtering replaces the centre with the neighbourhood median.
median_image = noisy_image.filter(ImageFilter.MedianFilter(size=3))
median_image.save(output_dir / "02_median_filter.png")

# Gaussian filtering averages nearby pixel values with Gaussian weights.
gaussian_image = noisy_image.filter(ImageFilter.GaussianBlur(radius=1))
gaussian_image.save(output_dir / "03_gaussian_blur.png")

# Unsharp masking is applied to the MEDIAN-DENOISED result, not noisy input.
unsharp_image = median_image.filter(
    ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3)
)
unsharp_image.save(output_dir / "04_unsharp_after_median.png")

# Compare one additional ImageEnhance adjustment on the SAME median result.
# Contrast factor 1.10 means an approximately 10% stronger contrast setting.
contrast_image = ImageEnhance.Contrast(median_image).enhance(1.10)
contrast_image.save(output_dir / "05_contrast_after_median.png")


# ============================================================
# PART C: MEASURE RGB MSE AGAINST THE CLEAN REFERENCE
# ============================================================

# Keep descriptive labels for the assignment's comparison table.
methods = [
    ("Original noisy image", noisy_image),
    ("Median Filter", median_image),
    ("Gaussian Blur", gaussian_image),
    ("Unsharp Mask (after median)", unsharp_image),
    ("Contrast 1.10 (after median)", contrast_image),
]

# Evaluate every result using exactly the same clean image.
scores = {}
for method_name, result_image in methods:
    scores[method_name] = calculate_mse(clean_image, result_image)

# Find the lowest MSE among the three specified filtering pipelines.
main_filters = ["Median Filter", "Gaussian Blur", "Unsharp Mask (after median)"]
best_method = min(main_filters, key=lambda name: scores[name])

# Format the actual results for easy copying into Microsoft Word.
report_lines = [
    "EXERCISE 04: IMAGE RESTORATION RESULTS",
    f"Input image: {input_path.name}",
    f"Clean reference size: {clean_image.width} x {clean_image.height}",
    f"Random seed: 42",
    f"Noise: {number_of_noisy_pixels} of {total_pixels} pixels (3.00%)",
    "All MSE values use RGB channel differences against the clean image.",
    "",
    f"{'Method':<32} {'MSE':>14}",
    "-" * 48,
]
for method_name, _ in methods:
    report_lines.append(f"{method_name:<32} {scores[method_name]:>14.4f}")
report_lines += [
    "",
    f"Lowest MSE among the three filtering pipelines: {best_method}",
    "Visual quality and edge preservation must be assessed from the images.",
]

# Print the results in the terminal.
print("\n".join(report_lines))

# Save the same results as a text file for the Word report.
(output_dir / "07_mse_results.txt").write_text(
    "\n".join(report_lines) + "\n", encoding="utf-8"
)


# ============================================================
# PART D: CREATE A VISUAL COMPARISON SHEET FOR WORD
# ============================================================

# Put the clean image and all five variants in a 3 x 2 layout.
panels = [("Clean reference", clean_image)] + methods

# Leave enough top margin above each panel for its title.
label_height = 34
columns = 3
rows = 2
panel_width, panel_height = image_size

# Create the summary sheet using Pillow only (no Matplotlib needed).
sheet = Image.new(
    "RGB",
    (columns * panel_width, rows * (panel_height + label_height)),
    (245, 245, 245)
)
draw = ImageDraw.Draw(sheet)

# Place each result on the sheet, labelled for easy inspection.
for index, (label, panel_image) in enumerate(panels):
    column = index % columns
    row = index // columns
    x = column * panel_width
    y = row * (panel_height + label_height)
    draw.text((x + 8, y + 10), label, fill=(10, 10, 10))
    sheet.paste(panel_image, (x, y + label_height))

# Save the 1200 x 668 pixel visual comparison sheet.
sheet.save(output_dir / "06_visual_comparison_grid.png")

# End with paths and a useful final status message.
print("\nVisual comparison saved: 06_visual_comparison_grid.png")
print("MSE report saved: 07_mse_results.txt")
print("All outputs saved in:", output_dir)
print("\n========== EXPERIMENT COMPLETED ==========")
