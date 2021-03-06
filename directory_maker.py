# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'directorymaker.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 239)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setGeometry(QtCore.QRect(260, 160, 111, 31))
        self.createButton.setObjectName("createButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 19))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 10, 471, 20))
        self.lineEdit.setToolTipDuration(-5)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 40, 471, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 71, 19))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 81, 19))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 70, 471, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 100, 31, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 130, 31, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 160, 31, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 61, 19))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 61, 19))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 160, 41, 19))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 21))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.createButton.clicked.connect(self.directory_create)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Directory Maker"))
        self.createButton.setText(_translate("MainWindow", "Create Folder"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:22px; background-color:#c0e218;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:16px; color:#0f1123;\">C:/Users/rollm/Desktop/</span></pre></body></html>"))
        self.label.setText(_translate("MainWindow", "Enter Directory"))
        self.label_2.setText(_translate("MainWindow", "Folder Name"))
        self.label_3.setText(_translate("MainWindow", "Subfolder Name"))
        self.label_4.setText(_translate("MainWindow", "Count Start"))
        self.label_5.setText(_translate("MainWindow", "Count End"))
        self.label_6.setText(_translate("MainWindow", "Interval"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

    def directory_create(self):
        try:
            directory_location = (self.lineEdit.text()) #input string location address
            directory_location = directory_location.replace('\\', '/')
            print(directory_location)
            xroot_directory = directory_location
            print(os.getcwd())
            new_root_directory = os.chdir(xroot_directory)
            print(os.getcwd())

            directory_name = (self.lineEdit_2.text()) #input string folder name
            print(directory_name)
            root = directory_name
            os.mkdir(root)
            print(os.getcwd())

            directory_subfolder_name = (self.lineEdit_3.text()) #input string sub folder name
            print(directory_subfolder_name)
            folder_name = directory_subfolder_name
            #os.mkdir(folder_name)

            start_count = (self.lineEdit_4.text()) #input integer sub folder name
            sc = int(start_count)
            print(sc)

            end_count = (self.lineEdit_5.text()) #input integer sub folder name
            ec = int(end_count)
            print(ec)

            interval_count = (self.lineEdit_6.text()) #input integer sub folder name
            ic = int(interval_count)
            print(ic)

            #a = int(input("start: "))
            #b = int(input("end: "))
            #c = int(input("interval: "))

            folders = [None]*ec

            for x in range(sc, ec, ic):
                print(str(x))
                folders[x] = folder_name +"_0" + str(x)


            for folder in folders:
                os.mkdir(os.path.join(root, folder))

            self.window = QtWidgets.QWidget()

        except ValueError:
            directory_location = (self.lineEdit.setText(""))
            self.error_messageBox1()
            print("Please enter an Directory Name!")
            directory_name = (self.lineEdit_2.setText(""))
            self.error_messageBox2()
            print("Please enter an Folder Name!")
            directory_subfolder_name = (self.lineEdit_3.setText(""))
            self.error_messageBox3()
            print("Please enter an Sub Folder Name!")

    def error_messageBox1(self):
        msg1 = QMessageBox()
        msg1.setWindowTitle("Input Error")
        msg1.setText("Please enter a Directory Name!")
        msg1.setIcon(QMessageBox.Warning)
        msg1.setStandardButtons(QMessageBox.Retry)
        x = msg1.exec_()

    def error_messageBox2(self):
        msg = QMessageBox()
        msg.setWindowTitle("Input Error")
        msg.setText("Please enter a Folder Name!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Retry)
        x = msg.exec_()

    def error_messageBox3(self):
        msg = QMessageBox()
        msg.setWindowTitle("Input Error")
        msg.setText("Please enter a SubFolder Name!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Retry)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
