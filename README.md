Requirements
  pytest
  Python 3.8.*
  PyQt5 5.15.4
  pyqt5-tools 5.15.4.3.2
  
To install packages run:
  pip install PyQt5
  pip install pytest
  pip freeze to check installed packages
  
  
Make shure you are in correct directory and execute file TicTacToe.py using python TicTacToe.py

Game Description:
  Tic-tac-toe is a paper-and-pencil game for two players, X and O, who take
  turns marking the spaces in a 3×3 grid. The player who succeeds in placing
  three respective marks in a horizontal, vertical, or diagonal row wins the
  game. The following example game is won by the first player, X: Players soon
  discover that best play from both parties leads to a draw. Hence,
  Tic-tac-toe is most often played by young children.

About program:
  Program has one class [UI] which has these methods (check comments in .py file to see what they do):
                1.__init__
                2.action
                3.disableAll
                4.win
                5.reset
  Program starts by creating game field with 9 boxes and Reset button, python gets all buttons from UI and after each step played, it swithches between X and O and checks if there is a winner or it is a draw. Before game ends prompt under Reset button shows whos turn it is. When game ends prompt under Reset button shows the result and all buttons are disabled. Reset button can be used at any time to reset the game. After placing X or O that buutton is disabled untill Reset is clicked.
