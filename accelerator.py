# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accelerator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Accelerator(object):
    def setupUi(self, Accelerator):
        Accelerator.setObjectName("Accelerator")
        Accelerator.resize(381, 561)
        self.centralwidget = QtWidgets.QWidget(Accelerator)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 151, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 60, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 480, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(150, 60, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(12)
        self.spinBox.setSingleStep(2)
        self.spinBox.setProperty("value", 2)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 81, 21))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 160, 311, 291))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 120, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 110, 101, 51))
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(50, 90, 83, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 90, 81, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(230, 90, 83, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        Accelerator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Accelerator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 22))
        self.menubar.setObjectName("menubar")
        Accelerator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Accelerator)
        self.statusbar.setObjectName("statusbar")
        Accelerator.setStatusBar(self.statusbar)

        self.retranslateUi(Accelerator)
        QtCore.QMetaObject.connectSlotsByName(Accelerator)

    def retranslateUi(self, Accelerator):
        _translate = QtCore.QCoreApplication.translate
        Accelerator.setWindowTitle(_translate("Accelerator", "Accelerator"))
        self.label.setText(_translate("Accelerator", "请添加后缀为.c的串行文件"))
        self.pushButton.setText(_translate("Accelerator", "上传文件"))
        self.pushButton_2.setText(_translate("Accelerator", "加速"))
        self.pushButton_3.setText(_translate("Accelerator", "生成图像"))
        self.label_2.setText(_translate("Accelerator", "请选择线程数"))
        self.label_3.setText(_translate("Accelerator", "请输入行数"))
        self.radioButton.setText(_translate("Accelerator", "Reduction"))
        self.radioButton_2.setText(_translate("Accelerator", "Critical"))
        self.radioButton_3.setText(_translate("Accelerator", "Automatic"))

