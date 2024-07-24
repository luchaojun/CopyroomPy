import uiautomation as auto
import subprocess
import time
import pywinauto.mouse as mouse
import tkinter as tk
from tkinter import font
import comtypes.stream

root = tk.Tk()
file_name = ''


def on_enter(event):
    entry = event.widget
    copyInfo = entry.get()
    data_list = copyInfo.split(";")
    data_dict = {}
    for item in data_list:
        print(item)
        key, value = item.split(":")
        data_dict[key.strip()] = value.strip()
    file_name = data_dict["M/O"] + "---" + data_dict["Nameplate"] + "---" + data_dict["Checksum"] + ".job";
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


def uiAutomationTest(file_name=""):
    auto.ShowDesktop()
    subprocess.Popen('D:\\WorkDocument\\CopyRoomSW\\Hi-Lo\\ALL-300G\\ALL-300G.exe', shell=True)
    time.sleep(3)
    window = auto.WindowControl(searchDepth=1, Name="ALL-300G")
    # # screenWidth, screenHeight = auto.GetScreenSize()
    # # window.MoveWindow(screenWidth // 4, screenHeight // 4, screenWidth // 2, screenHeight // 2)
    window.SetActive()
    window.MenuItemControl(Name='File').Click()
    # # 移动鼠标到指定坐标（x=100, y=100）
    mouse.move(coords=(0, 200))
    window.MenuItemControl(Name="Open Job File").Click()
    window.EditControl(Name='檔案名稱(N):').SendKeys("D:\\WorkDocument\\CopyRoomSW\\temp\\"+file_name)
    window.ButtonControl(Name='開啟(O)').Click()
    time.sleep(10)
    openBurn();


def openBurn():
    subprocess.Popen('D:\\WorkDocument\\CopyRoomSW\\Burn_V1.0.1.12 -hl\\Burn\\bin\\Debug\\Burn.exe', shell=True)


if __name__ == "__main__":
    showGetInformationDialog(400, 150)
    # uiAutomationTest()
