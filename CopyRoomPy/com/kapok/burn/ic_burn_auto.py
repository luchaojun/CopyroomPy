# Form implementation generated from reading ui file 'ui/ic_burn_auto.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(519, 580)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(130, 10, 241, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 61, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setDisabled(True)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 60, 151, 31))
        self.lineEdit_2.returnPressed.connect(self.on_return_pressed)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 100, 61, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 100, 151, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setDisabled(True)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 140, 61, 31))
        self.lineEdit_5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 180, 61, 31))
        self.lineEdit_6.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(30, 220, 61, 31))
        self.lineEdit_7.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(260, 60, 71, 31))
        self.lineEdit_8.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(260, 100, 71, 31))
        self.lineEdit_9.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(260, 140, 71, 31))
        self.lineEdit_10.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(260, 180, 71, 31))
        self.lineEdit_11.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(260, 220, 71, 31))
        self.lineEdit_12.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_13.setGeometry(QtCore.QRect(260, 260, 71, 31))
        self.lineEdit_13.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_14.setGeometry(QtCore.QRect(30, 260, 61, 31))
        self.lineEdit_14.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_15.setGeometry(QtCore.QRect(330, 60, 151, 31))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_15.setDisabled(True)
        self.lineEdit_16 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_16.setGeometry(QtCore.QRect(330, 100, 151, 31))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_16.setDisabled(True)
        self.lineEdit_17 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_17.setGeometry(QtCore.QRect(330, 140, 151, 31))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_17.setDisabled(True)
        self.lineEdit_18 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_18.setGeometry(QtCore.QRect(330, 180, 151, 31))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_18.setDisabled(True)
        self.lineEdit_19 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_19.setGeometry(QtCore.QRect(330, 220, 151, 31))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_19.setDisabled(True)
        self.lineEdit_20 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_20.setGeometry(QtCore.QRect(330, 260, 151, 31))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_20.setDisabled(True)
        self.lineEdit_21 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_21.setGeometry(QtCore.QRect(90, 140, 151, 31))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_21.setDisabled(True)
        self.lineEdit_22 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_22.setGeometry(QtCore.QRect(90, 180, 151, 31))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_22.setDisabled(True)
        self.lineEdit_23 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_23.setGeometry(QtCore.QRect(90, 220, 151, 31))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_23.setDisabled(True)
        self.lineEdit_24 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_24.setGeometry(QtCore.QRect(90, 260, 151, 31))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_24.setDisabled(True)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(0, 360, 191, 41))
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(parent=Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 420, 421, 121))
        self.textEdit.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 310, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 310, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "IC Burn Auto"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700;\">IC Burn Auto</span></p></body></html>"))
        self.lineEdit.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit.setText(_translate("Form", "     M/O"))
        self.lineEdit.setDisabled(True)
        self.lineEdit_3.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_3.setText(_translate("Form", "   Model"))
        self.lineEdit_3.setDisabled(True)
        self.lineEdit_5.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_5.setText(_translate("Form", " MO QTY"))
        self.lineEdit_5.setDisabled(True)
        self.lineEdit_6.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_6.setText(_translate("Form", "     Line"))
        self.lineEdit_6.setDisabled(True)
        self.lineEdit_7.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_7.setText(_translate("Form", "    Type"))
        self.lineEdit_7.setDisabled(True)
        self.lineEdit_8.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_8.setText(_translate("Form", " CheckSum"))
        self.lineEdit_8.setDisabled(True)
        self.lineEdit_9.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_9.setText(_translate("Form", "  Position"))
        self.lineEdit_9.setDisabled(True)
        self.lineEdit_10.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_10.setText(_translate("Form", "Nameplate"))
        self.lineEdit_10.setDisabled(True)
        self.lineEdit_11.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_11.setText(_translate("Form", "    Version"))
        self.lineEdit_11.setDisabled(True)
        self.lineEdit_12.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_12.setText(_translate("Form", "      Date"))
        self.lineEdit_12.setDisabled(True)
        self.lineEdit_13.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_13.setText(_translate("Form", "   Reel Qty"))
        self.lineEdit_13.setDisabled(True)
        self.lineEdit_14.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.lineEdit_14.setText(_translate("Form", " Operator"))
        self.lineEdit_14.setDisabled(True)
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt;\">Error Message:</span></p></body></html>"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft JhengHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">None</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "开始测试"))
        self.pushButton_2.setText(_translate("Form", "重新测试"))

    def on_return_pressed(self):
        data_dict = {}
        print("on_return_pressed")
        ic_burn_info_all = self.lineEdit_2.text()
        ic_burn_info = ic_burn_info_all[:-1]
        print('copyInfo=' + ic_burn_info)
        data_list = ic_burn_info.split(";")
        for item in data_list:
            if not item == "":
                print(item)
                key, value = item.split(":")
                data_dict[key.strip()] = value.strip()
        print(data_dict)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
