from PyQt5 import QtCore, QtWidgets


class Ui_Lab(object):
    def setupUi(self, Lab):
        Lab.setObjectName("Lab")
        Lab.resize(400, 300)
        Lab.setMouseTracking(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Lab)
        self.buttonBox.setGeometry(QtCore.QRect(30, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Lab)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 20))
        self.label.setObjectName("label")
        self.checkBox_2 = QtWidgets.QCheckBox(Lab)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 150, 131, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.radioButton = QtWidgets.QRadioButton(Lab)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(30, 60, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.lineEdit = QtWidgets.QLineEdit(Lab)
        self.lineEdit.setGeometry(QtCore.QRect(30, 180, 251, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton_2 = QtWidgets.QRadioButton(Lab)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 90, 111, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.checkBox = QtWidgets.QCheckBox(Lab)
        self.checkBox.setGeometry(QtCore.QRect(30, 120, 81, 20))
        self.checkBox.setAcceptDrops(False)
        self.checkBox.setObjectName("checkBox")
        self.progressBar = QtWidgets.QProgressBar(Lab)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(30, 220, 341, 23))
        self.progressBar.setProperty("value", 99)
        self.progressBar.setObjectName("progressBar")
        self.toolButton = QtWidgets.QToolButton(Lab)
        self.toolButton.setGeometry(QtCore.QRect(300, 180, 61, 21))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Lab)
        self.buttonBox.accepted.connect(Lab.accept)  # type: ignore
        self.buttonBox.rejected.connect(Lab.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Lab)

    def retranslateUi(self, Lab):
        _translate = QtCore.QCoreApplication.translate
        Lab.setWindowTitle(_translate("Lab", "Lab 2"))
        self.label.setText(_translate("Lab", "Label"))
        self.checkBox_2.setText(_translate("Lab", "Disabled checkbox"))
        self.radioButton.setText(_translate("Lab", "Radio"))
        self.lineEdit.setText(_translate("Lab", "C:\\Users\\"))
        self.radioButton_2.setText(_translate("Lab", "Disabled radio"))
        self.checkBox.setText(_translate("Lab", "Checkbox"))
        self.toolButton.setText(_translate("Lab", "Browse..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Lab = QtWidgets.QDialog()
    ui = Ui_Lab()
    ui.setupUi(Lab)
    Lab.show()
    sys.exit(app.exec_())
