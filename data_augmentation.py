import os
import random
import numpy as np
from PIL import Image, ImageEnhance, ImageOps

# Define the folder containing the input images
input_folder = r"D:\MCIT\581\extra project\train\New folder\output_frames"

# Define the folder to export the augmented images to
output_folder = r"D:\MCIT\581\extra project\train\New folder\New folder"

# Define the number of augmented images to generate per input image
num_augmentations = 2

# Define the range of rotation angles in degrees
rotation_range = (-0.5, 0.5)

# Define the range of shear angles in degrees
shear_range = (-0.5, 0.5)

# Define the range of color enhancements
brightness_range = (0.5, 1.5)
contrast_range = (0.5, 1.5)
sharpness_range = (0.5, 1.5)

# Define the range of cropping ratios
crop_range = (0.8, 1.0)

# Define a list of image file extensions to process
extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]

# Loop through all the image files in the input folder
for filename in os.listdir(input_folder):
    if any(filename.lower().endswith(ext) for ext in extensions):
        # Open the input image file
        image = Image.open(os.path.join(input_folder, filename)).convert('RGB')
        # Loop through the number of augmentations to generate
        for i in range(num_augmentations):
            # Apply random rotation
            angle = random.uniform(*rotation_range)
            rotated_image = image.rotate(angle)

            # Apply random shear
            shear = random.uniform(*shear_range)
            sheared_image = rotated_image.transform(
                rotated_image.size, Image.AFFINE, (1, shear, 0, 0, 1, 0))

            # Apply random color enhancement
            brightness = random.uniform(*brightness_range)
            contrast = random.uniform(*contrast_range)
            sharpness = random.uniform(*sharpness_range)
            enhancer = ImageEnhance.Brightness(
                ImageEnhance.Contrast(
                    ImageEnhance.Sharpness(sheared_image).enhance(sharpness)
                ).enhance(contrast)
            ).enhance(brightness)

            # Apply random cropping
            crop_ratio = random.uniform(*crop_range)
            crop_size = (int(enhancer.width * crop_ratio),
                         int(enhancer.height * crop_ratio))
            cropped_image = ImageOps.fit(
                enhancer, crop_size, centering=(0.5, 0.5))

            # Save the augmented image to the output folder
            output_filename = os.path.splitext(filename)[0] + \
                f"_aug{i:02d}.jpg"
            output_path = os.path.join(output_folder, output_filename)
            cropped_image.save(output_path)
