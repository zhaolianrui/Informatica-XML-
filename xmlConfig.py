from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from xml_ui import Ui_Form
app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = Ui_Form()
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())