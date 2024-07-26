"""
关闭已打开的All-300G.exe
auto_window = auto.WindowControl(searchDepth=2, Name='Auto')
print(auto_window.Exists())
auto_window.GetWindowPattern().Close()
time.sleep(1)
job_window = auto.WindowControl(searchDepth=1, RegexName='.*.job')
print(job_window.Exists())
job_window.GetWindowPattern().Close()
'''


'''
根据前缀和后缀去查找对应的文件
import os
def find_file(directory, prefix, suffix):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith(prefix) and file.endswith(suffix):
                print(file)
                print(os.path.join(root, file))
    return None
directory = "D:/WorkDocument/CopyRoomSW/temp"
prefix = "L1XXAU"
suffix = "25B256EY---F99B.job"
result = find_file(directory, prefix, suffix)

if result:
    print(f"找到符合条件的文件： {result}")
else:
    print("没有找到符合条件的文件")
"""