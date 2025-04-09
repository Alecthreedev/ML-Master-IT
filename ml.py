import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract

# If you're on Windows, uncomment and set your Tesseract path here:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def choose_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
    )
    if file_path:
        extract_text(file_path)

def extract_text(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, text)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text:\n{e}")

# Create GUI window
root = tk.Tk()
root.title("Image to Text (OCR)")

# Create GUI elements
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

choose_btn = tk.Button(frame, text="Choose Image", command=choose_file, width=20)
choose_btn.pack(pady=10)

text_area = tk.Text(frame, height=20, width=60, wrap=tk.WORD)
text_area.pack()

root.mainloop()
