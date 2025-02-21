#stego_encrypt.py file

import cv2
import os

# Load the cover image where the secret message will be embedded
img = cv2.imread("mypic.jpg")  # Ensure the image exists in the working directory
if img is None:
    print("❌ Error: Cover image not found! Please check the file name.")
    exit()

# Prompt the user to enter a secret message and a password for security
msg = input("📝 Enter the secret message: ")
password = input("🔑 Enter a passcode: ")

# Save the password securely (for simplicity, stored in a file)
with open("Pass.txt", "w") as f:
    f.write(password)

# Embed the secret message into the image using pixel channels
n, m, z = 0, 0, 0  # (row index, column index, color channel)

for char in msg:
    if n >= img.shape[0] or m >= img.shape[1]:
        print("⚠️ Warning: Message is too long to fit in the image.")
        break
    img[n, m, z] = ord(char)  # Store ASCII value of the character in the pixel channel
    n += 1  # Move to the next row
    m += 1  # Move to the next column
    z = (z + 1) % 3  # Cycle through BGR channels

# Save the modified image in PNG format to prevent lossy compression
cv2.imwrite("MyEncryptedImage.png", img)
os.system("start MyEncryptedImage.png")  # Automatically open the encrypted image (Windows only)
print("✅ Secret message successfully embedded into the image!")
