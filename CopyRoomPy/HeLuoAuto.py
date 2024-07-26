import uiautomation as auto
import subprocess
import time
import pywinauto.mouse as mouse
import tkinter as tk
from tkinter import font
import comtypes.stream
import os

root = tk.Tk()
file_name = ''
data_dict = {}

"""
扫码后点击回车驱动事件, 对扫码枪带出来的数据进行解析
"""
def on_enter(event):
    entry = event.widget
    copyInfo = entry.get()
    data_list = copyInfo.split(";")
    for item in data_list:
        if not item == "":
            print(item)
            key, value = item.split(":")
            data_dict[key.strip()] = value.strip()
    model_name = data_dict["Model"].split("/")[0]
    file_name = model_name + "---" + data_dict["Nameplate"] + "---" + data_dict["Checksum"] + ".job";
    root.destroy()
    uiAutomationAll300G(file_name)


"""
绘制接收扫码信息的界面
"""
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


"""
automation自动操控All-300G.exe UI界面控制
"""
def uiAutomationAll300G(file_name=""):
    auto.ShowDesktop()
    # subprocess.Popen('D:\\StudyFolder\\WorkDocument\\Hi-Lo\\ALL-300G\\ALL-300G.exe', shell=True)
    window = auto.WindowControl(searchDepth=1, Name="ALL-300G")
    # if not window.Exists(5):
    #     subprocess.Popen('D:\\WorkDocument\\CopyRoomSW\\Hi-Lo\\ALL-300G\\ALL-300G.exe', shell=True)
    if not window.Exists():
        subprocess.Popen('C:\\Program Files (x86)\\Hi-Lo\\ALL-300G\\ALL-300G.exe', shell=True)
    window.SetActive()
    window.MenuItemControl(searchDepth=2, Name='文件').Click()
    # 移动鼠标到指定坐标（x=100, y=100）
    mouse.move(coords=(500, 500))
    window.MenuItemControl(searchDepth=3, Name="打开工程文件").Click()
    window.EditControl(searchDepth=4, Name='文件名(N):').SendKeys(u"C:\\Users\\Group-test\\Desktop\\烧录软体\\" + file_name)
    window.ButtonControl(searchDepth=4, Name='打开(O)').Click()
    time.sleep(20)
    auto_window = auto.WindowControl(searchDepth=2, Name="Auto")
    if auto_window.Exists():
        time.sleep(2)
        print("开启Burn exe")
        uiAutomationBurn();


"""
automation自动操控Burn.exe UI界面控制
"""
def uiAutomationBurn():
    # subprocess.Popen('D:\\WorkDocument\\CopyRoomSW\\Burn_V1.0.1.12 -hl\\Burn\\bin\\Debug\\Burn.exe', shell=True)
    time.sleep(8)
    window = auto.WindowControl(searchDepth=1, Name=u" 群沃自动烧录系统")
    if not window.Exists():
        subprocess.Popen('D:\\WorkDocument\\CopyRoomSW\\Burn_V1.0.1.12 -hl\\Burn\\bin\\Debug\\Burn.exe', shell=True)
    window.ButtonControl(searchDepth=6, AutomationId="but_Homing").Click()
    time.sleep(15)
    window.ButtonControl(searchDepth=6, AutomationId="but_WorkOrder").Click()
    time.sleep(3)
    work_order_name_ed = window.EditControl(searchDepth=7, AutomationId="txt_WorkOrderName")
    work_order_name_ed.SetFocus()
    work_order_name_ed.SendKeys(data_dict["M/O"])
    time.sleep(2)
    work_order_num_ed = window.EditControl(searchDepth=7, AutomationId="txt_WorkOrderNum")
    work_order_num_ed.SetFocus()
    work_order_num_ed.SendKeys(data_dict["MO Qty"])
    time.sleep(2)
    operater_ed = window.EditControl(searchDepth=7, AutomationId="txt_Operator")
    operater_ed.SetFocus()
    operater_ed.SendKeys("待定")
    time.sleep(2)
    inspectors_ed = window.EditControl(searchDepth=7, AutomationId="txt_Inspectors")
    inspectors_ed.SetFocus()
    inspectors_ed.SendKeys("待定")
    time.sleep(2)


if __name__ == "__main__":
    showGetInformationDialog(400, 150)
    # uiAutomationAll300G("a.txt")
    # uiAutomationBurn()