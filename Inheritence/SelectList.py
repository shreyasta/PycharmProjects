import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Listwidget import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.intensityWidget.itemSelectionChanged.connect(self.dispSelectedTest)
        self.ui.emotionWidget.itemSelectionChanged.connect(self.dispSelectedTest)
        self.show()
    def dispSelectedTest(self):
        self.ui.resultWidget.clear()
        items_1 = self.ui.intensityWidget.selectedItems()
        items_2 = self.ui.emotionWidget.selectedItems()
        for i in list(items_1):
            self.ui.resultWidget.addItem(i.text())

        for j in list(items_2):
            self.ui.resultWidget.addItem(j.text())


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())