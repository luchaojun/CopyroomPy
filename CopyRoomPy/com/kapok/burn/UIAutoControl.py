import uiautomation as auto
import subprocess
import pywinauto.mouse as mouse
import time


class UIAutoControl:
    """
    自动操控All-300G.exe UI界面控制
    """
    def __init__(self, test_log):
        self.test_log = test_log


    """
    自动操控All-300G.exe UI界面控制
    """
    def controlAll300G(self, file_name=""):
        try:
            auto.ShowDesktop()
            # subprocess.Popen('D:\\StudyFolder\\WorkDocument\\Hi-Lo\\ALL-300G\\ALL-300G.exe', shell=True)
            window = auto.WindowControl(searchDepth=1, Name="ALL-300G")
            # if not window.Exists(5):
            #     subprocess.Popen('D:\\WorkDocument\\CopyRoomSW\\Hi-Lo\\ALL-300G\\ALL-300G.exe', shell=True)
            if not window.Exists():
                subprocess.Popen('D:\\WorkDocument\\CopyRoomSW\Hi-Lo\\ALL-300G\\ALL-300G.exe', shell=True)
            window.SetActive()
            window.MenuItemControl(searchDepth=3, Name='File').Click()
            # 移动鼠标到指定坐标（x=100, y=100）
            mouse.move(coords=(500, 500))
            window.MenuItemControl(searchDepth=3, Name="Open Job File").Click()
            print("File_name=" + file_name)
            jobFile = auto.WindowControl(searchDepth=2, Name="Open Job File")
            jobFile.EditControl(searchDepth=3, Name='檔案名稱(N):').SendKeys(file_name)
            jobFile.ButtonControl(searchDepth=3, Name='開啟(O)').Click()
            time.sleep(10)
            auto_window = auto.WindowControl(searchDepth=2, Name="Auto")
            if auto_window.Exists():
                return 1
            else:
                return 0
        except Exception as e:
            self.test_log.record_test_log(str(e))


    """
    自动操控Burn.exe UI界面控制
    """
    def controlBurn(self,data_dict):
        try:
            window = auto.WindowControl(searchDepth=1, Name=u" 群沃自动烧录系统")
            if not window.Exists(20):
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
        except Exception as e:
            self.test_log.record_test_log(str(e))


    def controlInfoGet(self):
        time.sleep(2)
        window = auto.WindowControl(searchDepth=1, Name="信息获取")
        window.SetActive()
        pane = window.PaneControl(searchDepth=3, ClassName="TkChild")
        pane.SendKeys("{Shift}")