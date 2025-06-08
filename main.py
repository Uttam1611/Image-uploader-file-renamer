import os
import shutil
from tkinter import filedialog, simpledialog, Tk

def main():
    root = Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(title="Select multiple images")
    if not file_paths:
        print("No files selected.")
        return

    save_dir = os.path.join(os.getcwd(), "image")
    os.makedirs(save_dir, exist_ok=True)

    for i, file_path in enumerate(file_paths, start=1):
        ext = os.path.splitext(file_path)[1]

        default_name = f"img_{i}"
        user_input = simpledialog.askstring("Rename", f"Enter name for image {i} (Leave blank for default):")

        if user_input:
            base_name = user_input.strip()
        else:
            base_name = default_name

        counter = 1
        dest_path = os.path.join(save_dir, f"{base_name}{ext}")
        while os.path.exists(dest_path):
            dest_path = os.path.join(save_dir, f"{base_name}({counter}){ext}")
            counter += 1

        shutil.copy(file_path, dest_path)
        print(f"File saved as: {os.path.basename(dest_path)}")

if __name__ == "__main__":
    main()
