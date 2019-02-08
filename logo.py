# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("profile picture.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.password_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.password_entry.setObjectName("password_entry")
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.password_entry, 3, 1, 1, 2)
        self.filename_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.filename_edit.setObjectName("filename_edit")
        self.gridLayout.addWidget(self.filename_edit, 5, 1, 1, 2)
        self.logo_number_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.logo_number_entry.setObjectName("logo_number_entry")
        self.gridLayout.addWidget(self.logo_number_entry, 4, 1, 1, 2)
        self.email_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.email_entry.setObjectName("email_entry")
        self.gridLayout.addWidget(self.email_entry, 0, 1, 1, 2)
        self.output = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.output.setFont(font)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 8, 0, 1, 3)
        self.filename_label = QtWidgets.QLabel(self.centralwidget)
        self.filename_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.filename_label.setFont(font)
        self.filename_label.setObjectName("filename_label")
        self.gridLayout.addWidget(
            self.filename_label, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.scrape_all_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setBold(True)
        font.setWeight(75)
        self.scrape_all_button.setFont(font)
        self.scrape_all_button.setObjectName("scrape_all_button")
        self.gridLayout.addWidget(self.scrape_all_button, 7, 2, 1, 1)
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.logo_label.setFont(font)
        self.logo_label.setObjectName("logo_label")
        self.gridLayout.addWidget(
            self.logo_label, 4, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(
            self.password_label, 3, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.scrape_one_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setBold(True)
        font.setWeight(75)
        self.scrape_one_button.setFont(font)
        self.scrape_one_button.setObjectName("scrape_one_button")
        self.gridLayout.addWidget(self.scrape_one_button, 7, 1, 1, 1)
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setMouseTracking(False)
        self.email_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.email_label.setAutoFillBackground(False)
        self.email_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(
            self.email_label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.gridLayout.addWidget(self.login_button, 7, 0, 1, 1)
        self.browse_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.browse_entry.setObjectName("browse_entry")
        self.browse_entry.setText(os.getcwd())
        self.gridLayout.addWidget(self.browse_entry, 6, 1, 1, 2)
        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.browse_button.setFont(font)
        self.browse_button.setObjectName("browse_button")
        self.gridLayout.addWidget(
            self.browse_button, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.email_entry, self.password_entry)
        MainWindow.setTabOrder(self.password_entry, self.logo_number_entry)
        MainWindow.setTabOrder(self.logo_number_entry, self.filename_edit)
        MainWindow.setTabOrder(self.filename_edit, self.browse_button)
        MainWindow.setTabOrder(self.browse_button, self.browse_entry)
        MainWindow.setTabOrder(self.browse_entry, self.login_button)
        MainWindow.setTabOrder(self.login_button, self.scrape_one_button)
        MainWindow.setTabOrder(self.scrape_one_button, self.scrape_all_button)
        MainWindow.setTabOrder(self.scrape_all_button, self.output)

        # Setup profile
        self.session_requests = ''

        # Setup button connect
        self.login_button.clicked.connect(self.login_action)
        self.browse_button.clicked.connect(self.select_file)
        self.scrape_one_button.clicked.connect(self.scrape_one_photo_action)
        self.scrape_all_button.clicked.connect(self.scrape_all_photos_action)

    def select_file(self):
        self.browse_entry.setText(QtWidgets.QFileDialog.getExistingDirectory())

    def login_action(self):
        email = self.email_entry.text()
        password = self.password_entry.text()
        self.session_requests = login(email, password)
        if (self.session_requests == 'Failed'):
            self.session_requests = ''
            self.output.appendPlainText('Log in failed. Please try again.\n')
        else:
            self.output.appendPlainText(
                'Log in successfully as ' + email + '\n')

    def scrape_one_photo_action(self):
        if (self.session_requests == ''):
            self.output.appendPlainText('You need to log-in first.\n')
        else:
            index = self.logo_number_entry.text()
            filename = self.filename_edit.text()
            if (index == '' or filename == ''):
                if (index == ''):
                    self.output.appendPlainText(
                        'You need to input logo number.\n')
                if (filename == ''):
                    self.output.appendPlainText(
                        'You need to input filename.\n')
            else:
                index = int(index)
                img_src = scrape_all_logos(self.session_requests)
                if index >= 1 and index <= len(img_src) + 1:
                    scrape_specific_img(
                        img_src[index - 1], self.session_requests, filename, self.browse_entry.text())
                    self.output.appendPlainText(
                        'Successfully scraping ' + filename + '\n')
                else:
                    self.output.appendPlainText(
                        'Incorrect image number, try again.\n')

    def scrape_all_photos_action(self):
        if (self.session_requests == ''):
            self.output.appendPlainText('You need to log-in first.\n')
        else:
            count = 0
            img_src = scrape_all_logos(self.session_requests)
            while count < len(img_src):
                scrape_specific_img(
                    img_src[count], self.session_requests, img_src[count][-7:-1], self.browse_entry.text())
                self.output.appendPlainText(
                    'Image ' + str(count + 1) + ' success\n')
                count += 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Mybrandnewlogo Crawler"))
        self.filename_label.setText(_translate("MainWindow", "Filename"))
        self.scrape_all_button.setText(
            _translate("MainWindow", "Scrape all photos"))
        self.logo_label.setText(_translate("MainWindow", "Logo Number"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.scrape_one_button.setText(
            _translate("MainWindow", "Scrape a photo"))
        self.email_label.setText(_translate("MainWindow", "Email"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
