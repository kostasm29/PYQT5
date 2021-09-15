import SignUp2
from PyQt5 import QtCore, QtGui, QtWidgets
from psycopg2.extensions import AsIs
import psycopg2
DB_HOST = "localhost"
DB_NAME = "demodb"
DB_USER = "postgres"
DB_PASS = "kostas"


class Ui_MainWindow(object):
    def setupUi(self):

        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.resize(348, 420)

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.LoginButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.LoginUser())
        self.LoginButton.setGeometry(QtCore.QRect(60, 290, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet("background-color: rgb(90, 90, 90);\n"
                                       "                    color: white;\n"
                                       "                                        width:80%;\n"
                                       "                                        border:none;")
        self.LoginButton.setObjectName("LoginButton")

        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(70, 120, 191, 31))
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

        self.Login = QtWidgets.QLabel(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(70, 45, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Login.setFont(font)
        self.Login.setAlignment(QtCore.Qt.AlignCenter)
        self.Login.setObjectName("Login")

        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(70, 170, 191, 31))
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

        self.Account = QtWidgets.QLabel(self.centralwidget)
        self.Account.setGeometry(QtCore.QRect(70, 230, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Account.setFont(font)
        self.Account.setObjectName("Account")

        self.SignUpButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.SignUpForm())
        self.SignUpButton.setGeometry(QtCore.QRect(200, 230, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.SignUpButton.setFont(font)
        self.SignUpButton.setStyleSheet("background-color: none;\n"
                                        "color: black;\n"
                                        "border: none;")
        self.SignUpButton.setObjectName("SignUpButton")

        self.Message = QtWidgets.QLabel(self.centralwidget)
        self.Message.setGeometry(QtCore.QRect(58, 365, 300, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Message.setFont(font)
        self.Message.setStyleSheet("color:red;")
        self.Message.setText("")
        self.Message.setObjectName("Message")

        self.MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(self.MainWindow)
        self.MainWindow.show()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def SignUpForm(self):
        self.MainWindow.close()
        self.mw = SignUp2.Ui_SignUpForm()
        self.mw.setupUi()

    def LoginUser(self):
        if not self.Username.text():
            self.Message.setText("Username name can not be Empty")
        elif not self.Password.text():
            self.Message.setText("Password name can not be Empty")
        else:
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                                    password=DB_PASS, host=DB_HOST)
            cur = conn.cursor()
            # cur.execute("Create TABLE Users(ID SERIAL PRIMARY KEY, firstname TEXT, lastname TEXT);")
            # Insert values
            #cur.execute("CREATE EXTENSION pgcrypto")
            cur.execute(
                """SELECT username, password  FROM Users WHERE username = %s and password = crypt(%s,password)""", (self.Username.text(), self.Password.text(),))
            rows = cur.fetchall()
            # prepei na elegxo prota to username
            # an to rows einai adeio den tha mpei stin for
            #
            for data in rows:
                if str(data[0]) == self.Username.text():
                    print('Log in')
                    self.Message.setText("Successful  Login")
                else:
                    self.Message.setText("Wrong Username")
            if not rows:
                self.Message.setText("Wrong Password")
            else:
                self.Message.setText("Successful Login")

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    sys.exit(app.exec_())
