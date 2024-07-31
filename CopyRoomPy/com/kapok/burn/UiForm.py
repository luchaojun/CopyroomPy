# Form implementation generated from reading ui file 'ui/ic_burn_auto.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import os
import sys
import threading
import tkinter as tk
from tkinter import messagebox

from com.kapok.burn.TestLogRecord import TestLogRecord
from com.kapok.burn.UIAutoControl import UIAutoControl


class UiForm(object):
    def __init__(self, ui_auto, test_log):
        self.data_dict = {}
        self.file_name = None
        self.ui_auto = ui_auto
        self.test_log = test_log
        self.form = None

    """
    获取UI界面对象
    """
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(519, 580)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(130, 10, 241, 41))
        self.label.setObjectName("label")
        self.lineEdit_mo = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_mo.setGeometry(QtCore.QRect(30, 60, 61, 31))
        self.lineEdit_mo.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_mo.setObjectName("lineEdit_mo")
        self.lineEdit_mo_value = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_mo_value.setGeometry(QtCore.QRect(90, 60, 151, 31))
        self.lineEdit_mo_value.returnPressed.connect(self.on_return_pressed)
        self.lineEdit_mo_value.setObjectName("lineEdit_mo_value")
        self.lineEdit_model = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_model.setGeometry(QtCore.QRect(30, 100, 61, 31))
        self.lineEdit_model.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_model.setObjectName("lineEdit_model")
        self.lineEdit_model_value = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_model_value.setGeometry(QtCore.QRect(90, 100, 151, 31))
        self.lineEdit_model_value.setObjectName("lineEdit_model_value")
        self.lineEdit_model_value.setDisabled(True)
        self.lineEdit_moqty = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_moqty.setGeometry(QtCore.QRect(30, 140, 61, 31))
        self.lineEdit_moqty.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_moqty.setObjectName("lineEdit_moqty")
        self.lineEdit_moqty_value = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_moqty_value.setGeometry(QtCore.QRect(90, 140, 151, 31))
        self.lineEdit_moqty_value.setObjectName("lineEdit_moqty_value")
        self.lineEdit_moqty_value.setDisabled(True)
        self.lineEdit_line = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_line.setGeometry(QtCore.QRect(30, 180, 61, 31))
        self.lineEdit_line.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_line.setObjectName("lineEdit_line")
        self.lineEdit_line_value = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_line_value.setGeometry(QtCore.QRect(90, 180, 151, 31))
        self.lineEdit_line_value.setObjectName("lineEdit_line_value")
        self.lineEdit_line_value.setDisabled(True)
        self.lineEdit_type = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_type.setGeometry(QtCore.QRect(30, 220, 61, 31))
        self.lineEdit_type.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_type.setObjectName("lineEdit_type")
        self.lineEdit_type_value = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_type_value.setGeometry(QtCore.QRect(90, 220, 151, 31))
        self.lineEdit_type_value.setObjectName("lineEdit_type_value")
        self.lineEdit_type_value.setDisabled(True)
        self.lineEdit_operator = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_operator.setGeometry(QtCore.QRect(30, 260, 61, 31))
        self.lineEdit_operator.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_operator.setObjectName("lineEdit_operator")
        self.lineEdit_operator_value = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_operator_value.setGeometry(QtCore.QRect(90, 260, 151, 31))
        self.lineEdit_operator_value.setObjectName("lineEdit_operator_value")
        self.lineEdit_operator_value.setDisabled(True)
        self.lineEdit_checksum = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_checksum.setGeometry(QtCore.QRect(260, 60, 71, 31))
        self.lineEdit_checksum.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_checksum.setObjectName("lineEdit_checksum")
        self.lineEdit_checksum_value = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_checksum_value.setGeometry(QtCore.QRect(330, 60, 151, 31))
        self.lineEdit_checksum_value.setObjectName("lineEdit_checksum_value")
        self.lineEdit_checksum_value.setDisabled(True)
        self.lineEdit_position = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_position.setGeometry(QtCore.QRect(260, 100, 71, 31))
        self.lineEdit_position.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_position.setObjectName("lineEdit_position")
        self.lineEdit_position_value = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_position_value.setGeometry(QtCore.QRect(330, 100, 151, 31))
        self.lineEdit_position_value.setObjectName("lineEdit_position_value")
        self.lineEdit_position_value.setDisabled(True)
        self.lineEdit_nameplate = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_nameplate.setGeometry(QtCore.QRect(260, 140, 71, 31))
        self.lineEdit_nameplate.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_nameplate.setObjectName("lineEdit_nameplate")
        self.lineEdit_nameplate_value = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_nameplate_value.setGeometry(QtCore.QRect(330, 140, 151, 31))
        self.lineEdit_nameplate_value.setObjectName("lineEdit_nameplate_value")
        self.lineEdit_nameplate_value.setDisabled(True)
        self.lineEdit_version = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_version.setGeometry(QtCore.QRect(260, 180, 71, 31))
        self.lineEdit_version.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_version.setObjectName("lineEdit_version")
        self.lineEdit_version_value = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_version_value.setGeometry(QtCore.QRect(330, 180, 151, 31))
        self.lineEdit_version_value.setObjectName("lineEdit_version_value")
        self.lineEdit_version_value.setDisabled(True)
        self.lineEdit_date = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_date.setGeometry(QtCore.QRect(260, 220, 71, 31))
        self.lineEdit_date.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.lineEdit_date_value = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_date_value.setGeometry(QtCore.QRect(330, 220, 151, 31))
        self.lineEdit_date_value.setObjectName("lineEdit_date_value")
        self.lineEdit_date_value.setDisabled(True)
        self.lineEdit_reelqty = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_reelqty.setGeometry(QtCore.QRect(260, 260, 71, 31))
        self.lineEdit_reelqty.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_reelqty.setObjectName("lineEdit_reelqty")
        self.lineEdit_reelqty_value = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_reelqty_value.setGeometry(QtCore.QRect(330, 260, 151, 31))
        self.lineEdit_reelqty_value.setObjectName("lineEdit_reelqty_value")
        self.lineEdit_reelqty_value.setDisabled(True)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(0, 360, 191, 41))
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(parent=Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 420, 421, 121))
        self.textEdit.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setDisabled(True)
        self.pushButton_start = QtWidgets.QPushButton(parent=Form)
        self.pushButton_start.setGeometry(QtCore.QRect(70, 310, 101, 41))
        self.pushButton_start.setObjectName("pushButton")
        self.pushButton_start.clicked.connect(self.start_test)
        self.pushButton_restart = QtWidgets.QPushButton(parent=Form)
        self.pushButton_restart.setGeometry(QtCore.QRect(320, 310, 101, 41))
        self.pushButton_restart.setObjectName("pushButton_2")
        self.pushButton_restart.clicked.connect(self.restart_test)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    """
    给UI界面设置值
    """
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "IC Burn Auto"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700;\">IC Burn Auto</span></p></body></html>"))
        self.lineEdit_mo.setToolTip(_translate("Form",
                                               "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_mo.setText(_translate("Form", "     M/O"))
        self.lineEdit_mo.setDisabled(True)
        self.lineEdit_model.setToolTip(_translate("Form",
                                                  "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_model.setText(_translate("Form", "   Model"))
        self.lineEdit_model.setDisabled(True)
        self.lineEdit_moqty.setToolTip(_translate("Form",
                                                  "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_moqty.setText(_translate("Form", " MO QTY"))
        self.lineEdit_moqty.setDisabled(True)
        self.lineEdit_line.setToolTip(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_line.setText(_translate("Form", "     Line"))
        self.lineEdit_line.setDisabled(True)
        self.lineEdit_type.setToolTip(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_type.setText(_translate("Form", "    Type"))
        self.lineEdit_type.setDisabled(True)
        self.lineEdit_operator.setToolTip(_translate("Form",
                                                     "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_operator.setText(_translate("Form", " Operator"))
        self.lineEdit_operator.setDisabled(True)
        self.lineEdit_checksum.setToolTip(_translate("Form",
                                                     "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_checksum.setText(_translate("Form", " CheckSum"))
        self.lineEdit_checksum.setDisabled(True)
        self.lineEdit_position.setToolTip(_translate("Form",
                                                     "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_position.setText(_translate("Form", "  Position"))
        self.lineEdit_position.setDisabled(True)
        self.lineEdit_nameplate.setToolTip(_translate("Form",
                                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_nameplate.setText(_translate("Form", "Nameplate"))
        self.lineEdit_nameplate.setDisabled(True)
        self.lineEdit_version.setToolTip(_translate("Form",
                                                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_version.setText(_translate("Form", "    Version"))
        self.lineEdit_version.setDisabled(True)
        self.lineEdit_date.setToolTip(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_date.setText(_translate("Form", "      Date"))
        self.lineEdit_date.setDisabled(True)
        self.lineEdit_reelqty.setToolTip(_translate("Form",
                                                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_reelqty.setText(_translate("Form", "   Reel Qty"))
        self.lineEdit_reelqty.setDisabled(True)
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:20pt;\">錯誤信息:</span></p></body></html>"))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "hr { height: 1px; border-width: 0; }\n"
                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                         "</style></head><body style=\" font-family:\'Microsoft JhengHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">None</span></p></body></html>"))
        self.pushButton_start.setText(_translate("Form", "開始測試"))
        self.pushButton_start.setDisabled(True)
        self.pushButton_restart.setText(_translate("Form", "重新測試"))
        self.pushButton_restart.setDisabled(True)

    """
    给line edit控件设置读取到的值
    """
    def setValue(self):
        self.lineEdit_mo_value.setText(self.data_dict['M/O'])
        self.lineEdit_mo_value.setDisabled(True)
        self.lineEdit_model_value.setText(self.data_dict['Model'])
        self.lineEdit_moqty_value.setText(self.data_dict['MO Qty'])
        self.lineEdit_line_value.setText(self.data_dict['Line'])
        self.lineEdit_type_value.setText(self.data_dict['Type'])
        self.lineEdit_operator_value.setText(self.data_dict['Operator'])
        self.lineEdit_checksum_value.setText(self.data_dict['Checksum'])
        self.lineEdit_position_value.setText(self.data_dict['Position'])
        self.lineEdit_nameplate_value.setText(self.data_dict['Nameplate'])
        self.lineEdit_version_value.setText(self.data_dict['Version'])
        self.lineEdit_date_value.setText(self.data_dict['Date'])
        self.lineEdit_reelqty_value.setText(self.data_dict['Reel Qty'])

    """
    按Enter按钮驱动事件
    """
    def on_return_pressed(self):
        print("on_return_pressed")
        ic_burn_info_all = self.lineEdit_mo_value.text()
        ic_burn_info = ic_burn_info_all[:-1]
        print('copyInfo=' + ic_burn_info)
        data_list = ic_burn_info.split(";")
        for item in data_list:
            if not item == "":
                print(item)
                key, value = item.split(":")
                self.data_dict[key.strip()] = value.strip()
        self.setValue()
        model_name = self.data_dict["Model"][:6]
        print("model_name=" + model_name)
        file_count, self.file_name, file_name_list = self.find_file("D:\\WorkDocument\\CopyRoomSW\\temp", model_name,
                                        "---" + self.data_dict["Nameplate"] + "---" + self.data_dict[
                                            "Checksum"] + ".job")
        if self.file_name is None:
            self.setErrorMessage("沒有找到對應的job文件, 請檢查後重新開始測試!!!!!!!!!")
            self.test_log.record_test_log("error message - 沒有找到對應的job文件, 請檢查後重新開始測試!!!!!!!!!, 目前查詢的job檔案的名字(注意開頭六位是模糊查詢)-"+model_name+
                                        "---" + self.data_dict["Nameplate"] + "---" + self.data_dict[
                                            "Checksum"] + ".job")
        if file_count > 1:
            self.setErrorMessage("发现多个對應的job文件, 請检查job文件命名!!!")
            self.test_log.record_test_log("发现多个對應的job文件---"+str(file_name_list))
        else:
            self.pushButton_start.setDisabled(False)

    """
    开始测试
    """
    def start_test(self):
        self.pushButton_start.setDisabled(True)
        self.form.close()
        self.ui_auto.controlAll300G(self.file_name, self.data_dict)

    """
    重新测试
    """
    def restart_test(self):
        self.pushButton_start.setDisabled(False)
        self.form.close()
        self.form = QtWidgets.QWidget()
        self.setupUi(self.form)
        my_thread = threading.Thread(target=self.ui_auto.controlInfoGet)
        my_thread.start()
        self.form.show()

    """
    寻找合适的job file
    """
    def find_file(self, directory, prefix, suffix):
        file_count = 0
        file_name_list = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.startswith(prefix) and file.endswith(suffix) and (not file.endswith("C"+suffix)):
                    file_count = file_count + 1
                    file_name = os.path.join(root, file)
                    file_name_list.append(file_name)
        return file_count, file_name, file_name_list

    """
    显示绘制的页面
    """
    def showUI(self):
        app = QtWidgets.QApplication(sys.argv)
        self.form = QtWidgets.QWidget()
        self.setupUi(self.form)

        my_thread = threading.Thread(target=self.ui_auto.controlInfoGet)
        my_thread.start()

        self.form.show()
        sys.exit(app.exec())

    """
    设置Error框的error信息
    """
    def setErrorMessage(self, msg):
        _translate = QtCore.QCoreApplication.translate
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "hr { height: 1px; border-width: 0; }\n"
                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                         "</style></head><body style=\" font-family:\'Microsoft JhengHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">" + msg + "</span></p></body></html>"))
        self.pushButton_restart.setDisabled(False)


if __name__ == "__main__":
    test_log = TestLogRecord()
    ui_auto = UIAutoControl(test_log)
    ui_form = UiForm(ui_auto, test_log)
    ui_form.showUI()
