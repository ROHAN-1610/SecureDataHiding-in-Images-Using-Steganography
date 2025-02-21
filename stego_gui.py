import sys
import cv2
import os
import numpy
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog,
    QLineEdit, QTextEdit, QMessageBox
)
from PyQt6.QtGui import QFont


class SteganographyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cover_image_path = ""  # Path of the cover image (original image)
        self.encrypted_image_path = ""  # Path of the encrypted image (image with hidden message)
        self.initUI()

    def initUI(self):
        """Initialize the user interface with buttons, input fields, and labels."""
        self.setWindowTitle("Image Steganography Project")
        self.setGeometry(100, 100, 550, 500)
        self.setStyleSheet("background-color: #2E4053; color: white;")

        layout = QVBoxLayout()
        font = QFont("Arial", 12)

        # Load Cover Image Button
        self.load_cover_btn = QPushButton("\U0001F4C2 Load Image")
        self.load_cover_btn.setFont(font)
        self.load_cover_btn.setStyleSheet("background-color: #1ABC9C; color: white; padding: 10px;")
        self.load_cover_btn.clicked.connect(self.loadCoverImage)
        self.cover_label = QLabel("No file selected")
        self.cover_label.setFont(font)
        layout.addWidget(self.load_cover_btn)
        layout.addWidget(self.cover_label)

        # Input Fields for Secret Message and Password
        self.msg_input = QLineEdit()
        self.msg_input.setPlaceholderText("Enter secret message")
        self.msg_input.setFont(font)
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Enter passcode")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_input.setFont(font)
        layout.addWidget(self.msg_input)
        layout.addWidget(self.pass_input)

        # Encrypt Button
        self.encrypt_btn = QPushButton("\U0001F512 Encrypt Message")
        self.encrypt_btn.setFont(font)
        self.encrypt_btn.setStyleSheet("background-color: #E67E22; color: white; padding: 10px;")
        self.encrypt_btn.clicked.connect(self.encryptMessage)
        layout.addWidget(self.encrypt_btn)

        # Load Encrypted Image Button
        self.load_encrypted_btn = QPushButton("\U0001F4C2 Load Encrypted Image")
        self.load_encrypted_btn.setFont(font)
        self.load_encrypted_btn.setStyleSheet("background-color: #3498DB; color: white; padding: 10px;")
        self.load_encrypted_btn.clicked.connect(self.loadEncryptedImage)
        self.encrypted_label = QLabel("No file selected")
        self.encrypted_label.setFont(font)
        layout.addWidget(self.load_encrypted_btn)
        layout.addWidget(self.encrypted_label)

        # Input Fields for Decryption (Passcode & Message Length)
        self.dec_pass_input = QLineEdit()
        self.dec_pass_input.setPlaceholderText("Enter passcode for decryption")
        self.dec_pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.dec_pass_input.setFont(font)
        self.msg_length_input = QLineEdit()
        self.msg_length_input.setPlaceholderText("Enter message length")
        self.msg_length_input.setFont(font)
        layout.addWidget(self.dec_pass_input)
        layout.addWidget(self.msg_length_input)

        # Decrypt Button
        self.decrypt_btn = QPushButton("\U0001F513 Decrypt Message")
        self.decrypt_btn.setFont(font)
        self.decrypt_btn.setStyleSheet("background-color: #9B59B6; color: white; padding: 10px;")
        self.decrypt_btn.clicked.connect(self.decryptMessage)
        layout.addWidget(self.decrypt_btn)

        # Output Field for Decrypted Message
        self.decrypted_msg = QTextEdit()
        self.decrypted_msg.setReadOnly(True)
        self.decrypted_msg.setFont(font)
        layout.addWidget(self.decrypted_msg)

        self.setLayout(layout)

    def loadCoverImage(self):
        #Load the cover image where the message will be hidden.
        self.cover_image_path, _ = QFileDialog.getOpenFileName(self, "Select Cover Image", "",
                                                               "Images (*.png *.jpg *.jpeg *.bmp)")
        self.cover_label.setText(self.cover_image_path if self.cover_image_path else "No file selected")

    def loadEncryptedImage(self):
        #Load the encrypted image for message extraction
        self.encrypted_image_path, _ = QFileDialog.getOpenFileName(self, "Select Encrypted Image", "",
                                                                   "PNG Files (*.png)")
        self.encrypted_label.setText(self.encrypted_image_path if self.encrypted_image_path else "No file selected")

    def encryptMessage(self):
        #Embed a secret message into the selected image
        if not self.cover_image_path:
            QMessageBox.warning(self, "Error", "Please load a cover image!")
            return

        msg = self.msg_input.text()
        password = self.pass_input.text()
        if not msg or not password:
            QMessageBox.warning(self, "Error", "Please enter both message and passcode!")
            return

        img = cv2.imread(self.cover_image_path)
        if img is None:
            QMessageBox.warning(self, "Error", "Failed to load the image!")
            return

        with open("Pass.txt", "w") as f:
            f.write(password)

        # Embed message in pixel values
        n, m, z = 0, 0, 0
        for char in msg:
            if n >= img.shape[0] or m >= img.shape[1]:
                QMessageBox.warning(self, "Error", "Message too long for the image!")
                return
            img[n, m, z] = ord(char)
            n += 1
            m += 1
            z = (z + 1) % 3

        cv2.imwrite("EncryptedImage.png", img)
        QMessageBox.information(self, "Success", "Message embedded into image: 'EncryptedImage.png'")

    def decryptMessage(self):
        #Extract the hidden message from an encrypted image
        if not self.encrypted_image_path:
            QMessageBox.warning(self, "Error", "Please load an encrypted image!")
            return

        password_input = self.dec_pass_input.text()
        try:
            with open("Pass.txt", "r") as f:
                correct_pass = f.read().strip()
        except:
            QMessageBox.warning(self, "Error", "Password file not found!")
            return

        if password_input != correct_pass:
            QMessageBox.warning(self, "Error", "Incorrect passcode!")
            return

        try:
            length = int(self.msg_length_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid message length!")
            return

        img = cv2.imread(self.encrypted_image_path)
        if img is None:
            QMessageBox.warning(self, "Error", "Failed to load the image!")
            return

        message = ""
        n, m, z = 0, 0, 0
        for _ in range(length):
            message += chr(img[n, m, z])
            n += 1
            m += 1
            z = (z + 1) % 3

        self.decrypted_msg.setText(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SteganographyApp()
    window.show()
    sys.exit(app.exec())
