import comtypes.stream
from com.kapok.burn.TestDialog import TestDialog
from com.kapok.burn.TestLogRecord import TestLogRecord
from com.kapok.burn.UIAutoControl import UIAutoControl

if __name__ == "__main__":
    test_log = TestLogRecord()
    ui_auto = UIAutoControl(test_log)
    test_dialog = TestDialog(ui_auto, test_log)
    test_dialog.showGetInformationDialog(400, 150)
    file_name = test_dialog.get_file_name()
    if file_name is None:
        test_dialog.showWarningDialog()
    else:
        test_result = ui_auto.controlAll300G(file_name)
        print("test_result=" + str(test_result))
        if test_result:
            data_dict = test_dialog.get_data_dict()
            ui_auto.controlBurn(data_dict)
