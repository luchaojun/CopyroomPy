import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.withdraw()  # 隐藏主窗口
messagebox.showwarning("警告", "这是一个警告框！")
print("1234567890")
root.destroy()
root.mainloop()
