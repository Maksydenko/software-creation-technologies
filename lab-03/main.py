from sys import argv, exit
from random import randint, choice
from urllib import request

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton
from PyQt5.QtGui import QFont, QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # Constants

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 450

    DEFAULT_TITLE_STYLES = "font-size: 24px; \
      font-weight: 700; \
        color: #333333;"
    DEFAULT_RADIO_STYLES = "font-size: 16px; \
      font-weight: 600; \
        color: #333333;"
    DEFAULT_BUTTON_STYLES = "font-size: 16px; \
      font-weight: 500; \
        border-radius: 5px;"

    TEMPLATE_IMG_URL = "https://raw.githubusercontent.com/Maksydenko/olegity/master/src/src/assets/img/concerts/webp/concert"

    LABELS = [
        "HTML",
        "CSS",
        "SCSS",
        "JavaScript",
        "TypeScript",
        "React",
        "Redux Toolkit",
        "Next.js",
        "Webpack",
        "Git",
    ]

    FONT_FAMILIES = [
        "Arial",
        "Times New Roman",
        "Courier New",
        "Impact",
        "Comic Sans MS",
    ]
    BORDER_STYLES = [
        "dotted",
        "dashed",
        "solid",
        "double",
        "groove",
        "ridge",
        "inset",
        "outside",
    ]
    TEXT_TRANSFORMS = ["capitalize", "uppercase", "lowercase"]

    def initUI(self):
        # Image
        self.img = QLabel(self)

        # Title
        self.title = QLabel(self)
        self.title.setText("Frontend")
        self.title.setStyleSheet(self.DEFAULT_TITLE_STYLES)
        self.title.move(200, 100)

        # Radios

        self.move_items_radio = QRadioButton("Turn on move items", self)
        self.move_items_radio.setStyleSheet(self.DEFAULT_RADIO_STYLES)
        self.move_items_radio.setChecked(True)
        self.move_items_radio.move(200, 150)

        self.static_items_radio = QRadioButton("Turn off move items", self)
        self.static_items_radio.setStyleSheet(self.DEFAULT_RADIO_STYLES)
        self.static_items_radio.move(200, 190)

        # Buttons

        self.main_button = QPushButton("Change all", self)
        self.main_button.setStyleSheet(
            self.DEFAULT_BUTTON_STYLES + self.get_colorize_styles("#170c10", "#1edd63")
        )
        self.main_button.move(200, 240)
        self.main_button.clicked.connect(self.handle_click_button)

        self.reserve_button = QPushButton("Reserve change all", self)
        self.reserve_button.setStyleSheet(
            self.DEFAULT_BUTTON_STYLES + self.get_colorize_styles("#001e36", "#31a7fd")
        )
        self.reserve_button.move(200, 280)
        self.reserve_button.clicked.connect(self.handle_click_button)

        self.resize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowTitle("Lab 3")
        self.show()

    # Static methods

    @staticmethod
    def get_img_number():
        img_number = randint(1, 20)

        if img_number < 10:
            img_number = f"0{img_number}"
        return img_number

    @staticmethod
    def get_size(max_width, max_height):
        min_width = max_width // 1.5
        min_height = max_height // 1.5

        width = randint(min_width, max_width)
        height = randint(min_height, max_height)
        return width, height

    @staticmethod
    def get_colorize_styles(color, background_color):
        return f"border: 2px solid {color}; color: {color}; background-color: {background_color}"

    # Common methods

    def generate_styles(self):
        font_size = f"{randint(12, 24)}px"
        font_weight = randint(1, 9) * 100
        color = f"#{randint(100000, 999999)}"
        border_radius = f"{randint(0, 50)}px"
        border = f"{randint(1, 5)}px {choice(self.BORDER_STYLES)} {color}"
        background_color = f"#{randint(100000, 999999)}"

        return f"font-size: {font_size}; \
          font-weight: {font_weight}; \
            border-radius: {border_radius}; \
              border: {border}; \
                color: {color}; \
                  background-color: {background_color}; \
                    text-transform: {choice(self.TEXT_TRANSFORMS)};"

    def handle_change_text(self, object, max_width, max_height):
        font = QFont()
        font.setFamily(choice(self.FONT_FAMILIES))

        object.setFont(font)
        object.resize(*self.get_size(max_width, max_height))
        object.setStyleSheet(self.generate_styles())

    def get_coords(self, max_width, max_height, padding=15):
        x = self.WINDOW_WIDTH - (max_width + padding)
        y = self.WINDOW_HEIGHT - (max_height + padding)

        x = randint(padding, x)
        y = randint(padding, y)
        return x, y

    # Image change
    def handle_change_img(self):
        img_url = f"{self.TEMPLATE_IMG_URL}-{self.get_img_number()}.webp"
        data = request.urlopen(img_url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)

        self.img.resize(*self.get_size(300, 300))
        self.img.setPixmap(pixmap)
        self.img.setScaledContents(True)

    # Label change
    def handle_change_title(self):
        self.handle_change_text(self.title, 225, 50)
        self.title.setText(choice(self.LABELS))

    # Move items radio change
    def handle_change_move_radio(self):
        self.handle_change_text(self.move_items_radio, 375, 50)

    # Static items radio change
    def handle_change_static_radio(self):
        self.handle_change_text(self.static_items_radio, 375, 50)

    # Main button change
    def handle_change_main_button(self):
        self.handle_change_text(self.main_button, 275, 50)

    # Reserve button change
    def handle_change_reserve_button(self):
        self.handle_change_text(self.reserve_button, 375, 50)

    # Move items
    def handle_move_items(self):
        self.img.move(*self.get_coords(300, 300))
        self.title.move(*self.get_coords(300, 50))
        self.move_items_radio.move(*self.get_coords(300, 50))
        self.static_items_radio.move(*self.get_coords(300, 50))
        self.main_button.move(*self.get_coords(300, 50))
        self.reserve_button.move(*self.get_coords(375, 450, 0))

    # Click on button
    def handle_click_button(self):
        self.window().setStyleSheet(f"background-color: #{randint(100000, 999999)}")
        self.handle_change_img()
        self.handle_change_title()
        self.handle_change_move_radio()
        self.handle_change_static_radio()
        self.handle_change_main_button()
        self.handle_change_reserve_button()

        if self.move_items_radio.isChecked():
            self.handle_move_items()


if __name__ == "__main__":
    app = QApplication(argv)
    ex = Example()
    exit(app.exec_())
