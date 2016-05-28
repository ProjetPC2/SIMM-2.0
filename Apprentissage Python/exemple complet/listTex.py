from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys


class MyListView(QtWidgets.QListView):
    def ItemClicked(self, modelIndex):
        QtWidgets.QMessageBox.information(None, "Hello!", "You Clicked: \n" + modelIndex.data())


def main():
    app = QtWidgets.QApplication(sys.argv)
    listView = MyListView(None)
    model = QtCore.QStringListModel()

    model.setStringList(['Item 1', 'Item 2', 'Item 3', 'Item 4'])
    listView.setModel(model)
    listView.setWindowTitle("QListView Detect Click")
    listView.show()

    listView.clicked[QtCore.QModelIndex].connect(listView.ItemClicked)
    return app.exec_()


if __name__ == '__main__':
    main()