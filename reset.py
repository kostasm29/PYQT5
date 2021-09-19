from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from random import randint
import psycopg2
import Login
import forgot

DB_HOST = "localhost"
DB_NAME = "demodb"
DB_USER = "postgres"
DB_PASS = "kostas"
Email_Address = 'kostantinosmavros28@gmail.com'
Email_Password = 'ibryovtatdfyjqvu'


class Ui_Reset(object):
    def setupUi(self, Email):
        self.Reset = QtWidgets.QMainWindow()
        self.Reset.setObjectName("Reset")
        self.Reset.resize(345, 370)
        self.centralwidget = QtWidgets.QWidget(self.Reset)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(36, 10, 271, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.ResetPass = QtWidgets.QLabel(self.frame_2)
        self.ResetPass.setGeometry(QtCore.QRect(40, 30, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ResetPass.setFont(font)
        self.ResetPass.setAlignment(QtCore.Qt.AlignCenter)
        self.ResetPass.setObjectName("ResetPass")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Password = QtWidgets.QLineEdit(self.frame)
        self.Password.setEnabled(True)
        self.Password.setGeometry(QtCore.QRect(20, 0, 231, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(
            self.Password.sizePolicy().hasHeightForWidth())
        self.Password.setSizePolicy(sizePolicy)
        self.Password.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("\'Open Sans\'")
        font.setPointSize(10)
        self.Password.setFont(font)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setStyleSheet("border: none;\n"
                                    "outline: none;\n"
                                    "background: none;\n"
                                    "font-family: \\\'Open Sans\\\', Helvetica, Arial, sans-serif;")
        self.Password.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Password.setObjectName("Password")
        self.Password_2 = QtWidgets.QLineEdit(self.frame)
        self.Password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_2.setEnabled(True)
        self.Password_2.setGeometry(QtCore.QRect(20, 50, 231, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(
            self.Password_2.sizePolicy().hasHeightForWidth())
        self.Password_2.setSizePolicy(sizePolicy)
        self.Password_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("\'Open Sans\'")
        font.setPointSize(10)
        self.Password_2.setFont(font)
        self.Password_2.setStyleSheet("border: none;\n"
                                      "outline: none;\n"
                                      "background: none;\n"
                                      "font-family: \\\'Open Sans\\\', Helvetica, Arial, sans-serif;")
        self.Password_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Password_2.setObjectName("Password_2")
        self.verticalLayout.addWidget(self.frame)
        self.ResetPasswordButtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.reset(Email))
        self.ResetPasswordButtton.setGeometry(QtCore.QRect(55, 240, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ResetPasswordButtton.setFont(font)
        self.ResetPasswordButtton.setStyleSheet("background-color: rgb(94, 94, 94);\n"
                                                "                                       color: white;\n"
                                                "                                       width:80%;\n"
                                                "                                        \n"
                                                "border:none;")
        self.ResetPasswordButtton.setObjectName("ResetPasswordButtton")

        self.Login = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.LoginForm())
        self.Login.setGeometry(QtCore.QRect(55, 320, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Login.setFont(font)
        self.Login.setStyleSheet("background-color: none;\n"
                                 "color: black;\n"
                                 "border: none;\n"
                                 "")
        self.Login.setObjectName("Login")

        self.Message = QtWidgets.QLabel(self.centralwidget)
        self.Message.setGeometry(QtCore.QRect(55, 285, 350, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.Message.setFont(font)
        self.Message.setObjectName("Message")
        self.Message.setStyleSheet(
            "background-color: rgb(255, 69, 69);  color: white;  padding: 10px;  width: fit-content;   border-radius: 5px;")
        self.Message.setText("")
        self.Reset.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.Reset)
        self.Reset.show()

    def LoginForm(self):
        self.Reset.close()
        self.mw = Login.Ui_MainWindow()
        self.mw.setupUi()

    def reset(self, Email):
        if not self.Password.text():
            self.Message.setText("Password can not be Empty")
        else:
            if self.Password.text() == self.Password_2.text():
                conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                                        password=DB_PASS, host=DB_HOST)
                cur = conn.cursor()
                cur.execute("""UPDATE users set password = crypt(%s,gen_salt('bf')) WHERE email = %s""",
                            (self.Password.text(), Email,))

                if cur.fetchall():
                    self.Message.setText(
                        "You have changed your password successfully!!")
                    conn.commit()
                    cur.close()
                    conn.close()
                else:
                    self.Message.setText(
                        "Something went wrong")

            else:
                self.Message.setText(
                    "Those passwords did not match. Try again.")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Reset.setWindowTitle(_translate("Reset", "Reset Password"))
        self.ResetPass.setText(_translate("Reset", "Reset Password"))
        self.Password.setPlaceholderText(_translate("Reset", "Password"))
        self.Password_2.setPlaceholderText(
            _translate("Reset", "Confirm Password"))
        self.ResetPasswordButtton.setText(
            _translate("Reset", "Reset Password"))
        self.Login.setText(
            _translate("Reset", "Log in"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Reset()
    ui.setupUi()
    sys.exit(app.exec_())
