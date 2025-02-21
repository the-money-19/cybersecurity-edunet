🔒 Image Steganography Using OpenCV
Overview
This project shows how you can hide secret messages inside images using a simple Python script with OpenCV. It lets you securely encrypt a message by embedding it in an image and then decrypt it later with a password.

What’s Inside
 Python: The main programming language we use.
 OpenCV: Handles image processing tasks.
 OS Module: Manages file operations like saving images.
 String Module: Helps with encoding and decoding characters for the hidden message.

Cool Features
 Hide secret messages inside an image.
 Password protection ensures only you (or the right person) can read the message.
 A lightweight, command-line tool that’s easy to use.
 Unique method using pixel manipulation to keep things under the radar.

 How It’s Organized
  Image-Stegano/
  ├── stego.py             # The script that encrypts and decrypts messages
  ├── mypic.jpg            # A sample image to work with
  ├── encryptedImage.jpg   # The output image containing the hidden message
  └── README.md            # This file!

How to Get Started
  1. Set Up
     Make sure you have Python installed. Then, install OpenCV by running:
      pip install opencv-python
2. Encrypt a Message
     Run the script:
      python stego.py
   When prompted, enter your secret message and a password. The script will create an image called encryptedImage.jpg with your hidden message.
3. Decrypt the Message
  To read your secret message, run the script again and provide the correct password when asked.
