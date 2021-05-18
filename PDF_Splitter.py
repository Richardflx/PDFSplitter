from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyPDF2 import PdfFileReader, PdfFileWriter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 442)
        MainWindow.setMinimumSize(QtCore.QSize(422, 442))
        MainWindow.setMaximumSize(QtCore.QSize(422, 442))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 40, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 49, 251, 21))
        self.lineEdit.setObjectName("lineEdit")
        
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(10, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(210, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(310, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.txtArea = QtWidgets.QTextEdit(self.centralwidget)
        self.txtArea.setGeometry(QtCore.QRect(10, 210, 401, 201))
        self.txtArea.setObjectName("listView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menuBar.setObjectName("menuBar")
        
        self.menuAjuda = QtWidgets.QMenu(self.menuBar)
        self.menuAjuda.setObjectName("menuAjuda")
        MainWindow.setMenuBar(self.menuBar)
        
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        
        self.actionSobre_2 = QtWidgets.QAction(MainWindow)
        self.actionSobre_2.setObjectName("actionSobre_2")
        
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        
        self.menuAjuda.addAction(self.actionSobre)
        self.menuAjuda.addAction(self.actionSobre_2)
        self.menuAjuda.addAction(self.actionSair)
        self.menuBar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.GetDir)
        self.pushButton_2.clicked.connect(self.num_pages)
        
        self.actionSobre.triggered.connect(self.menu_ajuda)
        self.actionSobre_2.triggered.connect(self.menu_sobre)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF Splitter"))
        self.pushButton.setText(_translate("MainWindow", "Buscar"))
        self.radioButton.setText(_translate("MainWindow", "1 Página"))
        self.radioButton_2.setText(_translate("MainWindow", "2 Páginas"))
        self.radioButton_3.setText(_translate("MainWindow", "3 Páginas"))
        self.radioButton_4.setText(_translate("MainWindow", "4 Páginas"))
        self.label.setText(_translate("MainWindow", "Selecionar arquivo:"))
        self.label_2.setText(_translate("MainWindow", "Arquivos gerados:"))
        self.pushButton_2.setText(_translate("MainWindow", "Dividir!"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Arquivo"))
        self.actionSobre.setText(_translate("MainWindow", "Ajuda"))
        self.actionSobre_2.setText(_translate("MainWindow", "Sobre"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))

    def menu_ajuda(self):
        self.txtArea.clear()
        self.txtArea.insertPlainText('Selecione o arquivo que deseja dividir e o numero de páginas por arquivo\r')

    def menu_sobre(self):
        self.txtArea.clear()
        self.txtArea.insertPlainText('PDF SPLITTER\rv1.3\rDesenvolvido por Richard Félix Rosa :)\r')

    def GetDir(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                    None,
                    "Selecionar arquivo:",
                    "",
                    "Arquivos PDF (*.pdf);; Todos os arquivos (*)",
                    options=options)
        if fileName:
            self.lineEdit.setText(fileName)

    def pdf_splitter(self):
            path = self.lineEdit.text()
            fname = os.path.splitext(os.path.basename(path))[0]
            try:
                pdf = PdfFileReader(path)
                self.textArea.clear()
                for page in range(pdf.getNumPages()):
                    pdf_writer = PdfFileWriter()
                    pdf_writer.addPage(pdf.getPage(page))

                    output_filename = '_page_{}.pdf'.format(page+1)
                    with open(path.replace('.pdf','') + output_filename, 'wb') as out:
                        pdf_writer.write(out)


                        self.txtArea.insertPlainText('Criado: {}{}'.format(output_filename, '\r'))
            except:
                self.txtArea.clear()
                self.txtArea.insertPlainText('Selecione um arquivo\r')        

    def pdf_splitter_2_pages(self):
        path = self.lineEdit.text()
        try:
            pdf = PdfFileReader(path)
            page = 0
            self.textArea.clear()
            while page < pdf.getNumPages():
                pdf_writer = PdfFileWriter()

                if page % 2 == 0:
                    pdf_writer.addPage(pdf.getPage(page))
                    pdf_writer.addPage(pdf.getPage(page+1))

                    output_filename = '_page_{}-{}.pdf'.format(page+1, page+2)
                    with open(path.replace('.pdf', '') + output_filename, 'wb') as out:
                        pdf_writer.write(out)

                    self.txtArea.insertPlainText
                    (f'Criado: {output_filename}\r')

                    page = page + 1

                else:
                    page = page + 1
                    continue
        except:
            self.txtArea.clear()
            self.txtArea.insertPlainText('Selecione um arquivo\r')         

    def pdf_splitter_3_pages(self):
        path = self.lineEdit.text()
        fname = os.path.splitext(os.path.basename(path))[0]
        try:
            pdf = PdfFileReader(path)
            page = 0
            self.textArea.clear()
            while page < pdf.getNumPages():
                pdf_writer = PdfFileWriter()

                if page % 3 == 0:
                    pdf_writer.addPage(pdf.getPage(page))
                    pdf_writer.addPage(pdf.getPage(page+1))
                    pdf_writer.addPage(pdf.getPage(page+2))

                    output_filename = '_page_{}-{}.pdf'.format(page+1,page+3)
                    with open(path.replace('.pdf','') + output_filename, 'wb') as out:
                        pdf_writer.write(out)

                    self.txtArea.insertPlainText('Criado: {}{}'.format(output_filename, '\r'))

                    page = page + 3

                else:
                    page = page + 3
                    continue
        except:
            self.txtArea.clear()
            self.txtArea.insertPlainText('Selecione um arquivo\r')

    def pdf_splitter_4_pages(self):
        path = self.lineEdit.text()
        fname = os.path.splitext(os.path.basename(path))[0]
        try:
            pdf = PdfFileReader(path)
            page = 0
            self.textArea.clear()
            while page < pdf.getNumPages():
                pdf_writer = PdfFileWriter()

                if page % 4 == 0:
                    pdf_writer.addPage(pdf.getPage(page))
                    pdf_writer.addPage(pdf.getPage(page+1))
                    pdf_writer.addPage(pdf.getPage(page+2))
                    pdf_writer.addPage(pdf.getPage(page+3))

                    output_filename = '_page_{}-{}.pdf'.format(page+1,page+4)
                    with open(path.replace('.pdf','') + output_filename, 'wb') as out:
                        pdf_writer.write(out)

                    self.txtArea.insertPlainText('Criado: {}{}'.format(output_filename, '\r'))

                    page = page + 4

                else:
                    page = page + 4
                    continue
        except:
            self.txtArea.clear()
            self.txtArea.insertPlainText('Selecione um arquivo\r')

    def num_pages(self):
            if self.radioButton.isChecked():
                print('1 pg')
                self.pdf_splitter()
                
            elif self.radioButton_2.isChecked():
                print('2 pgs')
                self.pdf_splitter_2_pages()
                
            elif self.radioButton_3.isChecked():
                print('3 pgs')
                self.pdf_splitter_3_pages()
                
            elif self.radioButton_4.isChecked():
                print('4 pgs')
                self.pdf_splitter_4_pages()
                
            else:
                self.txtArea.setPlainText('Defina o intervalo de páginas!')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
