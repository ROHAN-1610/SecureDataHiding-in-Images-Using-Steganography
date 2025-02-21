# 🖼️ Secure Data Hiding in Images Using Steganography

## 🔍 Introduction  
This project is a **Python-based steganography tool** that allows users to **hide and extract secret messages** within images.  
Using **PyQt6** for the GUI, the application provides a simple way to embed data into images securely.

Steganography is a technique of hiding information inside images without altering their visible appearance.  
This project enables users to encode secret messages into `.png` or `.jpg` images and later retrieve them.

---

## 🚀 Features  

- ✅ **Hide Secret Messages** – Encrypt messages within an image.  
- ✅ **Extract Hidden Data** – Retrieve the hidden text from an image.  
- ✅ **Simple & Interactive GUI** – Built with PyQt6 for easy usage.  
- ✅ **Supports Common Image Formats** – Works with `.png` and `.jpg`.  
- ✅ **Secure & Efficient** – Uses OpenCV and NumPy for data processing.  

---

## 🛠️ Installation  

### **1️⃣ Clone the Repository**  
First, download the project from GitHub:  

```sh
git clone https://github.com/ROHAN-1610/SecureDataHiding-in-Images-Using-Steganography.git
cd SecureDataHiding-in-Images-Using-Steganography

### **2️⃣ Create and Activate a Virtual Environment**
python -m venv .venv
.venv\Scripts\activate

 ### **3️⃣ Install Dependencies**
Install all required Python packages:
pip install -r requirements.txt

If you don’t have a requirements.txt, install them manually:
pip install PyQt6 opencv-python numpy

### **🎮 Usage**
**Run the Application**

To launch the GUI:
python stego_gui.py

---

## How to Use?
1.Select an image – Choose a .png , .jpg file , .jpeg file, .bmp file.
2.Enter a secret message – Type the text to be hidden.
3.Click "Hide Data" – The text is embedded into the image.
4.Click "Extract Data" – The hidden message is revealed.
