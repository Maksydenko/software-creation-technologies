from PyQt5 import QtCore, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(495, 360)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")

        # Input first number
        self.firstNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.firstNumber.setGeometry(QtCore.QRect(90, 80, 113, 22))
        self.firstNumber.setObjectName("firstNumber")

        # Input second number
        self.secondNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.secondNumber.setGeometry(QtCore.QRect(280, 80, 113, 22))
        self.secondNumber.setObjectName("secondNumber")

        # First number label
        self.firstNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.firstNumberLabel.setGeometry(QtCore.QRect(90, 50, 81, 16))
        self.firstNumberLabel.setObjectName("firstNumberLabel")

        # Second number label
        self.secondNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.secondNumberLabel.setGeometry(QtCore.QRect(280, 50, 101, 16))
        self.secondNumberLabel.setObjectName("secondNumberLabel")

        # Operation label
        self.operationLabel = QtWidgets.QLabel(self.centralwidget)
        self.operationLabel.setGeometry(QtCore.QRect(90, 140, 61, 16))
        self.operationLabel.setObjectName("operationLabel")

        # Summation button
        self.summationButton = QtWidgets.QPushButton(self.centralwidget)
        self.summationButton.setGeometry(QtCore.QRect(90, 170, 31, 28))
        self.summationButton.setObjectName("summationButton")
        self.summationButton.clicked.connect(self.summarize)

        # Subtraction button
        self.subtractionButton = QtWidgets.QPushButton(self.centralwidget)
        self.subtractionButton.setGeometry(QtCore.QRect(140, 170, 31, 28))
        self.subtractionButton.setObjectName("subtractionButton")
        self.subtractionButton.clicked.connect(self.subtract)

        # Multiply button
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget)
        self.multiplyButton.setGeometry(QtCore.QRect(190, 170, 31, 28))
        self.multiplyButton.setObjectName("multiplyButton")
        self.multiplyButton.clicked.connect(self.multiply)

        # Division button
        self.divisionButton = QtWidgets.QPushButton(self.centralwidget)
        self.divisionButton.setGeometry(QtCore.QRect(240, 170, 31, 28))
        self.divisionButton.setObjectName("divisionButton")
        self.divisionButton.clicked.connect(self.divide)

        # Answer label
        self.answerLabel = QtWidgets.QLabel(self.centralwidget)
        self.answerLabel.setGeometry(QtCore.QRect(90, 230, 55, 16))
        self.answerLabel.setObjectName("answerLabel")

        # Answer
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(90, 260, 55, 16))
        self.answer.setObjectName("answer")

        Calculator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))

        self.firstNumberLabel.setText(
            _translate("Calculator", "First number:"))
        self.secondNumberLabel.setText(
            _translate("Calculator", "Second number:"))
        self.operationLabel.setText(_translate("Calculator", "Operation:"))

        self.summationButton.setText(_translate("Calculator", "+"))
        self.subtractionButton.setText(_translate("Calculator", "-"))
        self.multiplyButton.setText(_translate("Calculator", "*"))
        self.divisionButton.setText(_translate("Calculator", "/"))

        self.answerLabel.setText(_translate("Calculator", "Answer:"))
        self.answer.setText(_translate("Calculator", "---"))

    # Check whether the value can be the float
    @staticmethod
    def is_float(value):
        try:
            float(value.text())
            return True
        except ValueError:
            return False

    # Summarize
    def summarize(self):
        first_number = self.firstNumber
        second_number = self.secondNumber
        answer = self.answer
        is_float = self.is_float

        if is_float(first_number) and is_float(second_number):
            result = float(first_number.text()) + \
                float(second_number.text())
            answer.setText(str(result))
        else:
            answer.setText("ValueError")

    # Subtract
    def subtract(self):
        first_number = self.firstNumber
        second_number = self.secondNumber
        answer = self.answer
        is_float = self.is_float

        if is_float(first_number) and is_float(second_number):
            result = float(first_number.text()) - \
                float(second_number.text())
            answer.setText(str(result))
        else:
            answer.setText("ValueError")

    # Multiply
    def multiply(self):
        first_number = self.firstNumber
        second_number = self.secondNumber
        answer = self.answer
        is_float = self.is_float

        if is_float(first_number) and is_float(second_number):
            result = float(first_number.text()) * \
                float(second_number.text())
            answer.setText(str(result))
        else:
            answer.setText("ValueError")

    # Divide
    def divide(self):
        first_number = self.firstNumber
        second_number = self.secondNumber
        answer = self.answer
        is_float = self.is_float

        if is_float(first_number) and self.is_float(second_number):
            result = float(first_number.text()) / \
                float(second_number.text())
            answer.setText(str(result))
        else:
            answer.setText("ValueError")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
