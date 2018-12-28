from accelerator import Ui_Accelerator
import os,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
import readCFile
class query_window(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Accelerator()
        self.filename=""
        self.operator="Reduction"
        self.thread=2
        self.row=""
        self.op=0
        self.ui.setupUi(self)
        self.ui.radioButton.setChecked(True)
        self.ui.radioButton.toggled.connect(lambda :self.btnstate(self.ui.radioButton))
        self.ui.radioButton_2.toggled.connect(lambda: self.btnstate(self.ui.radioButton_2))
        self.ui.radioButton_3.toggled.connect(lambda: self.btnstate(self.ui.radioButton_3))
        self.ui.pushButton.clicked.connect(self.selectFile)
        self.ui.plainTextEdit.setReadOnly(True)
        self.ui.spinBox.valueChanged.connect(self.getQspinbox)
        self.ui.pushButton_3.clicked.connect(self.DrawPic)
        self.ui.textEdit.textChanged.connect(self.getText)
        self.ui.pushButton_2.clicked.connect(self.function1)
    def selectFile(self):
        filename = QFileDialog.getOpenFileName(self, "open file dialog", "C:\\Users\\likai\\Desktop",
                                                "C files(*.c);;All Files (*)")

        self.filename=filename
        name=str(filename[0]).split("\\")
        self.Print(filename=name[len(name)-1])
    def Print(self,filename):
        if filename.endswith(".c"):
            self.ui.plainTextEdit.appendPlainText("选择文件为" + filename)
        else:
            self.ui.plainTextEdit.appendPlainText('文件读入格式错误')
        self.ui.plainTextEdit.show()
    def btnstate(self, btn):
        if btn.text() == 'Reduction':
            if btn.isChecked() == True:
                self.operator=btn.text()
                self.ui.plainTextEdit.appendPlainText("选择Openmp操作："+self.operator)
                self.ui.plainTextEdit.show()
                self.op = int(0)
                print(self.operator)

        if btn.text() == "Critical":
            if btn.isChecked() == True:
                self.operator=btn.text()
                self.ui.plainTextEdit.appendPlainText("选择Openmp操作：" + self.operator)
                self.ui.plainTextEdit.show()
                self.op = int(1)
                print(self.operator)


        if btn.text() == "Automatic":
            if btn.isChecked() ==True:
                self.operator=btn.text()
                self.ui.plainTextEdit.appendPlainText("选择Openmp操作：" + self.operator)
                self.ui.plainTextEdit.show()
                self.op = int(2)
                print(self.operator)

    def getQspinbox(self,value):
        self.thread=self.ui.spinBox.value()
        self.ui.plainTextEdit.appendPlainText("选择线程数：" + str(self.thread))
        self.ui.plainTextEdit.show()


    def getText(self):
        self.row=self.ui.textEdit.toPlainText()
        self.ui.plainTextEdit.appendPlainText("选择需要并行的行数："+str(self.row))
        self.ui.plainTextEdit.show()

    def function1(self):
        self.ui.plainTextEdit.appendPlainText("开始加速。。。。。")
        self.ui.plainTextEdit.show()
        rows=[int(i) for i in self.row.split(',')]
        operators=[int(self.op)]
        filename=str(self.filename[0])
        print(self.thread)
        readCFile.WEN(filename,rows,operators,self.thread)
        file=open("time"+str(self.thread)+".txt",'r')
        index=1
        self.ui.plainTextEdit.appendPlainText("实验结果即将呈现出。。。。。。")
        self.ui.plainTextEdit.show()
        for i in file.readlines():
            self.ui.plainTextEdit.appendPlainText("第"+ str(index)+"次实验结果："+ str(str(i).split("\n")[0])+" ms")
            self.ui.plainTextEdit.show()
            index+=1


    def DrawPic(self):
        print(os.getcwd())
        filepath=[]
        threads=[]
        for root,dirs,files in os.walk(os.getcwd()):
            for name in files:
                if name.endswith(".txt"):
                    filepath.append(os.path.join(root,name))
                    s=name.split(".")
                    thread=s[0][-1]
                    threads.append(thread)


        result=[]
        for index in filepath:
            file = open(index,'r')
            print(index)
            sum=0
            for line in file.readlines():
                print(line.split("\n"))
                sum+=float(str(line.replace("\n","")))
            average = sum/10
            result.append(average)



        # 设置画布大小
        plt.figure(figsize=(8, 8))

        # 标题
        plt.title(str(self.operator)+" "+"Parallel operation")

        # 数据
        plt.plot(threads, result, label='weight changes', linewidth=1, color='r', marker='o',
                 markerfacecolor='blue', markersize=2)

        # 横坐标描述
        plt.xlabel('threads/n')

        # 纵坐标描述
        plt.ylabel('time/ms')



        plt.legend(["Time Line"])
        plt.show()




if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=query_window()
    window.show()
    sys.exit(app.exec_())

