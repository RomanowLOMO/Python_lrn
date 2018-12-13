# ! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.layout = QGridLayout()
        self.checkbox = QCheckBox("Я управляю состоянием кнопок", self)
        self.push1 = QPushButton("Я кнопка, вызывающая QMessageBox", self)
        self.push2 = QPushButton("Я буду увеличивать значение SpinBox", self)
        self.push3 = QPushButton("Я буду уменьшать значение SpinBox", self)
        self.spin = QSpinBox(self)
        self.slider = QSlider(Qt.Horizontal, self)
        self.spin.setRange(0, 25)
        self.spin.setValue(0)
        self.slider.setRange(0, 25)
        self.line = QLineEdit(self)
        self.line.setReadOnly(True)
        self.checkbox.setChecked(True)
        self.layout.addWidget(self.checkbox, 0, 0, 1, 2)
        self.layout.addWidget(self.push1, 0, 2)
        self.layout.addWidget(self.push2, 0, 3)
        self.layout.addWidget(self.push3, 0, 4)
        self.layout.addWidget(self.spin, 1, 0)
        self.layout.addWidget(self.slider, 1, 1, 1, 3)
        self.layout.addWidget(self.line, 1, 4)
        self.setLayout(self.layout)
        self.setWindowTitle("Lambdas")

        # self.checkbox.stateChanged.connect(self.onCheckBoxStateChanged)
        # self.spin.valueChanged.connect(self.onSpinBoxValueChanged)
        # self.slider.valueChanged.connect(self.onSliderValueChanged)
        # self.push1.clicked.connect(self.onPush1Clicked)
        # self.push2.clicked.connect(self.onPush2Clicked)
        # self.push3.clicked.connect(self.onPush3Clicked)

        self.push2.clicked.connect(lambda: self.spin.setValue(self.spin.value() + 1))
        self.push3.clicked.connect(lambda: self.spin.setValue(self.spin.value() - 1))

        def onCheckBoxStateChanged(self):
            if not self.checkbox.isChecked():
                self.push1.setDisabled(True)
                self.push2.setDisabled(True)
                self.push3.setDisabled(True)
            else:
                self.push1.setEnabled(True)
                self.push2.setEnabled(True)
                self.push3.setEnabled(True)

        def onSpinBoxValueChanged(self, value):
            self.slider.setValue(value)
            if value > 10:
                self.line.setText("Warning!")
            else:
                self.line.setText("")

        def onSliderValueChanged(self, value):
            self.spin.setValue(value)
            if value > 10:
                self.line.setText("Warning!")
            else:
                self.line.setText("")

        def onPush1Clicked(self):
            if self.line.text() == "":
                QMessageBox.information(self, "Information", str(self.spin.value()))
            else:
                QMessageBox.critical(self, "Error", self.line.text())

        def onPush2Clicked(self):
            self.spin.setValue(self.spin.value() + 1)

        def onPush3Clicked(self):
            self.spin.setValue(self.spin.value() - 1)


def main():
    application = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(application.exec())


if __name__ == "__main__":
    main()