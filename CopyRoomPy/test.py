import pywinauto
import time

app = pywinauto.Application().start("C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe");
time.sleep(5)
title = 'VMware WOrkstation'
dlg = app[title]
dlg.menu_select('File->Close Tab')
saveWin = dlg.child_window(title=u"另存新檔", control_type="Window")
saveWin.child_window(title=u"存檔(S)", control_type="Button").click()





# # 启动记事本
# app = pywinauto.Application(backend='uia').start('notepad.exe')
#
# # 使用窗口标题获取记事本窗口
# dlg = app['未命名 - 記事本']
# print(dlg.print_ctrl_ids())

# # 输入文本
# dlg.type_keys('这里是你的文本内容123...')
#
# # 保存文件
# dlg.menu_select('檔案(F)->存儲檔案(S)')
# time.sleep(2)
#
# save_win = dlg.child_window(title="另存新檔", control_type="Window")
#
# # 输入文件名
# save_win.child_window(title="檔案名稱:", control_type="Edit").set_text("a.txt")
#
# # 确认保存
# save_win.child_window(title="存檔(S)", control_type="Button").click()
# time.sleep(2)
#
# save_finish = save_win.child_window(title="確認另存新檔", control_type="Window")
# save_win.child_window(title="是(Y)", control_type="Button").click()
