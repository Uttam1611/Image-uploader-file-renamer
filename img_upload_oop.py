import glob
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import os,shutil

class main():
    def __init__(self,root):
        self.root=root
        self.root.title("Option window")
        self.root.geometry('160x50+190+30')
        self.root.resizable(False,False)
        self.root.config(bg="#4A4848")
        
        # self.fldr_exists()

        Button(self.root, text="Save Image", font=("goudy old style", 20, "bold"), bg="#eb5834", fg="white", cursor="hand2",bd=10,relief=RIDGE,command=self.save_img).pack()

        
        
        # Button(self.root, text="Rename Image", font=("goudy old style", 20, "bold"), bg="#e4f2e5", fg="blue", cursor="hand2",bd=10,relief=RIDGE,command=self.rename).place(x=320, y=270, width=200, height=100)
        # Button(self.root, text="STUDENT", font=("goudy old style", 20, "bold"), bg="#0c8518", fg="white", cursor="hand2",bd=10,relief=RIDGE,command=self.std_win).place(x=570, y=270, width=200, height=100)


    # def open_img(self):
    #     file_path = filedialog.askopenfilenames()
    #     print("Selected file/s:",file_path)
        # img = Image.open(self.file_path)
        # img.show()
        # self.root.destroy()
        # self.new_win = Tk()
        # self.new_obj = Tlogin(self.new_win)

        

    def save_img(self):
        file_paths = filedialog.askopenfilenames(title="Select images")
        save_dir = os.path.join(os.getcwd(), "image")
        os.makedirs(save_dir, exist_ok=True)

        for i, file in enumerate(file_paths, start=1):
            ext = os.path.splitext(file)[1]
            base_name = f"img_{i}"
            counter = 1
            dest_path = os.path.join(save_dir, f"{base_name}{ext}")

            while os.path.exists(dest_path):
                dest_path = os.path.join(save_dir, f"{base_name}({counter}){ext}")
                counter += 1

            shutil.copy(file, dest_path)
            print(f"File saved as: {dest_path}")

    
    # ===================Create a folder to save images in if not exist=========================
    # def fldr_exists(self):
    #     imgfexists = False
    #     self.cwd = os.getcwd()
    #     dir_list = os.listdir(self.cwd)
    #     for dir in dir_list:
    #         if os.path.isdir(dir):
    #             image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp"]
    #             for ext in image_extensions:
    #                 if glob.glob(os.path.join(dir, ext)):
    #                     imgfexists = True

    #     if(imgfexists is False):
    #         os.mkdir('image')
        

if __name__=="__main__":
    root=Tk()
    obj=main(root)
    root.mainloop()

