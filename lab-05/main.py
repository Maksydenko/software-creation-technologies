from sys import argv
from json import load, dump
from PyQt5.QtWidgets import (
    QPushButton,
    QLineEdit,
    QLabel,
    QWidget,
    QApplication,
    QMainWindow,
    QGridLayout,
    QTableWidget,
    QTableWidgetItem,
    QAction,
    QToolBar,
    QShortcut,
)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lab 5")
        self.setMinimumSize(QSize(389, 580))
        # Create a central widget
        central_widget = QWidget(self)
        # Install the central widget
        self.setCentralWidget(central_widget)

        self.toolbar = QToolBar("Toolbar")
        self.addToolBar(self.toolbar)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu("File")
        openAction = QAction(QIcon("icons/open.svg"), "Open", self)
        openAction.triggered.connect(self.handle_open)
        openAction_shortcut = QShortcut(QKeySequence("Ctrl+O"), self)
        openAction_shortcut.activated.connect(self.handle_open)
        fileMenu.addAction(openAction)

        saveAction = QAction(QIcon("icons/save.svg"), "Save", self)
        saveAction.triggered.connect(self.handle_save)
        saveAction_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        saveAction_shortcut.activated.connect(self.handle_save)
        fileMenu.addAction(saveAction)

        editMenu = menubar.addMenu("Edit")
        cutAction = QAction(QIcon("icons/cut.svg"), "Cut", self)
        cutAction.triggered.connect(self.handle_copy)
        cutAction_shortcut = QShortcut(QKeySequence("Ctrl+X"), self)
        cutAction_shortcut.activated.connect(self.handle_cut)
        editMenu.addAction(cutAction)

        copyAction = QAction(QIcon("icons/copy.svg"), "Copy", self)
        copyAction.triggered.connect(self.handle_copy)
        copyAction_shortcut = QShortcut(QKeySequence("Ctrl+C"), self)
        copyAction_shortcut.activated.connect(self.handle_copy)
        editMenu.addAction(copyAction)

        pasteAction = QAction(QIcon("icons/paste.svg"), "Paste", self)
        pasteAction.triggered.connect(self.handle_past)
        pasteAction_shortcut = QShortcut(QKeySequence("Ctrl+V"), self)
        pasteAction_shortcut.activated.connect(self.handle_past)
        editMenu.addAction(pasteAction)

        # Create QGridLayout
        grid_layout = QGridLayout(self)
        # Set this layout in central widget
        central_widget.setLayout(grid_layout)

        # Lines edit

        self.name = QLineEdit()
        self.name.setPlaceholderText("Input name")
        self.name.setStyleSheet("border: 1px solid #dbdbdb;")

        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText("Input last name")
        self.last_name.setStyleSheet("border: 1px solid #dbdbdb;")

        self.age = QLineEdit()
        self.age.setPlaceholderText("Input age")
        self.age.setStyleSheet("border: 1px solid #dbdbdb;")

        # Buttons

        self.add_row_button = QPushButton("Add row")
        self.add_row_button.clicked.connect(self.add_row)

        self.remove_row_button = QPushButton("Remove row")
        self.remove_row_button.clicked.connect(self.remove_row)

        self.remove_column_button = QPushButton("Remove column")
        self.remove_column_button.clicked.connect(self.remove_column)

        employees = [
            {"First Name": "John", "Last Name": "Doe", "Age": 25},
            {"First Name": "Jane", "Last Name": "Doe", "Age": 22},
            {"First Name": "Alice", "Last Name": "Doe", "Age": 22},
        ]

        self.table = QTableWidget(self)
        self.table.setMaximumHeight = 200
        self.table.setMaximumWidth = 300
        self.table.show()
        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 50)
        self.table.setHorizontalHeaderLabels(employees[0].keys())
        self.table.setRowCount(len(employees))

        row = 0
        for e in employees:
            self.table.setItem(row, 0, QTableWidgetItem(e["First Name"]))
            self.table.setItem(row, 1, QTableWidgetItem(e["Last Name"]))
            self.table.setItem(row, 2, QTableWidgetItem(str(e["Age"])))
            row += 1

        self.counter = QLabel(
            f"Total rows: {self.table.rowCount()}\t"
            f"Total columns: {self.table.columnCount()}"
        )

        self.active = QLabel(f"Active row: 0\tActive column: 0")

        # Adding the table to the grid
        grid_layout.addWidget(self.table, 0, 0)
        grid_layout.addWidget(self.counter, 1, 0)
        grid_layout.addWidget(self.add_row_button, 2, 0)
        grid_layout.addWidget(self.name, 3, 0)
        grid_layout.addWidget(self.last_name, 4, 0)
        grid_layout.addWidget(self.age, 5, 0)
        grid_layout.addWidget(self.active, 6, 0)
        grid_layout.addWidget(self.remove_row_button, 7, 0)
        grid_layout.addWidget(self.remove_column_button, 8, 0)

        self.table.cellClicked.connect(self.update_active_cell)

    global clipboard

    # Toolbar methods

    def handle_cut(self):
        try:
            global clipboard

            selected_items = self.table.selectedItems()
            selected_item = selected_items[0]
            text = selected_item.text()
            clipboard = [text]

            row = selected_item.row()
            column = selected_item.column()
            self.table.setItem(row, column, QTableWidgetItem(""))
            return clipboard
        except:
            return

    def handle_copy(self):
        try:
            global clipboard

            selected_items = self.table.selectedItems()
            selected_item = selected_items[0]
            text = selected_item.text()
            clipboard = [text]
            return clipboard
        except:
            return

    def handle_past(self):
        try:
            global clipboard

            selected_items = self.table.selectedItems()
            selected_item = selected_items[0]
            row = selected_item.row()
            column = selected_item.column()

            self.table.setItem(row, column, QTableWidgetItem(str(clipboard[0])))
        except:
            return

    def handle_open(self):
        try:
            with open("data.json", "r") as f:
                data = load(f)

            num_rows = max([int(key.split("_")[0]) for key in data.keys()]) + 1
            num_cols = max([int(key.split("_")[1]) for key in data.keys()]) + 1

            self.table.setRowCount(num_rows)
            self.table.setColumnCount(num_cols)

            for key, value in data.items():
                row_idx = int(key.split("_")[0])
                col_idx = int(key.split("_")[1])
                item = QTableWidgetItem(str(value))
                self.table.setItem(row_idx, col_idx, item)
        except:
            return

    def handle_save(self):
        data = {}
        num_rows = self.table.rowCount()
        num_cols = self.table.columnCount()

        for row in range(num_rows):
            for col in range(num_cols):
                cell_value = self.table.item(row, col).text()
                data[f"{row}_{col}"] = cell_value

        with open("data.json", "w") as f:
            dump(data, f, indent=4)

    # Check whether the value can be the int
    @staticmethod
    def is_int(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    # Add row
    def add_row(self):
        row_position = self.table.rowCount()
        name = self.name.text()
        last_name = self.last_name.text()
        age = self.age.text()

        self.name.setStyleSheet("border: 1px solid #dbdbdb;")
        self.last_name.setStyleSheet("border: 1px solid #dbdbdb;")
        self.age.setStyleSheet("border: 1px solid #dbdbdb;")

        if len(name) and len(last_name) and self.is_int(self.age.text()):
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(name))
            self.table.setItem(row_position, 1, QTableWidgetItem(last_name))
            self.table.setItem(row_position, 2, QTableWidgetItem(age))

            self.counter.setText(
                f"Total rows: {self.table.rowCount()}\t"
                f"Total columns: {self.table.columnCount()}"
            )
            self.name.setText("")
            self.last_name.setText("")
            self.age.setText("")
        else:
            if not len(name):
                self.name.setStyleSheet("border: 1px solid red;")
            if not len(last_name):
                self.last_name.setStyleSheet("border: 1px solid red;")
            if not len(age):
                self.age.setStyleSheet("border: 1px solid red;")
            else:
                if not self.is_int(age):
                    self.age.setStyleSheet("border: 1px solid red;")

    # Remove row
    def remove_row(self):
        active_row = self.table.currentRow()

        self.table.removeRow(active_row)
        self.counter.setText(
            f"Total rows: {self.table.rowCount()}\t"
            f"Total columns: {self.table.columnCount()}"
        )

    # Remove column
    def remove_column(self):
        if self.table.columnCount() > 1:
            active_column = self.table.currentColumn()

            self.table.removeColumn(active_column)
            self.counter.setText(
                f"Total rows: {self.table.rowCount()}\t"
                f"Total columns: {self.table.columnCount()}"
            )

    # Update active cell
    def update_active_cell(self, row, column):
        self.active.setText(f"Active row: {row + 1}\tActive column: {column + 1}")


app = QApplication(argv)
window = MainWindow()
window.show()
app.exec()
