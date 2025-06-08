
# 🖼️ Image Uploader & File Renamer (Tkinter GUI)

This is a simple yet functional **Python GUI tool** built using `Tkinter`, allowing users to:
- Upload multiple image files
- Optionally rename them
- Automatically handle duplicate file names
- Save them in a designated folder (`image/`) inside the project directory

---

## 🚀 Features

- 📂 Upload multiple images at once
- ✏️ Automatically assigns names like `img_1.jpg`, `img_2.png`, etc.
- ⚠️ Checks for existing file names and avoids overwrites by appending suffixes: `img_1(1).jpg`, etc.
- 🖥️ Minimal GUI with a single "Save Image" button

---

## 🧱 Tech Stack

- `Python 3.x`
- `Tkinter` for GUI
- `PIL` (Pillow) for image handling (optional, future use)
- `shutil`, `os` for file management

---

## 📁 Folder Structure

```
your_project/
│
├── main.py          # Main application script
├── README.md        # Project documentation
└── image/           # Folder where images are saved (created automatically)
```

---

## 🛠️ How It Works

1. The GUI launches a small window with a **"Save Image"** button.
2. When clicked, the user can select multiple image files.
3. The program then:
   - Saves each image in the `image/` folder
   - Automatically names files `img_1`, `img_2`, ...
   - If a name already exists, adds `(1)`, `(2)` suffixes
4. Output is printed in the console for verification.

---

## 🧪 Sample Run

```bash
> python main.py
```

**GUI Opens** → Click on "Save Image" → Select multiple images → Images are saved to `/image/` folder.

Console output:

```
File saved as: image/img_1.jpg
File saved as: image/img_2.png
File saved as: image/img_1(1).jpg
```

---

## 📦 Dependencies

Install required packages if you plan to extend with image previews:

```bash
pip install Pillow
```

For basic version (as current), no additional packages are required beyond standard Python.

---

## 🔮 Future Enhancements

- Add preview window for selected images
- Allow custom naming via input box per image
- Drag-and-drop support
- Theme toggle (dark/light)

---

## 👨‍💻 Author

Uttam Singh  
Feel free to modify or extend this mini-project as per your needs!
