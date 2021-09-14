from PyQt5 import QtCore, QtGui, QtWidgets
from email.message import EmailMessage
import sys
import os
import smtplib
import psycopg2
import Login
import requests

DB_HOST = "localhost"
DB_NAME = "demodb"
DB_USER = "postgres"
DB_PASS = "kostas"
Email_Address = 'kostantinosmavros28@gmail.com'
Email_Password = 'ibryovtatdfyjqvu'


msg = EmailMessage()
msg['Subject'] = 'Verification Email'
msg['From'] = Email_Address
msg.set_content('Please verify your email')


class Ui_SignUpForm(object):
    def setupUi(self):

        self.SignUpForm = QtWidgets.QMainWindow()
        self.SignUpForm.setObjectName("SignUpForm")
        self.SignUpForm.resize(362, 520)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.SignUpForm.setFont(font)
        self.SignUpForm.setFocus(True)
        self.SignUpForm.setStyleSheet("\n"
                                      "  font-family: \'Open Sans\', Helvetica, Arial, sans-serif;")
        self.SignUpForm.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(self.SignUpForm)
        self.centralwidget.setObjectName("centralwidget")
        self.SignUp = QtWidgets.QLabel(self.centralwidget)
        self.SignUp.setGeometry(QtCore.QRect(126, 20, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.SignUp.setFont(font)
        self.SignUp.setObjectName("SignUp")

        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(70, 90, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.Username.setFont(font)
        self.Username.setPlaceholderText("Username")
        self.Username.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Username.setStyleSheet("border: none;\n"
                                    "outline: none;\n"
                                    "background: none;\n"
                                    "font-family: \'Open Sans\', Helvetica, Arial, sans-serif;\n"
                                    "  text-align: center;\n"
                                    "")
        self.Username.setText("")
        self.Username.setAlignment(QtCore.Qt.AlignCenter)
        self.Username.setReadOnly(False)
        self.Username.setObjectName("Username")

        self.FirstName = QtWidgets.QLineEdit(self.centralwidget)
        self.FirstName.setGeometry(QtCore.QRect(70, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.FirstName.setFont(font)
        self.FirstName.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.FirstName.setStyleSheet("border: none;\n"
                                     "outline: none;\n"
                                     "background: none;\n"
                                     "font-family: \'Open Sans\', Helvetica, Arial, sans-serif;\n"
                                     "  text-align: center;\n"
                                     "")
        self.FirstName.setText("")
        self.FirstName.setAlignment(QtCore.Qt.AlignCenter)
        self.FirstName.setReadOnly(False)
        self.FirstName.setObjectName("FirstName")

        self.LastName = QtWidgets.QLineEdit(self.centralwidget)
        self.LastName.setGeometry(QtCore.QRect(70, 190, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.LastName.setFont(font)
        self.LastName.setStyleSheet("border: none;\n"
                                    "  outline: none;\n"
                                    "  background: none;\n"
                                    "  font-family: \'Open Sans\', Helvetica, Arial, sans-serif;")
        self.LastName.setAlignment(QtCore.Qt.AlignCenter)
        self.LastName.setObjectName("LastName")
        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(70, 240, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.Email.setFont(font)
        self.Email.setStyleSheet("border: none;\n"
                                 "  outline: none;\n"
                                 "  background: none;\n"
                                 "  font-family: \'Open Sans\', Helvetica, Arial, sans-serif;\n"
                                 "")
        self.Email.setAlignment(QtCore.Qt.AlignCenter)
        self.Email.setObjectName("Email")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(70, 290, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.Password.setFont(font)
        self.Password.setStyleSheet("border: none;\n"
                                    "  outline: none;\n"
                                    "  background: none;\n"
                                    "  font-family: \'Open Sans\', Helvetica, Arial, sans-serif;")
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setAlignment(QtCore.Qt.AlignCenter)
        self.Password.setClearButtonEnabled(False)
        self.Password.setObjectName("Password")
        self.AlreadyAmember = QtWidgets.QLabel(self.centralwidget)
        self.AlreadyAmember.setGeometry(QtCore.QRect(90, 341, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.AlreadyAmember.setFont(font)
        self.AlreadyAmember.setObjectName("AlreadyAmember")
        self.Login = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.LoginForm())
        self.Login.setGeometry(QtCore.QRect(200, 330, 71, 41))
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
        self.SignUpButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.InsertData())
        self.SignUpButton.setGeometry(QtCore.QRect(70, 390, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(13)
        self.SignUpButton.setFont(font)
        self.SignUpButton.setStyleSheet("background-color: rgb(94, 94, 94);\n"
                                        "color: white;\n"
                                        "width:80%;\n"
                                        "border:none;")
        self.SignUpButton.setObjectName("SignUpButton")

        self.Message = QtWidgets.QLabel(self.centralwidget)
        self.Message.setGeometry(QtCore.QRect(85, 440, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.Message.setFont(font)
        self.Message.setObjectName("Message")
        self.Message.setStyleSheet("color: red;\n")
        self.Message.setText("")

        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Oh no!')

        self.SignUpForm.setCentralWidget(self.centralwidget)
        self.retranslateUi(self.SignUpForm)
        self.SignUpForm.show()
        QtCore.QMetaObject.connectSlotsByName(self.SignUpForm)

    def LoginForm(self):
        self.SignUpForm.close()
        self.mw = Login.Ui_MainWindow()
        self.mw.setupUi()

    def InsertData(self):
        self.Message.setText("")
        if not self.Username.text():
            self.Message.setText("Username name can not be Empty")
        elif not self.FirstName.text():
            self.Message.setText("First name can not be Empty")
        elif not self.LastName.text():
            self.Message.setText("Last name can not be Empty")
        elif not self.Email.text():
            self.Message.setText("Email can not be Empty")
        elif '@' not in self.Email.text():
            self.Message.setText("Email must contain character @")
        elif not self.Password.text():
            self.Message.setText("Password can not be Empty")
        else:
            # connect with database
            self.Message.setText("")
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                                    password=DB_PASS, host=DB_HOST)

            cur = conn.cursor()
            # cur.execute("Create TABLE Users(ID SERIAL PRIMARY KEY, firstname TEXT, lastname TEXT);")
            # Insert values
            #cur.execute("CREATE EXTENSION pgcrypto")
            if not cur.execute("SELECT username FROM Users WHERE username = %s", (self.Username.text(),)):
                response = requests.get("https://isitarealemail.com/api/email/validate",
                                        params={'email': self.Email.text()})
                self.Message.setText("")
                if cur.fetchone():
                    self.Message.setText("Username already exists")
                elif response.json()['status'] != 'invalid' and response.json()['status'] != 'valid':
                    self.Message.setText("")
                    self.Message.setText("Email does not exist")

                else:
                    self.Message.setText("")
                    try:
                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                            smtp.login(Email_Address,
                                       Email_Password)
                            msg['To'] = str(self.Email.text())
                            smtp.send_message(msg)
                            self.Message.setText(
                                'Succesful Sign UP!\n Please verify your email.')

                            cur.execute(
                                "INSERT INTO Users (username,firstname,lastname,email,password) VALUES(%s,%s,%s,%s,crypt(%s,gen_salt('bf')))", (self.Username.text(), self.FirstName.text(), self.LastName.text(), self.Email.text(), self.Password.text()))
                            #commit and close
                            conn.commit()
                            cur.close()
                            conn.close()
                    # self.SignUpForm.close()
                    except smtplib.SMTPRecipientsRefused:
                        self.Message.setText("This email does not exist")
                    except:
                        self.Message.setText("Something went wrong")

    def retranslateUi(self, SignUpForm):
        _translate = QtCore.QCoreApplication.translate
        SignUpForm.setWindowTitle(_translate("SignUpForm", "Sign Up"))
        self.SignUp.setText(_translate("SignUpForm", "Sign Up"))
        self.FirstName.setPlaceholderText(
            _translate("SignUpForm", "First Name"))
        self.LastName.setPlaceholderText(_translate("SignUpForm", "Last Name"))
        self.Email.setPlaceholderText(_translate("SignUpForm", "Email"))
        self.Password.setPlaceholderText(_translate("SignUpForm", "Password"))
        self.AlreadyAmember.setText(_translate(
            "SignUpForm", "Already a member?"))
        self.Login.setText(_translate("SignUpForm", "Log in"))
        self.SignUpButton.setText(_translate("SignUpForm", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_SignUpForm()
    ui.setupUi()
    sys.exit(app.exec_())
