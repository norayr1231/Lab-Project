import pytest
from PyQt5.QtCore import *
import TicTacToe

class TTTTest(QObject):

    def app(qtbot):
        test_app = TicTacToe.MyApp()
        qtbot.addWidget(test_app)
    
    def labelTest():
        assert app.label.text() == "X Starts"