from PyQt5 import uic, QtCore

def __init__(self):
        QtCore.QWidget.__init__(self)
        super().__init__()
        self.ui.setupUi(self)
        window = uic.loadUi("source_files/rn_gui_v0.7.ui")
        window.show()