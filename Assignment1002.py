# Author: Barini Simhadri
# Date: 21-03-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/dINNm4koBoI

import numpy as np
import cv2
import matplotlib.pyplot as plt

def salt_n_pepper(img, p):
    """
    Add salt-and-pepper noise to the input image.
    """
    noisy_img = np.copy(img)  # Create a copy of the input image
    # Generate random mask where pixels become either salt or pepper based on probability p
    salt_pepper = np.random.rand(*img.shape[:2])
    noisy_img[salt_pepper < p] = 0  # Salt noise (black pixels)
    noisy_img[salt_pepper > 1 - p] = 255  # Pepper noise (white pixels)
    return noisy_img

def median_filter(img, W):
    """
    Apply median filtering on the noisy input image.
    """
    denoised_img = np.copy(img)  # Create a copy of the input image
    for i in range(W//2, img.shape[0] - W//2):
        for j in range(W//2, img.shape[1] - W//2):
            # Extract the neighborhood window
            neighborhood = img[i - W//2: i + W//2 + 1, j - W//2: j + W//2 + 1]
            # Apply median filtering
            denoised_img[i, j] = np.median(neighborhood)
    return denoised_img

# Load the image
img_path = r"C:/Users/bunty/Desktop/DSC430/week_10/hw/Depaul.jpg"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Test salt-and-pepper noise addition with different probabilities
p_values = [0.01, 0.05, 0.1]  # Noise probabilities
noisy_images = []
for p in p_values:
    noisy_img = salt_n_pepper(img, p)
    noisy_images.append(noisy_img)

# Test median filtering with different window sizes
W_values = [3, 5, 7]  # Window sizes
denoised_images = []
for noisy_img in noisy_images:
    denoised_img = median_filter(noisy_img, W_values[0])  # Apply median filter with the first window size
    denoised_images.append(denoised_img)

# Display the original, noisy, and denoised images
plt.figure(figsize=(12, 6))

plt.subplot(1, len(noisy_images)+1, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

for i, noisy_img in enumerate(noisy_images):
    plt.subplot(1, len(noisy_images)+1, i+2)
    plt.imshow(noisy_img, cmap='gray')
    plt.title(f'Noisy Image (p={p_values[i]})')
    plt.axis('off')

plt.figure(figsize=(12, 6))

for i, denoised_img in enumerate(denoised_images):
    plt.subplot(1, len(denoised_images), i+1)
    plt.imshow(denoised_img, cmap='gray')
    plt.title(f'Denoised Image (W={W_values[0]})')
    plt.axis('off')

plt.show()