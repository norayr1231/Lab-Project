from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

#main class with methods needed
class UI(QMainWindow):
    #init method which loads UI and gets all buttons
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("TTTUI.ui", self)

        #counter for deciding whose turn is
        self.counter=0

        #all UI objects
        self.button1=self.findChild(QPushButton, "pushButton_1")
        self.button2=self.findChild(QPushButton, "pushButton_2")
        self.button3=self.findChild(QPushButton, "pushButton_3")
        self.button4=self.findChild(QPushButton, "pushButton_4")
        self.button5=self.findChild(QPushButton, "pushButton_5")
        self.button6=self.findChild(QPushButton, "pushButton_6")
        self.button7=self.findChild(QPushButton, "pushButton_7")
        self.button8=self.findChild(QPushButton, "pushButton_8")
        self.button9=self.findChild(QPushButton, "pushButton_9")
        self.start=self.findChild(QPushButton, "start")
        self.label=self.findChild(QLabel, "label")


        #all button clicks
        self.button1.clicked.connect(lambda: self.action(self.button1))
        self.button2.clicked.connect(lambda: self.action(self.button2))
        self.button3.clicked.connect(lambda: self.action(self.button3))
        self.button4.clicked.connect(lambda: self.action(self.button4))
        self.button5.clicked.connect(lambda: self.action(self.button5))
        self.button6.clicked.connect(lambda: self.action(self.button6))
        self.button7.clicked.connect(lambda: self.action(self.button7))
        self.button8.clicked.connect(lambda: self.action(self.button8))
        self.button9.clicked.connect(lambda: self.action(self.button9))
        self.start.clicked.connect(lambda: self.reset())
        

        self.button_list=[
                        self.button1,
                        self.button2,
                        self.button3,
                        self.button4,
                        self.button5,
                        self.button6,
                        self.button7,
                        self.button8,
                        self.button9,
                    ]

        #code for UI style
        self.setWindowTitle("Tic-Tac-Toe")
        self.setStyleSheet("background-color: white;")
        self.label.setText("X starts")
        self.label.setStyleSheet('QLabel {color: black;}')
        self.start.setStyleSheet('QPushButton {color: black;}')
        for b in self.button_list:
            b.setStyleSheet('QPushButton {border: none;}')
        

        self.show()

    #button triggers this method
    def action(self, btn):
        btn.setFont(QFont('Quicksliver', 36))
        if self.counter%2 == 0:
            btn.setText('X')
            btn.setStyleSheet('QPushButton {background-color: red; color: white;}')
            self.label.setText("O's Turn")
        else:
            btn.setText('O')
            btn.setStyleSheet('QPushButton {background-color: blue; color: white;}')
            self.label.setText("X's Turn")


        self.counter += 1
        btn.setEnabled(False)
        self.win()
    
    #disables all buttons after game ends
    def disableAll(self):
        for b in self.button_list:
            b.setEnabled(False)
    
    #checks if game is ending at each step
    def win(self):
        if (self.button1.text() != '' and self.button1.text() == 
            self.button4.text() == self.button7.text()):

            self.label.setText(f"{self.button1.text()} Wins")
            self.disableAll()

        elif (self.button2.text() != '' and self.button2.text() == 
            self.button5.text() == self.button8.text()):

            self.label.setText(f"{self.button2.text()} Wins")
            self.disableAll()

        elif (self.button3.text() != '' and self.button3.text() == 
            self.button6.text() == self.button9.text()):

            self.label.setText(f"{self.button3.text()} Wins")
            self.disableAll()

        elif (self.button1.text() != '' and self.button1.text() == 
            self.button2.text() == self.button3.text()):

            self.label.setText(f"{self.button1.text()} Wins")
            self.disableAll()

        elif (self.button4.text() != '' and self.button4.text() == 
            self.button5.text() == self.button6.text()):

            self.label.setText(f"{self.button4.text()} Wins")
            self.disableAll()

        elif (self.button7.text() != '' and self.button7.text() == 
            self.button8.text() == self.button9.text()):

            self.label.setText(f"{self.button7.text()} Wins")
            self.disableAll()

        elif (self.button1.text() != '' and self.button1.text() == 
            self.button5.text() == self.button9.text()):

            self.label.setText(f"{self.button1.text()} Wins")
            self.disableAll()

        elif (self.button7.text() != '' and self.button7.text() == 
            self.button5.text() == self.button3.text()):

            self.label.setText(f"{self.button7.text()} Wins")
            self.disableAll()

        elif (self.button1.text() != '' and self.button2.text() != '' and
            self.button3.text() != '' and self.button4.text() != '' and
            self.button5.text() != '' and self.button6.text() != '' and
            self.button7.text() != '' and self.button8.text() != '' and
            self.button9.text() != ''):

            self.label.setText("Draw!")

    #clears the field for starting new game
    def reset(self):
        for b in self.button_list:
            b.setText('')
            b.setEnabled(True)
            b.setStyleSheet('QPushButton {background-color: white; border: none;}')
            self.label.setText("X Starts")
            self.counter = 0


#code for app execution
app = QApplication(sys.argv)
window = UI()

app.exec_()