import tkinter as tk
from PIL import Image, ImageTk

print("APP IS ONLINE")

root = tk.Tk()
root.title("Crypt")
root.geometry("750x500")

logo = tk.PhotoImage(file= r"F:\CryptoCoin App\Logo.png")
logo = logo.subsample(5)
label = tk.Label(root, image=logo)
label.place(x=0, y=0, anchor="nw")





root.mainloop()