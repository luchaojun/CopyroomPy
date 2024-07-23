import uiautomation as auto
import subprocess
import time
import pywinauto.mouse as mouse
import tkinter as tk
from tkinter import font

root = tk.Tk()
file_name = ''


def on_enter(event):
    entry = event.widget
    file_name = entry.get()
    root.destroy()
    uiAutomationTest(file_name)


def showGetInformationDialog(width, height):
    root.title("信息获取")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    custom_font = font.Font(family="Helvetica", size=20, weight="bold")
    label_scan_content = tk.Label(root, text="请扫码输入工单内容:", font=custom_font)
    label_scan_content.grid(row=0, column=0, padx=10, pady=10)
    entry_scan_content = tk.Entry(root, width=50)
    entry_scan_content.focus();
    entry_scan_content.grid(row=1, column=0, padx=10, pady=10)
    entry_scan_content.bind('<Return>', on_enter)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()


def uiAutomationTest(file_name):
    auto.ShowDesktop()
    subprocess.Popen('notepad++.exe', shell=True)
    window = auto.WindowControl(searchDepth=1, Name="新文件 1 - Notepad++")
    screenWidth, screenHeight = auto.GetScreenSize()
    window.MoveWindow(screenWidth // 4, screenHeight // 4, screenWidth // 2, screenHeight // 2)
    window.SetActive()
    window.MenuItemControl(Name='文件(F)').Click()

    # 移动鼠标到指定坐标（x=100, y=100）
    mouse.move(coords=(100, 100))

    time.sleep(2)
    window.MenuItemControl(Name="打开(O)...	Ctrl+O").Click()
    window.EditControl(Name='文件名(N):').SendKeys("C:\\Users\\NINGMEI\\Desktop\\"+file_name)
    window.ButtonControl(Name='打开(O)').Click()


if __name__ == "__main__":
    # showGetInformationDialog(400, 150)
    uiAutomationTest('test123.txt')