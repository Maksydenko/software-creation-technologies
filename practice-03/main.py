import urllib.request
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Practice3(object):
    def setupUi(self, Practice3):
        Practice3.setObjectName("Practice3")
        Practice3.resize(501, 616)
        self.centralwidget = QtWidgets.QWidget(Practice3)
        self.centralwidget.setObjectName("centralwidget")

        # Stadium section

        # Title stadium section
        self.stadium_title = QtWidgets.QLabel(self.centralwidget)
        self.stadium_title.setGeometry(QtCore.QRect(20, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.stadium_title.setFont(font)
        self.stadium_title.setObjectName("stadium_title")

        # Stadium choice

        self.santiago_bernabeu = QtWidgets.QPushButton(self.centralwidget)
        self.santiago_bernabeu.setGeometry(QtCore.QRect(30, 70, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.santiago_bernabeu.setFont(font)
        self.santiago_bernabeu.setObjectName("santiago_bernabeu")
        self.santiago_bernabeu.clicked.connect(self.show_santiago_bernabeu)

        self.allianz_arena = QtWidgets.QPushButton(self.centralwidget)
        self.allianz_arena.setGeometry(QtCore.QRect(30, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.allianz_arena.setFont(font)
        self.allianz_arena.setObjectName("allianz_arena")
        self.allianz_arena.clicked.connect(self.show_allianz_arena)

        self.old_trafford = QtWidgets.QPushButton(self.centralwidget)
        self.old_trafford.setGeometry(QtCore.QRect(30, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.old_trafford.setFont(font)
        self.old_trafford.setObjectName("old_trafford")
        self.old_trafford.clicked.connect(self.show_old_trafford)

        # Night mode
        self.night_mode = QtWidgets.QCheckBox(self.centralwidget)
        self.night_mode.setGeometry(QtCore.QRect(30, 190, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.night_mode.setFont(font)
        self.night_mode.setObjectName("night_mode")

        # Stadium img
        self.stadium_img = QtWidgets.QLabel(self.centralwidget)
        self.stadium_img.setGeometry(QtCore.QRect(220, 70, 261, 151))
        self.stadium_img.setObjectName("stadium_img")

        # Stadium info
        self.stadium_info = QtWidgets.QLabel(self.centralwidget)
        self.stadium_info.setGeometry(QtCore.QRect(220, 230, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stadium_info.setFont(font)
        self.stadium_info.setText("")
        self.stadium_info.setObjectName("stadium_info")

        # Pizza section

        # Title pizza section
        self.pizza_title = QtWidgets.QLabel(self.centralwidget)
        self.pizza_title.setGeometry(QtCore.QRect(20, 280, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pizza_title.setFont(font)
        self.pizza_title.setObjectName("pizza_title")

        # Pizza size

        self.pizza_size = QtWidgets.QLabel(self.centralwidget)
        self.pizza_size.setGeometry(QtCore.QRect(30, 330, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pizza_size.setFont(font)
        self.pizza_size.setObjectName("pizza_size")

        self.pizza_large = QtWidgets.QRadioButton(self.centralwidget)
        self.pizza_large.setGeometry(QtCore.QRect(40, 370, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pizza_large.setFont(font)
        self.pizza_large.setObjectName("pizza_large")

        self.pizza_medium = QtWidgets.QRadioButton(self.centralwidget)
        self.pizza_medium.setGeometry(QtCore.QRect(40, 410, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pizza_medium.setFont(font)
        self.pizza_medium.setObjectName("pizza_medium")

        self.pizza_small = QtWidgets.QRadioButton(self.centralwidget)
        self.pizza_small.setGeometry(QtCore.QRect(40, 450, 82, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pizza_small.setFont(font)
        self.pizza_small.setObjectName("pizza_small")

        # Additional pizza ingredients

        self.pizza_additional_ingridients = QtWidgets.QLabel(
            self.centralwidget)
        self.pizza_additional_ingridients.setGeometry(
            QtCore.QRect(160, 330, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pizza_additional_ingridients.setFont(font)
        self.pizza_additional_ingridients.setObjectName(
            "pizza_additional_ingridients")

        self.mushrooms = QtWidgets.QCheckBox(self.centralwidget)
        self.mushrooms.setGeometry(QtCore.QRect(170, 370, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mushrooms.setFont(font)
        self.mushrooms.setObjectName("mushrooms")

        self.pineapple = QtWidgets.QCheckBox(self.centralwidget)
        self.pineapple.setGeometry(QtCore.QRect(170, 410, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pineapple.setFont(font)
        self.pineapple.setObjectName("pineapple")

        self.corn = QtWidgets.QCheckBox(self.centralwidget)
        self.corn.setGeometry(QtCore.QRect(170, 450, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.corn.setFont(font)
        self.corn.setObjectName("corn")

        self.bacon = QtWidgets.QCheckBox(self.centralwidget)
        self.bacon.setGeometry(QtCore.QRect(310, 370, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bacon.setFont(font)
        self.bacon.setObjectName("bacon")

        self.ham = QtWidgets.QCheckBox(self.centralwidget)
        self.ham.setGeometry(QtCore.QRect(310, 410, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ham.setFont(font)
        self.ham.setObjectName("ham")

        self.salmo = QtWidgets.QCheckBox(self.centralwidget)
        self.salmo.setGeometry(QtCore.QRect(310, 450, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.salmo.setFont(font)
        self.salmo.setObjectName("salmo")

        # Pizza price

        self.pizza_get_price = QtWidgets.QPushButton(self.centralwidget)
        self.pizza_get_price.setGeometry(QtCore.QRect(30, 500, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pizza_get_price.setFont(font)
        self.pizza_get_price.setObjectName("pizza_get_price")
        self.pizza_get_price.clicked.connect(self.get_pizza_price)

        self.pizza_price = QtWidgets.QLabel(self.centralwidget)
        self.pizza_price.setGeometry(QtCore.QRect(30, 540, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pizza_price.setFont(font)
        self.pizza_price.setObjectName("pizza_price")

        Practice3.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Practice3)
        self.statusbar.setObjectName("statusbar")
        Practice3.setStatusBar(self.statusbar)

        self.retranslateUi(Practice3)
        QtCore.QMetaObject.connectSlotsByName(Practice3)

    def retranslateUi(self, Practice3):
        _translate = QtCore.QCoreApplication.translate
        Practice3.setWindowTitle(_translate("Practice3", "Practice 3"))
        self.stadium_title.setText(_translate("Practice3", "View the stadium"))
        self.santiago_bernabeu.setText(
            _translate("Practice3", "Santiago Bernabéu"))
        self.allianz_arena.setText(_translate("Practice3", "Allianz Arena"))
        self.old_trafford.setText(_translate("Practice3", "Old Trafford"))
        self.night_mode.setText(_translate("Practice3", "Night"))
        self.pizza_title.setText(_translate("Practice3", "Order pizza"))
        self.pizza_size.setText(_translate("Practice3", "Size:"))
        self.pizza_large.setText(_translate("Practice3", "Large"))
        self.pizza_medium.setText(_translate("Practice3", "Medium"))
        self.pizza_small.setText(_translate("Practice3", "Small"))
        self.pizza_additional_ingridients.setText(
            _translate("Practice3", "Additional ingredients:"))
        self.mushrooms.setText(_translate("Practice3", "Mushrooms"))
        self.pineapple.setText(_translate("Practice3", "Pineapple"))
        self.corn.setText(_translate("Practice3", "Corn"))
        self.bacon.setText(_translate("Practice3", "Bacon"))
        self.ham.setText(_translate("Practice3", "Ham"))
        self.salmo.setText(_translate("Practice3", "Salmon"))
        self.pizza_get_price.setText(_translate("Practice3", "Get the price"))
        self.pizza_price.setText(_translate("Practice3", "Price: $0"))

    # Links to stadium images

    SANTIAGO_BERNABEU_IMG = "https://www.realmadrid.com/cs/Satellite?blobcol=urldata&blobheader=image%2Fjpeg&blobkey=id&blobtable=MungoBlobs&blobwhere=1203423418605&ssbinary=true"
    SANTIAGO_BERNABEU_NIGHT_IMG = "https://www.realmadrid.com/img/sc_1920px/reforma-del-estadio-santiago-bernabeu-05_20220124034518.jpg"
    ALLIANZ_ARENA_IMG = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Allianz-Arena-M%C3%BCnchen.jpg/1200px-Allianz-Arena-M%C3%BCnchen.jpg"
    ALLIANZ_ARENA_NIGHT_IMG = "https://upload.wikimedia.org/wikipedia/commons/3/36/Allianz_arena_at_night_Richard_Bartz.jpg"
    OLD_TRAFFORD_IMG = "https://i2-prod.manchestereveningnews.co.uk/sport/football/article24067811.ece/ALTERNATES/s615/0_GettyImages-1384570281.jpg"
    OLD_TRAFFORD_NIGHT_IMG = "https://assets.manutd.com/AssetPicker/images/0/0/17/106/1141450/GettyImages_14208441201662471639973_large.jpg "

    # Stadium section

    def show_santiago_bernabeu(self):
        if self.night_mode.isChecked():
            data = urllib.request.urlopen(
                self.SANTIAGO_BERNABEU_NIGHT_IMG).read()
        else:
            data = urllib.request.urlopen(
                self.SANTIAGO_BERNABEU_IMG).read()
        img = QtGui.QPixmap()
        img.loadFromData(data)
        self.stadium_img.setPixmap(img)
        self.stadium_img.setScaledContents(True)
        self.stadium_info.setText("Football stadium in Madrid")

    def show_allianz_arena(self):
        if self.night_mode.isChecked():
            data = urllib.request.urlopen(
                self.ALLIANZ_ARENA_NIGHT_IMG).read()
        else:
            data = urllib.request.urlopen(
                self.ALLIANZ_ARENA_IMG).read()
        img = QtGui.QPixmap()
        img.loadFromData(data)
        self.stadium_img.setPixmap(img)
        self.stadium_img.setScaledContents(True)
        self.stadium_info.setText("Football stadium in Munich")

    def show_old_trafford(self):
        if self.night_mode.isChecked():
            data = urllib.request.urlopen(
                self.OLD_TRAFFORD_NIGHT_IMG).read()
        else:
            data = urllib.request.urlopen(
                self.OLD_TRAFFORD_IMG).read()
        img = QtGui.QPixmap()
        img.loadFromData(data)
        self.stadium_img.setPixmap(img)
        self.stadium_img.setScaledContents(True)
        self.stadium_info.setText("Football stadium in Manchester")

    # Pizza section

    def get_pizza_price(self):
        price_value = 0

        # Pizza size
        if self.pizza_large.isChecked():
            price_value = 15
        if self.pizza_medium.isChecked():
            price_value = 10
        if self.pizza_small.isChecked():
            price_value = 5

        # Additional pizza ingredients
        if self.mushrooms.isChecked():
            price_value += 0.5
        if self.pineapple.isChecked():
            price_value += 0.5
        if self.corn.isChecked():
            price_value += 0.5
        if self.bacon.isChecked():
            price_value += 0.5
        if self.ham.isChecked():
            price_value += 0.5
        if self.salmo.isChecked():
            price_value += 0.5

        price = f"Price: ${price_value}"
        self.pizza_price.setText(price)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Practice3 = QtWidgets.QMainWindow()
    ui = Ui_Practice3()
    ui.setupUi(Practice3)
    Practice3.show()
    sys.exit(app.exec_())
