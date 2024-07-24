import uiautomation as auto
import subprocess
import pywinauto.mouse as mouse

# auto.ShowDesktop()
# subprocess.Popen('D:\\StudyFolder\\WorkDocument\\Hi-Lo\\ALL-300G\\ALL-300G.exe', shell=True)
window = auto.WindowControl(searchDepth=1, Name="ALL-300G")
# window.SetActive()
# window.MenuItemControl(searchDepth=2, Name='File').Click()
# # 移动鼠标到指定坐标（x=100, y=100）
# mouse.move(coords=(500, 500))
# window.MenuItemControl(searchDepth=3, Name="Open Job File").Click()
# window.EditControl(searchDepth=4, Name='文件名(N):').SendKeys("D:\\WorkDocument\\CopyRoomSW\\temp\\a.txt")
print(window.Exists(20, 0))