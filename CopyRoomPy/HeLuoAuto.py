import uiautomation as auto
import subprocess
import time
import pywinauto.mouse as mouse
import tkinter as tk
from tkinter import font
import comtypes.stream
import os
import threading

root = tk.Tk()
file_name = ''
data_dict = {}


"""
扫码后点击回车驱动事件, 对扫码枪带出来的数据进行解析
"""
def on_enter(event):
    entry = event.widget
    copyInfo_total = entry.get()
    copyInfo = copyInfo_total[:-1]
    print('copyInfo=' + copyInfo)
    data_list = copyInfo.split(";")
    for item in data_list:
        if not item == "":
            print(item)
            key, value = item.split(":")
            data_dict[key.strip()] = value.strip()
    print(data_dict["Model"])
    model_name_total = data_dict["Model"].split("/")[0]
    model_name = model_name_total[:6]
    file_name = find_file("D:\\WorkDocument\\CopyRoomSW\\temp\\", model_name,
                          "---" + data_dict["Nameplate"] + "---" + data_dict["Checksum"] + ".job")
    root.destroy()
    uiAutomationAll300G(file_name)


'''
寻找合适的job file
'''
def find_file(directory, prefix, suffix):
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(file)
            if file.startswith(prefix) and file.endswith(suffix):
                return os.path.join(root, file)
    return None


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
    #开启线程切换输入法
    my_thread = threading.Thread(target=my_function)
    my_thread.start()
    auto.ShowDesktop()
    root.mainloop()

'''
线程方法
'''
def my_function():
    time.sleep(2)
    window = auto.WindowControl(searchDepth=1, Name="信息获取")
    window.SetActive()
    pane = window.PaneControl(searchDepth=3, ClassName="TkChild")
    pane.SendKeys("{Shift}")


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
        subprocess.Popen('D:\\WorkDocument\\CopyRoomSW\\Hi-Lo\\ALL-300G\\ALL-300G.exe', shell=True)
    window.SetActive()
    window.MenuItemControl(searchDepth=3, Name='文件').Click()
    # 移动鼠标到指定坐标（x=100, y=100）
    mouse.move(coords=(500, 500))
    window.MenuItemControl(searchDepth=3, Name="打开工程文件").Click()
    print("File_name=" + file_name)
    jobFile = auto.WindowControl(searchDepth=2, Name="打开工程文件")
    jobFile.EditControl(searchDepth=3, Name='文件名(N):').SendKeys(file_name)
    jobFile.ButtonControl(searchDepth=3, Name='打开(O)').Click()
    auto_window = auto.WindowControl(searchDepth=2, Name="自动")
    if auto_window.Exists(20):
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
    window.SetActive()
    homeBtn = window.ButtonControl(searchDepth=6, AutomationId="but_Homing")
    if homeBtn.Exists(20):
        homeBtn.Click()
        time.sleep(18)
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
        operater_ed.SendKeys("N")
        time.sleep(2)
        inspectors_ed = window.EditControl(searchDepth=7, AutomationId="txt_Inspectors")
        inspectors_ed.SetFocus()
        inspectors_ed.SendKeys("N")
        time.sleep(2)


if __name__ == "__main__":
    showGetInformationDialog(400, 150)
    # uiAutomationAll300G("a.txt")
    # uiAutomationBurn()
