# 🎨 Secure Data Hiding in Images Using Steganography

## 🔍 Introduction  
This project is a **Python-based steganography tool** that allows users to **hide and extract secret messages** within images.  
Using **PyQt6** for the GUI, the application provides a simple way to embed data into images securely.

Steganography is a technique of hiding information inside images without altering their visible appearance.  
This project enables users to encode secret messages into `.png`, `.jpg`, `.jpeg`, or `.bmp` images and later retrieve them.

---

## 🚀 Features  

- ✅ **Hide Secret Messages** – Encrypt messages within an image.  
- ✅ **Extract Hidden Data** – Retrieve the hidden text from an image.  
- ✅ **Simple & Interactive GUI** – Built with PyQt6 for easy usage.  
- ✅ **Supports Common Image Formats** – Works with `.png`, `.jpg`, `.jpeg`, and `.bmp`.  
- ✅ **Secure & Efficient** – Uses OpenCV and NumPy for data processing.  

---

## 🛠️ Installation  

### **1️⃣ Clone the Repository**  
First, download the project from GitHub:  

```sh
git clone https://github.com/ROHAN-1610/SecureDataHiding-in-Images-Using-Steganography.git
cd SecureDataHiding-in-Images-Using-Steganography
```

### **2️⃣ Create and Activate a Virtual Environment**  

#### **For Windows:**  
```sh
python -m venv .venv
.venv\Scripts\activate
```

#### **For Linux/macOS:**  
```sh
python3 -m venv .venv
source .venv/bin/activate
```

### **3️⃣ Install Dependencies**  
Install all required Python packages:  
```sh
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install them manually:  
```sh
pip install PyQt6 opencv-python numpy
```

---

## 🎮 Usage  

### **Run the Application**  
To launch the GUI:  
```sh
python stego_gui.py
```

---

## 📝 How to Use?  

1. **Select an image** – Choose a `.png`, `.jpg`, `.jpeg`, or `.bmp` file.  
2. **Enter a secret message** – Type the text to be hidden.  
3. **Click "Hide Data"** – The text is embedded into the image.  
4. **Click "Extract Data"** – The hidden message is revealed.  

---

## 🐛 Dependencies  
This project requires the following libraries:  

| Dependency | Purpose |
|------------|---------|
| `Python 3.11` | Core programming language |
| `PyQt6` | GUI framework |
| `OpenCV (cv2)` | Image processing |
| `NumPy` | Matrix operations |

To install missing dependencies:  
```sh
pip install PyQt6 opencv-python numpy
```

---

## 🏠️ Contributing  
Want to contribute? Follow these steps:  

1. **Fork the repository** on GitHub.  
2. **Create a new branch** for your feature:  
   ```sh
   git checkout -b feature-branch
   ```
3. **Make your changes** and commit them:  
   ```sh
   git commit -m "Added new feature"
   ```
4. **Push to GitHub**:  
   ```sh
   git push origin feature-branch
   ```
5. **Create a Pull Request** and describe your changes.  

---

## 🖼️ Screenshots  

✅ **Main Application GUI**  
![App Screenshot](file:///C:/Users/ROHAN%20VERMA/OneDrive/Pictures/Screenshots/Screenshot%20(32).png)  

✅ **Hiding a Message in an Image**  
![Hiding Data](file:///C:/Users/ROHAN%20VERMA/OneDrive/Pictures/Screenshots/Screenshot%20(33).png)  

✅ **Extracting a Hidden Message**  
![Extracting Data](file:///C:/Users/ROHAN%20VERMA/OneDrive/Pictures/Screenshots/Screenshot%20(33).png)  

---

## 💃 License  
This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it.

---

## 💡 Future Improvements  
- 🔹 **Add Encryption** – Secure messages with a password.  
- 🔹 **Improve Compression** – Reduce image size after encoding.  
- 🔹 **Support More Formats** – Extend to `.tiff`, `.gif`, etc.  
- 🔹 **Command-Line Mode** – Allow hiding/extracting messages without GUI.  

---

## 📩 Contact    
🌐 **GitHub:** [ROHAN-1610](https://github.com/ROHAN-1610)  
📌 **LinkedIn:** [Rohan Verma](https://www.linkedin.com/in/rohan011aab253)  

---

### ⭐ If you find this project useful, don’t forget to **star** the repository on GitHub! ⭐
