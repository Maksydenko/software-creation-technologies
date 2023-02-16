from PyQt5 import QtCore, QtWidgets


class Ui_Practice(object):
    def setupUi(self, Practice):
        Practice.setObjectName("Practice")
        Practice.resize(400, 300)
        Practice.setMouseTracking(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Practice)
        self.buttonBox.setGeometry(QtCore.QRect(30, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Practice)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 20))
        self.label.setObjectName("label")
        self.checkBox_2 = QtWidgets.QCheckBox(Practice)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 150, 131, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.radioButton = QtWidgets.QRadioButton(Practice)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(30, 60, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.lineEdit = QtWidgets.QLineEdit(Practice)
        self.lineEdit.setGeometry(QtCore.QRect(30, 180, 251, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton_2 = QtWidgets.QRadioButton(Practice)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 90, 111, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.checkBox = QtWidgets.QCheckBox(Practice)
        self.checkBox.setGeometry(QtCore.QRect(30, 120, 81, 20))
        self.checkBox.setAcceptDrops(False)
        self.checkBox.setObjectName("checkBox")
        self.progressBar = QtWidgets.QProgressBar(Practice)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(30, 220, 341, 23))
        self.progressBar.setProperty("value", 99)
        self.progressBar.setObjectName("progressBar")
        self.toolButton = QtWidgets.QToolButton(Practice)
        self.toolButton.setGeometry(QtCore.QRect(300, 180, 61, 21))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Practice)
        self.buttonBox.accepted.connect(Practice.accept)  # type: ignore
        self.buttonBox.rejected.connect(Practice.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Practice)

    def retranslateUi(self, Practice):
        _translate = QtCore.QCoreApplication.translate
        Practice.setWindowTitle(_translate("Practice", "Practice"))
        self.label.setText(_translate("Practice", "Label"))
        self.checkBox_2.setText(_translate("Practice", "Disabled checkbox"))
        self.radioButton.setText(_translate("Practice", "Radio"))
        self.lineEdit.setText(_translate("Practice", "C:\\Users\\"))
        self.radioButton_2.setText(_translate("Practice", "Disabled radio"))
        self.checkBox.setText(_translate("Practice", "Checkbox"))
        self.toolButton.setText(_translate("Practice", "Browse..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Practice = QtWidgets.QDialog()
    ui = Ui_Practice()
    ui.setupUi(Practice)
    Practice.show()
    sys.exit(app.exec_())
