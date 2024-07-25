import uiautomation as auto
import subprocess
import pywinauto.mouse as mouse
import os
import psutil
import time


"""
关闭已打开的
"""
auto_window = auto.WindowControl(searchDepth=2, Name='Auto')
print(auto_window.Exists())
auto_window.GetWindowPattern().Close()

time.sleep(1)

job_window = auto.WindowControl(searchDepth=1, RegexName='.*.job')
print(job_window.Exists())
job_window.GetWindowPattern().Close()



