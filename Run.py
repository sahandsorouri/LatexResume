import subprocess
import os

# Define the base filename
base_filename = "Sahand Sorouri - Product Manager"

# Step 1: Convert .tex to .pdf
subprocess.run(["pdflatex", f"{base_filename}.tex"])

# Step 2: Convert .pdf to .png with high resolution
subprocess.run(["magick", "convert", "-density", "300",
                f"{base_filename}.pdf", "-quality", "100",
                "-flatten",  # Helps with PDFs that have transparency issues
                f"{base_filename}.png"])


# Step 4: Remove irrelevant files
for extension in ['.aux', '.log', '.out']:
    try:
        os.remove(f"{base_filename}{extension}")
    except FileNotFoundError:
        # If the file doesn't exist, just skip it
        pass

print("Conversion to PDF, PNG, and HTML completed.")
