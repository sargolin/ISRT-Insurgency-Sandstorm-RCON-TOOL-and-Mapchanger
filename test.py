from PyQt5 import QtWidgets
import sys

class TajirMWindow(QtWidgets.QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Tajir/Home")
        self.resize(800, 400)
        self.centralWidget = QtWidgets.QLabel("Hello, World")
        # self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        # self._createActions()
        # self._connectActions()
        self._createMenuBar() #Menus
        # self._createToolBars()#tools
        


    def _createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&File")
        menuBar = menuBar.addMenu("&Outils")
        menuBar.addSeparator()
        achatMenu = menuBar.addMenu("Bying")
        stockMenu = menuBar.addMenu("Stocks")
        menuBar.addSeparator()
        helpMenu = menuBar.addMenu("&Help")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # creating main window
    mw = TajirMWindow()
    mw.show()
    sys.exit(app.exec_())     

