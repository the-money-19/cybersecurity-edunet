import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.jpg")

# Retrieve the message length and passcode from the info file
with open("stego_info.txt", "r") as f:
    lines = f.readlines()
msg_length = int(lines[0].strip())
stored_password = lines[1].strip()

# Ask user for passcode to extract the message
pas = input("Enter passcode for decryption: ")

if pas == stored_password:
    # Create reverse mapping from integer to character
    c = {i: chr(i) for i in range(255)}
    
    message = ""
    n, m, z = 0, 0, 0
    
    # Extract the hidden message from the image
    for i in range(msg_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
        
    print("Decrypted message:", message)
else:
    print("Authentication failed. Incorrect passcode.")
