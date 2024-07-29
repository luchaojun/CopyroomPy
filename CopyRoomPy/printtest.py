import datetime
import os

current_date = datetime.datetime.now().strftime('%Y-%m-%d')
log_date = datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
# 创建以当前日期命名的文件夹
if not os.path.exists(current_date):
    os.makedirs(current_date)
# 将测试数据保存到当前日期的文件夹中
file_name = "IC_Burn_Label_Test_Record_" + log_date + ".txt"
file_path = os.path.join(current_date, file_name)

def record_test_log(test_data):
    # 获取当前日期并格式化为字符串
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(test_data)

record_test_log("test123")