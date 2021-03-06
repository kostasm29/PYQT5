import SignUp2
from PyQt5 import QtCore, QtGui, QtWidgets
from psycopg2.extensions import AsIs
import psycopg2
import forgot
DB_HOST = "localhost"
DB_NAME = "demodb"
DB_USER = "postgres"
DB_PASS = "kostas"


class Ui_MainWindow(object):
    def setupUi(self):
        # main Window
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.resize(348, 450)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Login Button
        self.LoginButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.LoginUser())
        self.LoginButton.setGeometry(QtCore.QRect(60, 275, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet("background-color: rgb(90, 90, 90);\n"
                                       "                    color: white;\n"
                                       "                                        width:80%;\n"
                                       "                                        border:none;")
        self.LoginButton.setObjectName("LoginButton")

        # User name unput
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(70, 130, 191, 31))
        font = QtGui.QFont()
        font.setFamily("\'Open Sans\'")
        font.setPointSize(10)
        self.Username.setFont(font)
        self.Username.setStyleSheet("border: none;\n""outline: none;\n"
                                    "background: none;\n"
                                    "font-family: \\\'Open Sans\\\', Helvetica, Arial, sans-serif;\n"
                                    "text-align: center;")
        self.Username.setText("")
        self.Username.setAlignment(QtCore.Qt.AlignCenter)
        self.Username.setObjectName("Username")

        # Login Label
        self.Login = QtWidgets.QLabel(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(70, 55, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Login.setFont(font)
        self.Login.setAlignment(QtCore.Qt.AlignCenter)
        self.Login.setObjectName("Login")

        # Password input
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(70, 180, 191, 31))
        font = QtGui.QFont()
        font.setFamily("\'Open Sans\'")
        font.setPointSize(10)
        self.Password.setFont(font)
        self.Password.setStyleSheet("border: none;\n"
                                    "outline: none;\n"
                                    "background: none;\n"
                                    "font-family: \\\'Open Sans\\\', Helvetica, Arial, sans-serif;\n"
                                    "text-align: center;")
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setAlignment(QtCore.Qt.AlignCenter)
        self.Password.setObjectName("Password")

        # Forgot button
        self.ForgotButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.Forgot())
        self.ForgotButton.setGeometry(QtCore.QRect(100, 230, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ForgotButton.setFont(font)
        self.ForgotButton.setStyleSheet("background-color: none;\n"
                                        "color: black;\n"
                                        "border: none;")
        self.ForgotButton.setObjectName("ForgotButton")

        # Already an account Lable
        self.Account = QtWidgets.QLabel(self.centralwidget)
        self.Account.setGeometry(QtCore.QRect(70, 420, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Account.setFont(font)
        self.Account.setObjectName("Account")

        # Sign Up button
        self.SignUpButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.SignUpForm())
        self.SignUpButton.setGeometry(QtCore.QRect(200, 420, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.SignUpButton.setFont(font)
        self.SignUpButton.setStyleSheet("background-color: none;\n"
                                        "color: black;\n"
                                        "border: none;")
        self.SignUpButton.setObjectName("SignUpButton")

        # Message Label
        self.Message = QtWidgets.QLabel(self.centralwidget)
        self.Message.setGeometry(QtCore.QRect(57, 340, 250, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Message.setFont(font)
        self.Message.setText("")
        self.Message.setObjectName("Message")
        self.Message.setWordWrap(True)

        self.MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(self.MainWindow)
        self.MainWindow.show()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def SignUpForm(self):
        self.MainWindow.close()
        self.mw = SignUp2.Ui_SignUpForm()
        self.mw.setupUi()

    def Forgot(self):
        self.MainWindow.close()
        self.mw = forgot.Ui_MainWindow()
        self.mw.setupUi()

    def LoginUser(self):
        if not self.Username.text():
            self.Message.setText(
                "Username name can not be Empty sfasfasfasfasfasfasfasfasfsas")
            self.Message.setStyleSheet(
                "background-color: rgb(255, 69, 69);  padding:5px; color: white;  height:fit-content; width: fit-content;   border-radius: 5px;")
        elif not self.Password.text():
            self.Message.setText("Password name can not be Empty")
            self.Message.setStyleSheet(
                "background-color: rgb(255, 69, 69);  color: white;  width: fit-content;   border-radius: 5px;")
        else:
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                                    password=DB_PASS, host=DB_HOST)
            cur = conn.cursor()
            # Insert values
            # na elegxo mono toy to username giati
            # kai ta dio mazi den ginetai na ksexoriso poio einai lathos
            cur.execute(
                """SELECT username  FROM Users WHERE username = %s """, (self.Username.text(),))
            rows = cur.fetchall()
            if not rows:
                self.Message.setText("Wrong Username")
                self.Message.setStyleSheet(
                    "background-color: rgb(255, 69, 69);  color: white;  width: fit-content;   border-radius: 5px;")
            else:
                cur.execute(
                    """SELECT username, password  FROM Users WHERE username = %s and password = crypt(%s,password)""", (self.Username.text(), self.Password.text(),))
                rows = cur.fetchall()
                if rows:
                    self.Message.setText("Successful Login")
                    self.Message.setStyleSheet(
                        "background-color: #74f174;  color: white;  font-weight:800; width: fit-content;   border-radius: 5px;")
                else:
                    self.Message.setText("Wrong Password")
                    self.Message.setStyleSheet(
                        "background-color: rgb(255, 69, 69);  color: white;  width: fit-content;   border-radius: 5px;")

            cur.close()
            conn.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoginButton.setText(_translate("MainWindow", "Login"))
        self.Username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.Login.setText(_translate("MainWindow", "Login"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.Account.setText(_translate(
            "MainWindow", "Don\'t have an account?"))
        self.SignUpButton.setText(_translate("MainWindow", "Sign Up"))
        self.ForgotButton.setText(_translate("MainWindow", "Forgot Password?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    sys.exit(app.exec_())
