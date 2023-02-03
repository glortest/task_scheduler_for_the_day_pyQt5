from MainWin import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    app.exec_()
