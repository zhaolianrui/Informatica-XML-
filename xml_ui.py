# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xml.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import xml.dom.minidom
import xlrd
import images_qr
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(527, 314)
        icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap(QtGui.QIcon(':/img/鲨鱼.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(QtGui.QIcon(':/img/鲨鱼.png'))
        self.open = QtWidgets.QPushButton(Form)
        self.open.setGeometry(QtCore.QRect(50, 100, 75, 23))
        icon1 = QtGui.QIcon(':/img/打开.png')
        #icon1.addPixmap(QtGui.QPixmap("打开.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open.setIcon(icon1)
        self.open.setObjectName("open")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(50, 170, 75, 23))
        icon2 = QtGui.QIcon(':/img/保存.png')
        #icon2.addPixmap(QtGui.QPixmap("保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon2)
        self.save.setObjectName("save")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 100, 321, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 170, 321, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 240, 321, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        #self.lineEdit_2.setText(os.path.join(os.path.expanduser("~"), 'Desktop'))
        self.generate = QtWidgets.QPushButton(Form)
        self.generate.setGeometry(QtCore.QRect(50, 240, 75, 23))
        icon3 = QtGui.QIcon(':/img/批量生成.png')
        #icon3.addPixmap(QtGui.QPixmap("批量生成.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.generate.setIcon(icon3)
        self.generate.setObjectName("generate")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 170, 321, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 240, 321, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(50, 40, 71, 21))
        self.label2.setLineWidth(1)
        self.label2.setTextFormat(QtCore.Qt.RichText)
        self.label2.setObjectName("label2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(140, 40, 71, 22))
        self.comboBox.setObjectName("comboBox")
        icon4 = QtGui.QIcon()
        #icon4.addPixmap(QtGui.QPixmap("xml/oracle数据库.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4 = QtGui.QIcon(':/img/oracle数据库.png')
        self.comboBox.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        #icon5.addPixmap(QtGui.QPixmap("xml/mysql数据库.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5 = QtGui.QIcon(':/img/mysql数据库.png')
        self.comboBox.addItem(icon5, "")
        self.comboBox.addItem(icon4, "")
        self.label3 = QtWidgets.QLabel(Form)
        self.label3.setGeometry(QtCore.QRect(250, 40, 101, 20))
        self.label3.setObjectName("label3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 40, 111, 20))
        self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        self.retranslateUi(Form)
        self.open.clicked.connect(self.getFileName)
        self.save.clicked.connect(self.getFileDirectory)
        self.generate.clicked.connect(self.generateXml)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.comboBox, self.lineEdit_4)
        Form.setTabOrder(self.lineEdit_4, self.open)
        Form.setTabOrder(self.open, self.save)
        Form.setTabOrder(self.save, self.generate)
        Form.setTabOrder(self.generate, self.lineEdit)
        Form.setTabOrder(self.lineEdit, self.lineEdit_2)
        Form.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        

    def getFileName(self,Form):
        self.fileName,fileType = QtWidgets.QFileDialog.getOpenFileName(None, '选取Excel文件', os.path.join(os.path.expanduser("~"), 'Desktop'),"Excel 文件(*.xlsx *.xls)")
        self.fileName = "\\".join(self.fileName.split('/'))
        self.xlmName = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\'
        self.lineEdit.setText(self.fileName)
        self.lineEdit_2.setText(self.xlmName)
        #print(self.fileName)
        
    def getFileDirectory(self):   
        pass
    def generateXml(self):
        #在内存中创建一个空的文档
        doc = xml.dom.minidom.Document() 

       #创建一个根节点Managers对象
        root = doc.createElement('PARAMETERS') 
       #设置根节点的属性
        root.setAttribute('REPOSITORY_NAME', '{0}'.format(self.lineEdit_4.text())) 
        root.setAttribute('REPOSITORY_VERSION', '186') 
        root.setAttribute('REPOSITORY_CODEPAGE', 'MS936') 
        root.setAttribute('REPOSITORY_DATABASETYPE', 'Oracle')
       #将根节点添加到文档对象中
        doc.appendChild(root) 

        book = xlrd.open_workbook(self.fileName)
        #print("表单数量:", book.nsheets)
        #print("表单名称:", book.sheet_names())
        #获取第1个表单
        sh = book.sheet_by_index(0)
        #print(u"表单 %s 共 %d 行 %d 列" % (sh.name, sh.nrows, sh.ncols))
        tableSuccess=[]
        nameFormat = "M_{0:04}_{1}_{2}"
        for i in range(book.nsheets):
            tableNameList = []
            sh = book.sheet_by_index(i)
            sheet_name = book.sheet_names()[i]
            if (sheet_name.startswith("Sheet")):
                continue

            for nrows in range(sh.nrows):
                tableName = sh.cell_value(nrows, 0)
                if self.comboBox.currentText()=="M2G":
                    targetName = tableName.lower()
                    sourceName = tableName.lower()
                else:
                    targetName = tableName.lower()
                    sourceName = tableName.upper()
                if(tableName not in tableNameList):
                    tableNameList.append(tableName)
                    nodeManager = doc.createElement('MAPPING')
                    nodeManager.setAttribute('NAME' , nameFormat.format(len(tableNameList), tableName.upper(), self.comboBox.currentText().upper()))
                    nodeManager.setAttribute('FOLDER_NAME' , sheet_name)
                    nodeManager.setAttribute('DESCRIPTION' , nameFormat.format(len(tableNameList), tableName.upper(), self.comboBox.currentText().upper()))

                    """if(self.lineEdit_5.text().upper() == "M2G"):
                        node = doc.createElement('PARAM')
                        node.setAttribute('NAME' , '$var$')
                        node.setAttribute('VALUE' , '$$temp1')
                        nodeManager.appendChild(node)"""
                    
                    node = doc.createElement('PARAM')
                    node.setAttribute('NAME' , '$Target$')
                    node.setAttribute('VALUE' , targetName)
                    nodeManager.appendChild(node)

                    node = doc.createElement('PARAM')
                    node.setAttribute('NAME' , '$Source$')
                    node.setAttribute('VALUE' , sourceName)
                    nodeManager.appendChild(node)
                    root.appendChild(nodeManager)

            a = doc.toprettyxml(encoding="UTF-8").decode()
            b = '<!DOCTYPE PARAMETERS SYSTEM "parameters.dtd">\n'
            c = a[0:39] + b + a[39:]

            #开始写xml文档
            fp = open(self.xlmName + sheet_name + ".xml", 'w')
            fp.write(c)
            fp.close()
            #self.lineEdit_3.setText("成功生成{0}文件".format(self.xlmName + sheet_name + ".xml"))
            tableSuccess.append(sheet_name + ".xml")
        self.lineEdit_3.setText("成功生成{0}文件,请在桌面查看!!!".format(",".join(tableSuccess)))
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Informatica XML配置文件生成工具V2.0版"))
        Form.setToolTip(_translate("Form", "如有使用问题请@赵连睿18663771449"))
        self.open.setToolTip(_translate("Form", "打开指定的Excel文件"))
        self.open.setText(_translate("Form", "打开文件"))
        self.save.setToolTip(_translate("Form", "请选择保存目录"))
        self.save.setText(_translate("Form", "保存目录"))
        self.generate.setToolTip(_translate("Form", "点击即可批量生成xml文件"))
        self.generate.setText(_translate("Form", "批量生成"))
        self.label2.setText(_translate("Form", "DESCRIPTION:"))
        self.label2.setToolTip(_translate("Form", "指定源端和目标端数据库类型,M代表MySQL,O代表Oracle,G代表GBase"))
        self.comboBox.setItemText(0, _translate("Form", "O2M"))
        self.comboBox.setItemText(1, _translate("Form", "M2G"))
        self.comboBox.setItemText(2, _translate("Form", "O2G"))
        self.comboBox.setToolTip(_translate("Form", "指定源端和目标端数据库类型,M代表MySQL,O代表Oracle,G代表GBase"))
        self.lineEdit.setToolTip(_translate("Form", "默认的打开路径是在桌面"))
        self.lineEdit_2.setToolTip(_translate("Form", "生成的XML文件默认放在桌面下"))
        self.label3.setText(_translate("Form", "REPOSITORY_NAME:"))
        self.lineEdit_4.setToolTip(_translate("Form", "指定Informatica存储库名称,默认为rep"))
        self.lineEdit_4.setText(_translate("Form", "rep"))

