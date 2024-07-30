import datetime
import os


class TestLogRecord:
    def __init__(self):
        # 创建一个Log File
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        log_date = datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
        log_path = 'C:\\ICBURN\\' + current_date
        # 创建以当前日期命名的文件夹
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        # 将测试数据保存到当前日期的文件夹中
        file_name = "IC_Burn_Label_Test_Record_" + log_date + ".txt"
        self.file_path = os.path.join(log_path, file_name)


        #记录log的信息
    def record_test_log(self, test_data):
            # 获取当前日期并格式化为字符串
            with open(self.file_path, 'a', encoding="utf-8") as f:
                f.write(test_data+'\n')