# from logWin import LoginWin
from mWin import MainWin
from PyQt6.QtWidgets import QApplication
import sys

def main() -> int:
    app = QApplication(sys.argv)
    mainWin = MainWin()
    mainWin.show()
    return app.exec()

if __name__ == '__main__':
    main()