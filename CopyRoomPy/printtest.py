import tkinter as tk
from tkinter import messagebox

rootDialog = tk.Tk()
rootDialog.withdraw()  # 隐藏主窗口
messagebox.showinfo("提示", "IC Burn自動化已經結束, 請手動完成下面其他步驟")
rootDialog.destroy()
rootDialog.mainloop()
print(456)