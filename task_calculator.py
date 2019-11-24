import sys
from PySide2.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QGridLayout


class Form(QWidget):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.setWindowTitle("Calculator")
        self.resize(300,250)
        self.move(750,300)
        self.label=QLabel()
        self.label1=QLabel()
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.button4 = QPushButton("4")
        self.button5 = QPushButton("5")
        self.button6 = QPushButton("6")
        self.button7 = QPushButton("7")
        self.button8 = QPushButton("8")
        self.button9 = QPushButton("9")
        self.button0 = QPushButton("0")
        self.buttonadd = QPushButton("+")
        self.buttonsub = QPushButton("-")
        self.buttondiv = QPushButton("/")
        self.buttonmult = QPushButton("*")
        self.buttoneq = QPushButton("=")
        self.buttondel = QPushButton("C")

        layout = QGridLayout()
        layout.addWidget(self.label,0,0)
        layout.addWidget(self.label1,1,0)
        layout.addWidget(self.button1,4,0)
        layout.addWidget(self.button2,4,1)
        layout.addWidget(self.button3,4,2)
        layout.addWidget(self.button4,5,0)
        layout.addWidget(self.button5,5,1)
        layout.addWidget(self.button6,5,2)
        layout.addWidget(self.button7,6,0)
        layout.addWidget(self.button8,6,1)
        layout.addWidget(self.button9,6,2)
        layout.addWidget(self.button0,7,1)
        layout.addWidget(self.buttonadd,4,3)
        layout.addWidget(self.buttonsub,4,4)
        layout.addWidget(self.buttondiv,5,3)
        layout.addWidget(self.buttonmult,5,4)
        layout.addWidget(self.buttoneq,6,4)
        layout.addWidget(self.buttondel,6,3)

        self.setLayout(layout)
        self.button1.clicked.connect(self.pressed_button_numb)
        self.button2.clicked.connect(self.pressed_button_numb)
        self.button3.clicked.connect(self.pressed_button_numb)
        self.button4.clicked.connect(self.pressed_button_numb)
        self.button5.clicked.connect(self.pressed_button_numb)
        self.button6.clicked.connect(self.pressed_button_numb)
        self.button7.clicked.connect(self.pressed_button_numb)
        self.button8.clicked.connect(self.pressed_button_numb)
        self.button9.clicked.connect(self.pressed_button_numb)
        self.button0.clicked.connect(self.pressed_button_numb)
        self.buttonadd.clicked.connect(self.pressed_button)
        self.buttonsub.clicked.connect(self.pressed_button)
        self.buttondiv.clicked.connect(self.pressed_button)
        self.buttonmult.clicked.connect(self.pressed_button)
        self.buttoneq.clicked.connect(self.function_result)
        self.buttondel.clicked.connect(self.delit_all)

    def delit_all(self):
        self.label.clear()
        self.label1.clear()

    def pressed_button_numb(self):
        self.button1=self.sender()
        self.label1.setText(self.label1.text() + self.button1.text())


    def pressed_button(self):
        self.button=self.sender()
        self.first_value = float(self.label1.text())
        self.label1.clear()
        self.label.setText(str(self.first_value)+self.button.text())

    def determinate_second_value(self):
        self.second_value = float(self.label1.text())
        self.label1.clear()
        self.label.setText(str(self.first_value) + self.button.text() + str(self.second_value))

    def function_addition(self):
        self.determinate_second_value()
        self.result = float(self.first_value + self.second_value)
        self.total_result()

    def function_subtraction(self):
        self.determinate_second_value()
        self.result = float(self.first_value - self.second_value)
        self.total_result()

    def function_divison(self):
        self.determinate_second_value()
        self.result = float(self.first_value / self.second_value)
        self.total_result()

    def function_multiply(self):
        self.determinate_second_value()
        self.result = float(self.first_value * self.second_value)
        self.total_result()

    def total_result(self):
         self.label.setText(str(self.first_value) + self.button.text() + str(self.second_value) + " = " + str(self.result))
         self.label1.clear()

    def function_result(self):
        if self.button.text() == '+':
            self.function_addition()
        elif self.button.text() == '-':
            self.function_subtraction()
        elif self.button.text() == "/":
            self.function_divison()
        elif self.button.text() == '*':
            self.function_multiply()


if __name__ == '__main__':
    app = QApplication()

    form = Form()
    form.show()
    sys.exit(app.exec_())