import threading
import uiautomation as auto
from tkinter import font
import tkinter as tk
from tkinter import messagebox
import os


class TestDialog:

    def __init__(self, ui_auto, test_log):
        self.root = tk.Tk()
        self.data_dict = {}
        self.ui_auto = ui_auto
        self.test_log = test_log
        self.file_name = None

    """
        绘制接收扫码信息的界面
    """

    def showGetInformationDialog(self, width, height):
        self.root.title("信息获取")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        custom_font = font.Font(family="Helvetica", size=20, weight="bold")
        label_scan_content = tk.Label(self.root, text="请扫码输入工单内容:", font=custom_font)
        label_scan_content.grid(row=0, column=0, padx=10, pady=10)
        entry_scan_content = tk.Entry(self.root, width=50)
        entry_scan_content.focus();
        entry_scan_content.grid(row=1, column=0, padx=10, pady=10)
        entry_scan_content.bind('<Return>', self.on_enter)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        # 开启线程切换输入法
        my_thread = threading.Thread(target=self.ui_auto.controlInfoGet)
        my_thread.start()
        auto.ShowDesktop()
        self.root.mainloop()

    """
    扫码后点击回车驱动事件, 对扫码枪带出来的数据进行解析
    """

    def on_enter(self, event):
        entry = event.widget
        copyInfo_total = entry.get()
        copyInfo = copyInfo_total[:-1]
        print('copyInfo=' + copyInfo)
        data_list = copyInfo.split(";")
        for item in data_list:
            if not item == "":
                print(item)
                key, value = item.split(":")
                self.data_dict[key.strip()] = value.strip()
        self.test_log.record_test_log("IC Burn Label = "+str(self.data_dict))
        model_name = self.data_dict["Model"][:6]
        print("model_name=" + model_name)
        file_name = self.find_file("D:\\WorkDocument\\CopyRoomSW\\temp", model_name,
                                   "---" + self.data_dict["Nameplate"] + "---" + self.data_dict["Checksum"] + ".job")
        # print("file_name="+file_name)
        self.root.destroy()
        self.file_name = file_name

    def get_file_name(self):
        return self.file_name

    def get_data_dict(self):
        return self.data_dict

    '''
    寻找合适的job file
    '''
    def find_file(self, directory, prefix, suffix):
        print("find_file")
        for root, dirs, files in os.walk(directory):
            for file in files:
                print(file)
                if file.startswith(prefix) and file.endswith(suffix):
                    return os.path.join(root, file)
        return None

    def showWarningDialog(self):
        rootDialog = tk.Tk()
        rootDialog.withdraw()  # 隐藏主窗口
        messagebox.showwarning("警告", "未找到对应的job档案, 请确认后进行重新测试!!!")
        self.test_log.record_test_log("error message - 未找到对应的job档案")
        rootDialog.destroy()
        rootDialog.mainloop()
