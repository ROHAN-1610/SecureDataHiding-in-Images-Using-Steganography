#stego_decrypt.py file

import cv2

# Load the encrypted image containing the hidden message
img = cv2.imread("MyEncryptedImage.png")
if img is None:
    print("❌ Error: Encrypted image not found! Please check the file name.")
    exit()

# Retrieve the stored passcode from the file
try:
    with open("Pass.txt", "r") as f:
        correct_pass = f.read().strip()
except FileNotFoundError:
    print("❌ Error: Password file is missing! Cannot proceed with decryption.")
    exit()

# Ask the user to input the passcode for decryption
pas = input("🔑 Enter passcode for Decryption: ")

# Verify if the entered passcode is correct
if pas != correct_pass:
    print("🚫 Incorrect passcode. Access denied!")
    exit()

# Ask the user for the length of the hidden message
try:
    length = int(input("📏 Enter the secret message length: "))
    if length <= 0:
        raise ValueError
except ValueError:
    print("❌ Invalid input! Message length must be a positive integer.")
    exit()

# Extract the hidden message from the image
message = ""
n, m, z = 0, 0, 0  # (row index, column index, color channel)

for i in range(length):
    if n >= img.shape[0] or m >= img.shape[1]:
        print("⚠️ Warning: Reached image boundary before reading the full message.")
        break
    message += chr(img[n, m, z])  # Convert ASCII values back to characters
    n += 1
    m += 1
    z = (z + 1) % 3  # Cycle through BGR channels

# Display the extracted message
print("✅ Decrypted message:", message)
