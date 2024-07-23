import uiautomation as auto
import subprocess
import time

auto.ShowDesktop()
subprocess.Popen('D:\\SoftWare\\VMWare\\vmware.exe', shell=True)
window = auto.WindowControl(searchDepth=1, Name="VMware Workstation")
screenWidth, screenHeight = auto.GetScreenSize()
window.MoveWindow(screenWidth // 4, screenHeight // 4, screenWidth // 2, screenHeight // 2)
window.SetActive()
window.MenuItemControl(Name='帮助(H)').Click()
time.sleep(1)
menu = auto.MenuControl(searchDepth=1, Name='上下文')
menu.MenuItemControl(Name='支持(S)').Click()
