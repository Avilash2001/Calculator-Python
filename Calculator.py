from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(800, 600)
        Calculator.setMinimumSize(QtCore.QSize(800, 600))               
        Calculator.setMaximumSize(QtCore.QSize(800, 600))
        Calculator.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        Calculator.setStyleSheet("")
        Calculator.setTabShape(QtWidgets.QTabWidget.Rounded)
        Calculator.setWindowIcon(QIcon("C:/Users/avila/Desktop/Python/Calculator/calc.png"))

        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        
        self.btEqual = QtWidgets.QPushButton(self.centralwidget)
        self.btEqual.setGeometry(QtCore.QRect(0, 500, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btEqual.setFont(font)
        self.btEqual.setStyleSheet("background-color: rgb(255, 170, 0);\n""color: rgb(255, 255, 255);")
        self.btEqual.setObjectName("btEqual")
        self.btEqual.clicked.connect(self.equal)
        
        self.btZero = QtWidgets.QPushButton(self.centralwidget)
        self.btZero.setGeometry(QtCore.QRect(200, 500, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btZero.setFont(font)
        self.btZero.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(50, 50, 50);")
        self.btZero.setObjectName("btZero")
        self.btZero.clicked.connect(self.zero)
        
        self.btDec = QtWidgets.QPushButton(self.centralwidget)
        self.btDec.setGeometry(QtCore.QRect(400, 500, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btDec.setFont(font)
        self.btDec.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(50, 50, 50);")
        self.btDec.setObjectName("btDec")
        
        self.btSub = QtWidgets.QPushButton(self.centralwidget)
        self.btSub.setGeometry(QtCore.QRect(600, 500, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btSub.setFont(font)
        self.btSub.setStyleSheet("background-color: rgb(95, 95, 95);color: rgb(255, 255, 255);")
        self.btSub.setObjectName("btSub")
        self.btSub.clicked.connect(self.sub)
        
        self.btThree = QtWidgets.QPushButton(self.centralwidget)
        self.btThree.setGeometry(QtCore.QRect(400, 400, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btThree.setFont(font)
        self.btThree.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(50, 50, 50);\n""")
        self.btThree.setObjectName("btThree")
        self.btThree.clicked.connect(self.three)
        
        self.btAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btAdd.setGeometry(QtCore.QRect(600, 400, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btAdd.setFont(font)
        self.btAdd.setStyleSheet("background-color: rgb(95, 95, 95);color: rgb(255, 255, 255);")
        self.btAdd.setObjectName("btAdd")
        self.btAdd.clicked.connect(self.add)
        
        self.btOne = QtWidgets.QPushButton(self.centralwidget)
        self.btOne.setGeometry(QtCore.QRect(0, 400, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btOne.setFont(font)
        self.btOne.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(50, 50, 50);")
        self.btOne.setObjectName("btOne")
        self.btOne.clicked.connect(self.one)
        
        self.btTwo = QtWidgets.QPushButton(self.centralwidget)
        self.btTwo.setGeometry(QtCore.QRect(200, 400, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btTwo.setFont(font)
        self.btTwo.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(50, 50, 50);\n""")
        self.btTwo.setObjectName("btTwo")
        self.btTwo.clicked.connect(self.two)
        
        self.btSix = QtWidgets.QPushButton(self.centralwidget)
        self.btSix.setGeometry(QtCore.QRect(400, 300, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btSix.setFont(font)
        self.btSix.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(50, 50, 50);")
        self.btSix.setObjectName("btSix")
        self.btSix.clicked.connect(self.six)
        
        self.btMul = QtWidgets.QPushButton(self.centralwidget)
        self.btMul.setGeometry(QtCore.QRect(600, 300, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btMul.setFont(font)
        self.btMul.setStyleSheet("background-color: rgb(95, 95, 95);color: rgb(255, 255, 255);\n""")
        self.btMul.setObjectName("btMul")
        self.btMul.clicked.connect(self.mul)

        self.btFour = QtWidgets.QPushButton(self.centralwidget)
        self.btFour.setGeometry(QtCore.QRect(0, 300, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btFour.setFont(font)
        self.btFour.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(50, 50, 50);")
        self.btFour.setObjectName("btFour")
        self.btFour.clicked.connect(self.four)
        
        self.btFive = QtWidgets.QPushButton(self.centralwidget)
        self.btFive.setGeometry(QtCore.QRect(200, 300, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btFive.setFont(font)
        self.btFive.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(50, 50, 50);")
        self.btFive.setObjectName("btFive")
        self.btFive.clicked.connect(self.five)
        
        self.btNine = QtWidgets.QPushButton(self.centralwidget)
        self.btNine.setGeometry(QtCore.QRect(400, 200, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btNine.setFont(font)
        self.btNine.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(50, 50, 50);")
        self.btNine.setObjectName("btNine")
        self.btNine.clicked.connect(self.nine)
        
        self.btDiv = QtWidgets.QPushButton(self.centralwidget)
        self.btDiv.setGeometry(QtCore.QRect(600, 200, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btDiv.setFont(font)
        self.btDiv.setStyleSheet("background-color: rgb(95, 95, 95);color: rgb(255, 255, 255);")
        self.btDiv.setObjectName("btDiv")
        self.btDiv.clicked.connect(self.div)
        
        self.btSeven = QtWidgets.QPushButton(self.centralwidget)
        self.btSeven.setGeometry(QtCore.QRect(0, 200, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btSeven.setFont(font)
        self.btSeven.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(50, 50, 50);")
        self.btSeven.setObjectName("btSeven")
        self.btSeven.clicked.connect(self.seven)
        
        self.btEight = QtWidgets.QPushButton(self.centralwidget)
        self.btEight.setGeometry(QtCore.QRect(200, 200, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btEight.setFont(font)
        self.btEight.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(50, 50, 50);")
        self.btEight.setObjectName("btEight")
        self.btEight.clicked.connect(self.eight)
        
        self.labRes = QtWidgets.QLabel(self.centralwidget)
        self.labRes.setGeometry(QtCore.QRect(0, 50, 800, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labRes.setFont(font)
        self.labRes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labRes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labRes.setObjectName("labRes")
        
        self.labHis = QtWidgets.QLabel(self.centralwidget)
        self.labHis.setGeometry(QtCore.QRect(0, 0, 800, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.labHis.setFont(font)
        self.labHis.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labHis.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.labHis.setObjectName("labHis")
        
        self.btNeg = QtWidgets.QPushButton(self.centralwidget)
        self.btNeg.setGeometry(QtCore.QRect(0, 150, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btNeg.setFont(font)
        self.btNeg.setStyleSheet("background-color: rgb(95, 95, 95);color: rgb(255, 255, 255);")
        self.btNeg.setObjectName("btNeg")
        self.btNeg.clicked.connect(self.neg)
        
        self.btSq = QtWidgets.QPushButton(self.centralwidget)
        self.btSq.setGeometry(QtCore.QRect(160, 150, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btSq.setFont(font)
        self.btSq.setStyleSheet("background-color: rgb(95, 95, 95);color: rgb(255, 255, 255);")
        self.btSq.setObjectName("btSq")
        self.btSq.clicked.connect(self.sq)
        
        self.btRoot = QtWidgets.QPushButton(self.centralwidget)
        self.btRoot.setGeometry(QtCore.QRect(320, 150, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btRoot.setFont(font)
        self.btRoot.setStyleSheet("background-color: rgb(95, 95, 95);color: rgb(255, 255, 255);")
        self.btRoot.setObjectName("btRoot")
        self.btRoot.clicked.connect(self.root)
        
        self.btCls = QtWidgets.QPushButton(self.centralwidget)
        self.btCls.setGeometry(QtCore.QRect(640, 150, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btCls.setFont(font)
        self.btCls.setStyleSheet("background-color: rgb(95, 95, 95);color: rgb(255, 255, 255);")
        self.btCls.setObjectName("btCls")
        self.btCls.clicked.connect(self.cls)
        
        self.btBksp = QtWidgets.QPushButton(self.centralwidget)
        self.btBksp.setGeometry(QtCore.QRect(480, 150, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.btBksp.setFont(font)
        self.btBksp.setStyleSheet("background-color: rgb(95, 95, 95);color: rgb(255, 255, 255);")
        self.btBksp.setObjectName("btBksp")
        self.btBksp.clicked.connect(self.bksp)

        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def one(self):
        prev = self.labRes.text()
        if prev == "0" or prev == "Cannot Divide By Zero" or prev == "Invalid Input":
                res="1"
                self.labRes.setText(res)
        else:
                res=prev+"1"
                self.labRes.setText(res)
                
    def two(self):
        prev = self.labRes.text()
        if prev == "0" or prev == "Cannot Divide By Zero" or prev == "Invalid Input":
                res="2"
                self.labRes.setText(res)
        else:
                res=prev+"2"
                self.labRes.setText(res)

    def three(self):
        prev = self.labRes.text()
        if prev == "0" or prev == "Cannot Divide By Zero" or prev == "Invalid Input":
                res="3"
                self.labRes.setText(res)
        else:
                res=prev+"3"
                self.labRes.setText(res)

    def four(self):
        prev = self.labRes.text()
        if prev == "0" or prev == "Cannot Divide By Zero" or prev == "Invalid Input":
                res="4"
                self.labRes.setText(res)
        else:
                res=prev+"4"
                self.labRes.setText(res)

    def five(self):
        prev = self.labRes.text()
        if prev == "0" or prev == "Cannot Divide By Zero" or prev == "Invalid Input":
                res="5"
                self.labRes.setText(res)
        else:
                res=prev+"5"
                self.labRes.setText(res)

    def six(self):
        prev = self.labRes.text()
        if prev == "0" or prev == "Cannot Divide By Zero" or prev == "Invalid Input":
                res="6"
                self.labRes.setText(res)
        else:
                res=prev+"6"
                self.labRes.setText(res)

    def seven(self):
        prev = self.labRes.text()
        if prev == "0" or prev == "Cannot Divide By Zero" or prev == "Invalid Input":
                res="7"
                self.labRes.setText(res)
        else:
                res=prev+"7"
                self.labRes.setText(res)

    def eight(self):
        prev = self.labRes.text()
        if prev == "0" or prev == "Cannot Divide By Zero" or prev == "Invalid Input":
                res="8"
                self.labRes.setText(res)
        else:
                res=prev+"8"
                self.labRes.setText(res)

    def nine(self):
        prev = self.labRes.text()
        if prev == "0" or prev == "Cannot Divide By Zero" or prev == "Invalid Input":
                res="9"
                self.labRes.setText(res)
        else:
                res=prev+"9"
                self.labRes.setText(res)

    def zero(self):
        prev = self.labRes.text()
        if prev == "0" or prev == "Cannot Divide By Zero" or prev == "Invalid Input":
                res="0"
                self.labRes.setText(res)
        else:
                res=prev+"0"
                self.labRes.setText(res)


    def add(self):
        prev = self.labRes.text()
        prev1= self.labHis.text()

        if prev != "0":
                calc=False
                check=list(self.labHis.text())
                flag=True
                for j in check:
                        if j == "=":
                                flag=False
                                break
                for i in check:
                        if i == "+" or i == "-" or i == "*" or i == "/":
                                calc=True
                                break
                if calc and flag:
                        res=0
                        num1=""
                        for x in check:
                                if x== " ":
                                        break
                                else:
                                        num1=num1+x
                        if is_integer(prev):
                                num2=int(prev)
                        else:
                                num2=float(prev)
                        if is_integer(num1):
                                num1=int(num1)
                        else:
                                num1=float(num1)
                        print(check[-1])
                        if check[-2] == "+":
                                res= num1+num2
                        elif check[-2] == "-":
                                res= num1-num2
                        elif check[-2] == "*":
                                res= num1*num2
                        elif check[-2] == "/":
                                if num2 == 0:
                                        self.labRes.setText("Cannot Divide By Zero")
                                        self.labHis.setText("0")
                                else:
                                        res= num1/num2
                                        if is_integer(res):
                                                res= int(res)
                                        else:
                                                res=float(num1)/float(num2)
                        res=str(res)
                        res= res+" "+"+"+" "
                        self.labRes.setText("0")
                        self.labHis.setText(res)
                
                elif not flag:
                        res = prev+" "+"+"+" "
                        self.labHis.setText(res)
                        self.labRes.setText("0")
                
                else:
                        res=prev+" "+"+"+" "
                        self.labRes.setText("0")
                        if prev1 !="0":
                                self.labHis.setText(prev1+res)
                        else:
                                self.labHis.setText(res)
        else:
                if prev1 =="0":
                        res="0 + "
                        self.labHis.setText(res)
                else:
                        check=list(self.labHis.text())
                        check.pop(-2)
                        check.insert(-1,"+")
                        new=""
                        for i in check:
                                new=new+i
                        self.labHis.setText(new)

    def sub(self):
        prev = self.labRes.text()
        prev1= self.labHis.text()
        if prev != "0":
                calc=False
                check=list(self.labHis.text())
                flag=True
                for j in check:
                        if j == "=":
                                flag=False
                                break
                for i in check:
                        if i == "+" or i == "-" or i == "*" or i == "/":
                                calc=True
                                break
                if calc and flag:
                        res=0
                        num1=""
                        for x in check:
                                if x== " ":
                                        break
                                else:
                                        num1=num1+x
                        if is_integer(prev):
                                num2=int(prev)
                        else:
                                num2=float(prev)
                        if is_integer(num1):
                                num1=int(num1)
                        else:
                                num1=float(num1)
                        print(check[-1])
                        if check[-2] == "+":
                                res= num1+num2
                        elif check[-2] == "-":
                                res= num1-num2
                        elif check[-2] == "*":
                                res= num1*num2
                        elif check[-2] == "/":
                                if num2 == 0:
                                        self.labRes.setText("Cannot Divide By Zero")
                                        self.labHis.setText("0")
                                else:
                                        res= num1/num2
                                        if is_integer(res):
                                                res= int(res)
                                        else:
                                                res=float(num1)/float(num2)
                        res=str(res)
                        res= res+" "+"-"+" "
                        self.labRes.setText("0")
                        self.labHis.setText(res)
                elif not flag:
                        res = prev+" "+"-"+" "
                        self.labHis.setText(res)
                        self.labRes.setText("0")
                else:
                        res=prev+" "+"-"+" "
                        self.labRes.setText("0")
                        if prev1 !="0":
                                self.labHis.setText(prev1+res)
                        else:
                                self.labHis.setText(res)
        else:
                if prev1 =="0":
                        res="0 - "
                        self.labHis.setText(res)
                else:
                        check=list(self.labHis.text())
                        check.pop(-2)
                        check.insert(-1,"-")
                        new=""
                        for i in check:
                                new=new+i
                        self.labHis.setText(new)

    def mul(self):
        prev = self.labRes.text()
        prev1= self.labHis.text()
        if prev != "0":
                calc=False
                check=list(self.labHis.text())
                flag=True
                for j in check:
                        if j == "=":
                                flag=False
                                break
                for i in check:
                        if i == "+" or i == "-" or i == "*" or i == "/":
                                calc=True
                                break
                if calc and flag:
                        res=0
                        num1=""
                        for x in check:
                                if x== " ":
                                        break
                                else:
                                        num1=num1+x
                        if is_integer(prev):
                                num2=int(prev)
                        else:
                                num2=float(prev)
                        if is_integer(num1):
                                num1=int(num1)
                        else:
                                num1=float(num1)
                        print(check[-1])
                        if check[-2] == "+":
                                res= num1+num2
                        elif check[-2] == "-":
                                res= num1-num2
                        elif check[-2] == "*":
                                res= num1*num2
                        elif check[-2] == "/":
                                if num2 == 0:
                                        self.labRes.setText("Cannot Divide By Zero")
                                        self.labHis.setText("0")
                                else:
                                        res= num1/num2
                                        if is_integer(res):
                                                res= int(res)
                                        else:
                                                res=float(num1)/float(num2)
                        res=str(res)
                        res= res+" "+"*"+" "
                        self.labRes.setText("0")
                        self.labHis.setText(res)
                elif not flag:
                        res = prev+" "+"*"+" "
                        self.labHis.setText(res)
                        self.labRes.setText("0")
                else:
                        res=prev+" "+"*"+" "
                        self.labRes.setText("0")
                        if prev1 !="0":
                                self.labHis.setText(prev1+res)
                        else:
                                self.labHis.setText(res)
        else:
                if prev1 =="0":
                        res="0 * "
                        self.labHis.setText(res)
                else:
                        check=list(self.labHis.text())
                        check.pop(-2)
                        check.insert(-1,"*")
                        new=""
                        for i in check:
                                new=new+i
                        self.labHis.setText(new)

    def div(self):
        prev = self.labRes.text()
        prev1= self.labHis.text()
        if prev != "0":
                calc=False
                check=list(self.labHis.text())
                flag=True
                for j in check:
                        if j == "=":
                                flag=False
                                break
                for i in check:
                        if i == "+" or i == "-" or i == "*" or i == "/":
                                calc=True
                                break
                if calc and flag:
                        res=0
                        num1=""
                        for x in check:
                                if x== " ":
                                        break
                                else:
                                        num1=num1+x
                        if is_integer(prev):
                                num2=int(prev)
                        else:
                                num2=float(prev)
                        if is_integer(num1):
                                num1=int(num1)
                        else:
                                num1=float(num1)
                        print(check[-1])
                        if check[-2] == "+":
                                res= num1+num2
                        elif check[-2] == "-":
                                res= num1-num2
                        elif check[-2] == "*":
                                res= num1*num2
                        elif check[-2] == "/":
                                if num2 == 0:
                                        self.labRes.setText("Cannot Divide By Zero")
                                        self.labHis.setText("0")
                                else:
                                        res= num1/num2
                                        if is_integer(res):
                                                res= int(res)
                                        else:
                                                res=float(num1)/float(num2)
                        res=str(res)
                        res= res+" "+"/"+" "
                        self.labRes.setText("0")
                        self.labHis.setText(res)
                elif not flag:
                        res = prev+" "+"/"+" "
                        self.labHis.setText(res)
                        self.labRes.setText("0")
                else:
                        res=prev+" "+"/"+" "
                        self.labRes.setText("0")
                        if prev1 !="0":
                                self.labHis.setText(prev1+res)
                        else:
                                self.labHis.setText(res)
        else:
                if prev1 =="0":
                        res="0 / "
                        self.labHis.setText(res)
                else:
                        check=list(self.labHis.text())
                        check.pop(-2)
                        check.insert(-1,"/")
                        new=""
                        for i in check:
                                new=new+i
                        self.labHis.setText(new)

    def cls(self):
        self.labRes.setText("0")
        self.labHis.setText("0")

    def bksp(self):
        prev=list(self.labRes.text())
        if self.labRes.text() !="0":
                prev.pop()
                new=""
                for i in prev:
                        new=new+i
                self.labRes.setText(new)
        else:
                pass
    def neg(self):
        prev=list(self.labRes.text())
        if self.labRes.text() !="0":
                if prev[0] == "-":
                        prev.pop(0)
                else:
                        prev.insert(0,"-")
                new=""
                for i in prev:
                        new=new+i
                self.labRes.setText(new)

    def sq(self):
        prev=self.labRes.text()
        if is_integer(prev):
                prev=int(prev)
        else:
                prv=float(prev)
        prev=prev*prev
        prev=str(prev)
        self.labRes.setText(prev)

    def root(self):
        prev=self.labRes.text()
        if is_integer(prev):
                prev=int(prev)
        else:
                prev=float(prev)
        if prev >= 0:
                prev=sqrt(prev)
                if is_integer(prev):
                        prev=int(prev)
                else:
                        prev=float(prev)
                prev=str(prev)
                self.labRes.setText(prev)
        else:
                self.labHis.setText("0")
                self.labRes.setText("Invalid Input")

    def equal(self):
        prev = self.labRes.text()
        prev1= self.labHis.text()
        if prev != "0" and prev1 != "0":
                check=list(self.labHis.text())
                res=0
                num1=""
                for x in check:
                        if x== " ":
                                break
                        else:
                                num1=num1+x
                if is_integer(prev):
                        num2=int(prev)
                else:
                        num2=float(prev)
                if is_integer(num1):
                        num1=int(num1)
                else:
                        num1=float(num1)
                print(check[-1])
                if check[-2] == "+":
                        res= num1+num2
                elif check[-2] == "-":
                        res= num1-num2
                elif check[-2] == "*":
                        res= num1*num2
                elif check[-2] == "/":
                        if num2 == 0:
                                self.labRes.setText("Cannot Divide By Zero")
                                self.labHis.setText("0")
                        else:
                                res= num1/num2
                                print(res)
                                if is_integer(res):
                                        res= int(res)
                                else:
                                        res=float(num1)/float(num2)
                res=str(res)
                self.labRes.setText(res)
                res= prev1+prev+" = "
                self.labHis.setText(res)
                

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Avilash Calculator"))
        self.btEqual.setText(_translate("Calculator", "="))
        self.btZero.setText(_translate("Calculator", "0"))
        self.btDec.setText(_translate("Calculator", "."))
        self.btSub.setText(_translate("Calculator", "-"))
        self.btThree.setText(_translate("Calculator", "3"))
        self.btAdd.setText(_translate("Calculator", "+"))
        self.btOne.setText(_translate("Calculator", "1"))
        self.btTwo.setText(_translate("Calculator", "2"))
        self.btSix.setText(_translate("Calculator", "6"))
        self.btMul.setText(_translate("Calculator", "*"))
        self.btFour.setText(_translate("Calculator", "4"))
        self.btFive.setText(_translate("Calculator", "5"))
        self.btNine.setText(_translate("Calculator", "9"))
        self.btDiv.setText(_translate("Calculator", "/"))
        self.btSeven.setText(_translate("Calculator", "7"))
        self.btEight.setText(_translate("Calculator", "8"))
        self.labRes.setText(_translate("Calculator", "0"))
        self.labHis.setText(_translate("Calculator", "0"))
        self.btNeg.setText(_translate("Calculator", "+/-"))
        self.btSq.setText(_translate("Calculator", "Square"))
        self.btRoot.setText(_translate("Calculator", "Sq root"))
        self.btCls.setText(_translate("Calculator", "Clear"))
        self.btBksp.setText(_translate("Calculator", "Bksp"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
