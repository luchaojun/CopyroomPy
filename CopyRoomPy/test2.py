import uiautomation as auto
import subprocess
import time

auto.ShowDesktop()
subprocess.Popen('C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe', shell=True)
window = auto.WindowControl(searchDepth=1, Name="VMware Workstation")
screenWidth, screenHeight = auto.GetScreenSize()
window.MoveWindow(screenWidth // 4, screenHeight // 4, screenWidth // 2, screenHeight // 2)
window.SetActive()
window.MenuItemControl(Name='Help').Click()
time.sleep(1)
window.MenuItemControl(Name='Hints').Click()
