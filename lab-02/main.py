from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.setWindowModality(QtCore.Qt.NonModal)
        Calculator.resize(331, 507)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")

        # Input
        self.input = QtWidgets.QLabel(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 10, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.input.setFont(font)
        self.input.setText("")
        self.input.setObjectName("input")

        # AC
        self.ac = QtWidgets.QPushButton(self.centralwidget)
        self.ac.setGeometry(QtCore.QRect(9, 80, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ac.setFont(font)
        self.ac.setObjectName("ac")
        self.ac.clicked.connect(self.clear_input)

        # Bracket open ( ( )
        self.bracketOpen = QtWidgets.QPushButton(self.centralwidget)
        self.bracketOpen.setGeometry(QtCore.QRect(90, 80, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bracketOpen.setFont(font)
        self.bracketOpen.setObjectName("bracketOpen")
        self.bracketOpen.clicked.connect(self.write_bracket_open)

        # Bracket close ( ) )
        self.bracketClose = QtWidgets.QPushButton(self.centralwidget)
        self.bracketClose.setGeometry(QtCore.QRect(170, 80, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bracketClose.setFont(font)
        self.bracketClose.setObjectName("bracketClose")
        self.bracketClose.clicked.connect(self.write_bracket_close)

        # Division ( / )
        self.division = QtWidgets.QPushButton(self.centralwidget)
        self.division.setGeometry(QtCore.QRect(250, 80, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.division.setFont(font)
        self.division.setObjectName("division")
        self.division.clicked.connect(self.write_division)

        # Multiplication ( * )
        self.multiplication = QtWidgets.QPushButton(self.centralwidget)
        self.multiplication.setGeometry(QtCore.QRect(250, 160, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.multiplication.setFont(font)
        self.multiplication.setObjectName("multiplication")
        self.multiplication.clicked.connect(self.write_multiplication)

        # Subtraction ( - )
        self.subtraction = QtWidgets.QPushButton(self.centralwidget)
        self.subtraction.setGeometry(QtCore.QRect(250, 240, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.subtraction.setFont(font)
        self.subtraction.setObjectName("subtraction")
        self.subtraction.clicked.connect(self.write_minus)

        # Addition ( + )
        self.addition = QtWidgets.QPushButton(self.centralwidget)
        self.addition.setGeometry(QtCore.QRect(250, 320, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.addition.setFont(font)
        self.addition.setObjectName("addition")
        self.addition.clicked.connect(self.write_plus)

        # Result ( = )
        self.result = QtWidgets.QPushButton(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(250, 400, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.result.clicked.connect(self.calc_input)

        # DEL button
        self.delBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delBtn.setGeometry(QtCore.QRect(170, 400, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.delBtn.setFont(font)
        self.delBtn.setObjectName("delBtn")
        self.delBtn.clicked.connect(self.del_symbol)

        # Point ( . )
        self.point = QtWidgets.QPushButton(self.centralwidget)
        self.point.setGeometry(QtCore.QRect(10, 400, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.point.setFont(font)
        self.point.setObjectName("point")
        self.point.clicked.connect(self.write_point)

        # Zero ( 0 )
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(90, 400, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.zero.setFont(font)
        self.zero.setObjectName("zero")
        self.zero.clicked.connect(self.write_zero)

        # One ( 1 )
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(9, 160, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.one.clicked.connect(self.write_one)

        # Two ( 2 )
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(90, 160, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.two.clicked.connect(self.write_two)

        # Three ( 3 )
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(170, 160, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.three.setFont(font)
        self.three.setObjectName("three")
        self.three.clicked.connect(self.write_three)

        # Four ( 4 )
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(10, 240, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.four.setFont(font)
        self.four.setObjectName("four")
        self.four.clicked.connect(self.write_four)

        # Five ( 5 )
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(90, 240, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.five.setFont(font)
        self.five.setObjectName("five")
        self.five.clicked.connect(self.write_five)

        # Six ( 6 )
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(170, 240, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.six.setFont(font)
        self.six.setObjectName("six")
        self.six.clicked.connect(self.write_six)

        # Seven ( 7 )
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(10, 320, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.seven.setFont(font)
        self.seven.setObjectName("seven")
        self.seven.clicked.connect(self.write_seven)

        # Eight ( 8 )
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(90, 320, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.eight.setFont(font)
        self.eight.setObjectName("eight")
        self.eight.clicked.connect(self.write_eight)

        # Nine ( 9 )
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(170, 320, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.nine.setFont(font)
        self.nine.setObjectName("nine")
        self.nine.clicked.connect(self.write_nine)

        Calculator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.ac.setText(_translate("Calculator", "AC"))
        self.bracketOpen.setText(_translate("Calculator", "("))
        self.bracketClose.setText(_translate("Calculator", ")"))
        self.division.setText(_translate("Calculator", "/"))
        self.multiplication.setText(_translate("Calculator", "*"))
        self.subtraction.setText(_translate("Calculator", "-"))
        self.addition.setText(_translate("Calculator", "+"))
        self.result.setText(_translate("Calculator", "="))
        self.delBtn.setText(_translate("Calculator", "DEL"))
        self.point.setText(_translate("Calculator", "."))
        self.zero.setText(_translate("Calculator", "0"))
        self.one.setText(_translate("Calculator", "1"))
        self.two.setText(_translate("Calculator", "2"))
        self.three.setText(_translate("Calculator", "3"))
        self.four.setText(_translate("Calculator", "4"))
        self.five.setText(_translate("Calculator", "5"))
        self.six.setText(_translate("Calculator", "6"))
        self.seven.setText(_translate("Calculator", "7"))
        self.eight.setText(_translate("Calculator", "8"))
        self.nine.setText(_translate("Calculator", "9"))

    def clear_input(self):
        equation = ""
        self.input.setText(str(equation))

    def write_bracket_open(self):
        equation = self.input.text()
        equation += "("
        self.input.setText(str(equation))

    def write_bracket_close(self):
        equation = self.input.text()
        if len(equation):
            equation += ")"
        self.input.setText(str(equation))

    def write_division(self):
        equation = self.input.text()

        if len(equation):
            if equation[-1] == "*" or equation[-1] == "/" or equation[-1] == "+" or equation[-1] == "-":
                equation = equation[:-1]
            equation += "/"
        self.input.setText(str(equation))

    def write_multiplication(self):
        equation = self.input.text()

        if len(equation):
            if equation[-1] == "*" or equation[-1] == "/" or equation[-1] == "+" or equation[-1] == "-":
                equation = equation[:-1]
            equation += "*"
        self.input.setText(str(equation))

    def write_minus(self):
        equation = self.input.text()

        if len(equation):
            if equation[-1] == "*" or equation[-1] == "/" or equation[-1] == "+" or equation[-1] == "-":
                equation = equation[:-1]
        equation += "-"
        self.input.setText(str(equation))

    def write_plus(self):
        equation = self.input.text()

        if len(equation):
            if equation[-1] == "*" or equation[-1] == "/" or equation[-1] == "+" or equation[-1] == "-":
                equation = equation[:-1]
            equation += "+"
        self.input.setText(str(equation))

    def calc_input(self):
        equation = self.input.text()

        if equation[-1] != "(" and equation[-1] != "*" and equation[-1] != "/" and equation[-1] != "+" and equation[-1] != "-" and equation[-1] != ".":
            try:
                self.input.setText(str(eval(equation)))
            except:
                return self.input.setText("Error")

    def del_symbol(self):
        equation = self.input.text()
        equation = equation[:-1]
        self.input.setText(str(equation))

    def write_point(self):
        equation = self.input.text()

        if len(equation):
            if equation[-1] == ".":
                equation = equation[:-1]
        equation += "."
        self.input.setText(str(equation))

    def write_zero(self):
        equation = self.input.text()
        equation += "0"
        self.input.setText(str(equation))

    def write_one(self):
        equation = self.input.text()
        equation += "1"
        self.input.setText(str(equation))

    def write_two(self):
        equation = self.input.text()
        equation += "2"
        self.input.setText(str(equation))

    def write_three(self):
        equation = self.input.text()
        equation += "3"
        self.input.setText(str(equation))

    def write_four(self):
        equation = self.input.text()
        equation += "4"
        self.input.setText(str(equation))

    def write_five(self):
        equation = self.input.text()
        equation += "5"
        self.input.setText(str(equation))

    def write_six(self):
        equation = self.input.text()
        equation += "6"
        self.input.setText(str(equation))

    def write_seven(self):
        equation = self.input.text()
        equation += "7"
        self.input.setText(str(equation))

    def write_eight(self):
        equation = self.input.text()
        equation += "8"
        self.input.setText(str(equation))

    def write_nine(self):
        equation = self.input.text()
        equation += "9"
        self.input.setText(str(equation))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
