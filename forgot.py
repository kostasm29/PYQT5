from PyQt5 import QtCore, QtGui, QtWidgets
from email.message import EmailMessage
import requests
import sys
import smtplib
from random import randint
import psycopg2
import Login

DB_HOST = "localhost"
DB_NAME = "demodb"
DB_USER = "postgres"
DB_PASS = "kostas"
Email_Address = 'kostantinosmavros28@gmail.com'
Email_Password = 'ibryovtatdfyjqvu'


msg = EmailMessage()
msg['Subject'] = 'Verification Email'
msg['From'] = Email_Address


class Ui_MainWindow(object):
    def setupUi(self, Forgot_Password):
        Forgot_Password.setObjectName("Forgot_Password")
        Forgot_Password.resize(307, 338)
        self.centralwidget = QtWidgets.QWidget(Forgot_Password)
        self.centralwidget.setObjectName("centralwidget")
        self.ForgotButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.InsertData())
        self.ForgotButton.setGeometry(QtCore.QRect(74, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ForgotButton.setFont(font)
        self.ForgotButton.setStyleSheet("background-color: rgb(90, 90, 90);\n"
                                        " color: white;\n"
                                        " width:80%;\n"
                                        " border:none;")
        self.ForgotButton.setObjectName("ForgotButton")
        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(50, 49, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Email.setFont(font)
        self.Email.setStyleSheet("border: none;\n"
                                 "outline: none;\n"
                                 "background: none;\n"
                                 "text-align: center;")
        self.Email.setAlignment(QtCore.Qt.AlignCenter)
        self.Email.setObjectName("Email")
        self.Verify = QtWidgets.QLineEdit(self.centralwidget)
        self.Verify.setGeometry(QtCore.QRect(50, 230, 211, 20))
        self.Verify.setStyleSheet("border: none;\n"
                                  "outline: none;\n"
                                  "color: grey;\n"
                                  "background: #F0F0F0;\n"
                                  "font-family: \\\'Open Sans\\\', Helvetica, Arial, sans-serif;")
        self.Verify.setObjectName("Verify")
        self.Message = QtWidgets.QLabel(self.centralwidget)
        self.Message.setGeometry(QtCore.QRect(46, 170, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Message.setStyleSheet("color: red;\n width: fit-content;")
        self.Message.setFont(font)
        self.Message.setText("")
        self.Message.setObjectName("Message")
        self.Ok = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.CloseForm())
        self.Ok.setGeometry(QtCore.QRect(100, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("\'Open Sans\'")
        font.setPointSize(12)
        self.Ok.setFont(font)
        self.Ok.setStyleSheet("border: none;\n"
                              "outline: none;\n""color: grey;\n"
                              "background: #F0F0F0;\n"
                              "font-family: \\\'Open Sans\\\', Helvetica, Arial, sans-serif;")
        self.Ok.setText("")
        self.Ok.setObjectName("Ok")
        self.verification_code = randint(100_000, 999_999)
        Forgot_Password.setCentralWidget(self.centralwidget)

        self.retranslateUi(Forgot_Password)
        QtCore.QMetaObject.connectSlotsByName(Forgot_Password)

    def InsertData(self):
        self.Message.setText("")

        # check if fields are empty
        if not self.Email.text():
            self.Message.setText("Email can not be Empty")
        else:
            response = requests.get(
                "https://isitarealemail.com/api/email/validate",
                params={'email': str(self.Email.text())})
            if response.json()['status'] == "valid":
                # connect with database
                conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                                        password=DB_PASS, host=DB_HOST)
                cur = conn.cursor()

                if not cur.execute("SELECT email FROM Users WHERE email = %s", (self.Email.text(),)):
                    if not cur.fetchone():
                        self.Message.setText(
                            "This Email does not have an accont")
                    else:
                        try:
                            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                                smtp.login(Email_Address,
                                           Email_Password)
                                msg['To'] = str(self.Email.text())
                                msg.add_alternative("""\
                                <!DOCTYPE html>
                                <html>
                                    <body>
                                        <h1 style="font-size:20px">"""f'Your verification code is:  {self.verification_code}'"""</h1>
                                    </body>
                                </html>
                                """, subtype='html')
                                smtp.send_message(msg)

                                self.Message.setText(
                                    'Successful Sign up!\nPlease verify your code sent to your email.')
                                self.Verify.setStyleSheet(
                                    "  background: none;")
                                self.Ok.setStyleSheet("background-color: rgb(94, 94, 94);\n"
                                                      "color: white;\n"
                                                      "width:80%;\n"
                                                      "border:none;")
                                self.Ok.setText("Ok")

                                conn.commit()
                                cur.close()
                                conn.close()

                        except:
                            self.Message.setText(
                                "Something went wrong please try again later.")
            else:
                self.Message.setText("This email does not exist")

    def CloseForm(self):
        if self.Verify.text() == str(self.verification_code):
            self.Message.setText("Well done!\nYou can login now.")
            # self.SignUpForm.close()
        else:
            self.Message.setText("Wrong verification code.\nPlease try again.")

    def retranslateUi(self, Forgot_Password):
        _translate = QtCore.QCoreApplication.translate
        Forgot_Password.setWindowTitle(_translate(
            "Forgot_Password", "Forgot Password"))
        self.ForgotButton.setText(_translate(
            "Forgot_Password", "Forgot Password"))
        self.Email.setPlaceholderText(_translate("Forgot_Password", "Email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Forgot_Password = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Forgot_Password)
    Forgot_Password.show()
    sys.exit(app.exec_())
