from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(531, 370)
        MainWindow.setMinimumSize(QtCore.QSize(531, 370))
        MainWindow.setMaximumSize(QtCore.QSize(531, 370))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setWindowTitle("Casagrande Test")
        MainWindow.setToolTip("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 70, 511, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(20, 0, 20, 0)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.b4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b4.setFont(font)
        self.b4.setAlignment(QtCore.Qt.AlignCenter)
        self.b4.setObjectName("b4")
        self.gridLayout.addWidget(self.b4, 3, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.b3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b3.setFont(font)
        self.b3.setAlignment(QtCore.Qt.AlignCenter)
        self.b3.setObjectName("b3")
        self.gridLayout.addWidget(self.b3, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)
        self.m1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.m1.setFont(font)
        self.m1.setAlignment(QtCore.Qt.AlignCenter)
        self.m1.setObjectName("m1")
        self.gridLayout.addWidget(self.m1, 0, 5, 1, 1)
        self.m4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.m4.setFont(font)
        self.m4.setAlignment(QtCore.Qt.AlignCenter)
        self.m4.setObjectName("m4")
        self.gridLayout.addWidget(self.m4, 3, 5, 1, 1)
        self.m3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.m3.setFont(font)
        self.m3.setText("")
        self.m3.setAlignment(QtCore.Qt.AlignCenter)
        self.m3.setObjectName("m3")
        self.gridLayout.addWidget(self.m3, 2, 5, 1, 1)
        self.m2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.m2.setFont(font)
        self.m2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.m2.setText("")
        self.m2.setAlignment(QtCore.Qt.AlignCenter)
        self.m2.setObjectName("m2")
        self.gridLayout.addWidget(self.m2, 1, 5, 1, 1)
        self.b1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.b1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b1.setFont(font)
        self.b1.setText("")
        self.b1.setAlignment(QtCore.Qt.AlignCenter)
        self.b1.setObjectName("b1")
        self.gridLayout.addWidget(self.b1, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.b2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b2.setFont(font)
        self.b2.setAlignment(QtCore.Qt.AlignCenter)
        self.b2.setObjectName("b2")
        self.gridLayout.addWidget(self.b2, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 310, 511, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(60, 0, 60, 0)
        self.gridLayout_2.setHorizontalSpacing(40)
        self.gridLayout_2.setVerticalSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plot = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.plot.setFont(font)
        self.plot.setCheckable(False)
        self.plot.setFlat(False)
        self.plot.setObjectName("plot")
        self.gridLayout_2.addWidget(self.plot, 0, 0, 1, 1)
        self.reset = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.reset.setFont(font)
        self.reset.setFlat(False)
        self.reset.setObjectName("reset")
        self.gridLayout_2.addWidget(self.reset, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 511, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.gridLayoutWidget_3.setFont(font)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(20, 0, 20, 0)
        self.gridLayout_3.setHorizontalSpacing(35)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 2, 1, 1)
        self.borehole = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.borehole.setText("")
        self.borehole.setAlignment(QtCore.Qt.AlignCenter)
        self.borehole.setObjectName("borehole")
        self.gridLayout_3.addWidget(self.borehole, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.sample = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.sample.setAlignment(QtCore.Qt.AlignCenter)
        self.sample.setObjectName("sample")
        self.gridLayout_3.addWidget(self.sample, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_7.setText(_translate("MainWindow", "Bumps №4"))
        self.label_8.setText(_translate("MainWindow", "Moisture"))
        self.label_3.setText(_translate("MainWindow", "Bumps №2"))
        self.label.setText(_translate("MainWindow", "Bumps №1"))
        self.label_5.setText(_translate("MainWindow", "Bumps №3"))
        self.label_6.setText(_translate("MainWindow", "Moisture"))
        self.label_4.setText(_translate("MainWindow", "Moisture"))
        self.label_2.setText(_translate("MainWindow", "Moisture"))
        self.plot.setText(_translate("MainWindow", "PLOT"))
        self.reset.setText(_translate("MainWindow", "RESET"))
        self.label_10.setText(_translate("MainWindow", "Sample"))
        self.label_9.setText(_translate("MainWindow", "Borehole"))