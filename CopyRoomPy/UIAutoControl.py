import uiautomation as auto
import subprocess
import pywinauto.mouse as mouse
import time
import tkinter as tk
from tkinter import messagebox


class UIAutoControl:
    """
    自动操控All-300G.exe UI界面控制
    """
    def __init__(self, test_log):
        self.test_log = test_log
        self.uiFormObj = None


    """
    自动操控All-300G.exe UI界面控制
    """
    def controlAll300G(self, file_name="", data_dict={}):
        try:
            auto.ShowDesktop()
            window = auto.WindowControl(searchDepth=1, Name="ALL-300G")
            if not window.Exists():
                # subprocess.Popen('D:\\WorkDocument\\CopyRoomSW\Hi-Lo\\ALL-300G\\ALL-300G.exe', shell=True) #office computer
                subprocess.Popen('C:\\Program Files (x86)\\Hi-Lo\\ALL-300G\\ALL-300G.exe', shell=True) #SMT computer
            window.SetActive()
            # window.MenuItemControl(searchDepth=3, Name='File').Click()  #office computer
            window.MenuItemControl(searchDepth=3, Name='文件').Click()  #SMT computer
            # 移动鼠标到指定坐标（x=100, y=100）
            mouse.move(coords=(500, 500))
            # window.MenuItemControl(searchDepth=3, Name="Open Job File").Click() #office computer
            window.MenuItemControl(searchDepth=3, Name="打开工程文件").Click() #SMT computer
            print("File_name=" + file_name)
            jobFile = auto.WindowControl(searchDepth=2, Name="Open Job File")
            # jobFile.EditControl(searchDepth=3, Name='檔案名稱(N):').SendKeys(file_name) #office computer
            jobFile.EditControl(searchDepth=3, Name='文件名(N):').SendKeys(file_name) #SMT computer
            # jobFile.ButtonControl(searchDepth=3, Name='開啟(O)').Click() #office computer
            jobFile.ButtonControl(searchDepth=3, Name='打开(O)').Click() #SMT computer
            # auto_window = auto.WindowControl(searchDepth=2, Name="Auto") #office computer
            time.sleep(4)
            auto_window = auto.WindowControl(searchDepth=2, Name="自动") #SMT computer
            if auto_window.Exists():
                self.controlBurn(data_dict)

        except Exception as e:
            self.test_log.record_test_log(str(e))


    """
    自动操控Burn.exe UI界面控制
    """
    def controlBurn(self,data_dict):
        try:
            window = auto.WindowControl(searchDepth=1, Name=u" 群沃自动烧录系统")
            if not window.Exists():
                # subprocess.Popen('D:\\WorkDocument\\CopyRoomSW\\Burn_V1.0.1.12 -hl\\Burn\\bin\\Debug\\Burn.exe', shell=True) #office computer
                subprocess.Popen('D:\\Burn_V1.0.1.12 -hl\\Burn\\bin\\Debug\\Burn.exe', shell=True) #SMT Computer
                time.sleep(10)
            window.SetActive()
            homeBtn = window.ButtonControl(searchDepth=6, AutomationId="but_Homing")
            if homeBtn.Exists():
                homeBtn.Click()
                # time.sleep(10)
                window.ButtonControl(searchDepth=6, AutomationId="but_WorkOrder").Click(waitTime=5)
                # time.sleep(3)
                work_order_name_ed = window.EditControl(searchDepth=7, AutomationId="txt_WorkOrderName")
                work_order_name_ed.SetFocus()
                work_order_name_ed.SendKeys(data_dict["M/O"])
                # time.sleep(2)
                work_order_num_ed = window.EditControl(searchDepth=7, AutomationId="txt_WorkOrderNum")
                work_order_num_ed.SetFocus()
                work_order_num_ed.SendKeys(data_dict["MO Qty"])
                # time.sleep(2)
                operater_ed = window.EditControl(searchDepth=7, AutomationId="txt_Operator")
                operater_ed.SetFocus()
                operater_ed.SendKeys(u"龙路")
                # time.sleep(2)
                inspectors_ed = window.EditControl(searchDepth=7, AutomationId="txt_Inspectors")
                inspectors_ed.SetFocus()
                inspectors_ed.SendKeys(u"张玉敏")
                # time.sleep(2)

                checksum_ed = window.EditControl(searchDepth=7, AutomationId="txt_CheckSum")
                checksum_burn = checksum_ed.GetLegacyIAccessiblePattern().Value;
                self.test_log.record_test_log("checksum_burn="+str(checksum_burn))


                check_sum = data_dict["Checksum"]
                self.test_log.record_test_log("checksum_label=" + str(check_sum))

                rootDialog = tk.Tk()
                rootDialog.withdraw()  # 隐藏主窗口
                if(checksum_burn.endswith(check_sum)):
                    messagebox.showinfo("提示", "Checksum值比對一致, IC Burn自動化已經結束, 請手動完成下面其他步驟")
                else:
                    messagebox.showerror("警告", "Checksum值比對不一致, 請檢查job檔案")
                rootDialog.destroy()
                rootDialog.mainloop()
        except Exception as e:
            self.test_log.record_test_log(str(e))


    """
    切换输入法由中文切换成英文
    """
    def controlInfoGet(self):
        time.sleep(1)
        window = auto.WindowControl(searchDepth=1, Name="IC Burn Auto")
        window.SetActive()
        pane = window.EditControl(searchDepth=3, AutomationId="Form.lineEdit_mo_value")
        pane.SendKeys("{Shift}")