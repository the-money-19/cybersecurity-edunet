import cv2
import os

# Read the original image
img = cv2.imread("mypic.jpg")  # Replace with your image path

# Get the secret message and passcode from the user
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create simple dictionaries for conversion between characters and integers
d = {chr(i): i for i in range(255)}

# Initialize position indexes for embedding
n, m, z = 0, 0, 0

# Embed each character of the message into the image pixel values
for char in msg:
    img[n, m, z] = d[char]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save the encrypted image and also store the message length and password in a separate file
cv2.imwrite("encryptedImage.jpg", img)
with open("stego_info.txt", "w") as f:
    f.write(f"{len(msg)}\n")
    f.write(password)

# Optionally open the encrypted image (Windows only)
os.system("start encryptedImage.jpg")
