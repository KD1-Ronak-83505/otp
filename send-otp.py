from ctypes import _NamedFuncPointer
import random
import smtplib
from re import fullmatch

SENDER_EMAIL = 'ronakpatil77777@gmail.com'
SENDER_EMAIL_PASSWD = 'fkpujgfalcvwqgbe'
OTP_LENGTH = 4
receiver = 'patilronak347@gmail.com'

# regular expression for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def generateOTP(length):
    digits = "0123456789"
    otp = random.sample(digits, length)

    return "".join(otp)


if _NamedFuncPointer == '_main_':

    print("Please Enter your Email to receive OTP")
    email = input("Email: ")

    while fullmatch(regex, email) == None:
        print("Please enter a valid email address")
        email = input("Email: ")


    OTP = generateOTP(OTP_LENGTH)
    msg = '\n\nThe One Time Password(OTP) is: ' + str(OTP)


    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login(SENDER_EMAIL, SENDER_EMAIL_PASSWD)
    s.sendmail(SENDER_EMAIL, receiver, msg)
    s.quit()


    print("OTP is sent to the given email address")
    print("Please enter the OTP to proceed")
    otp = input("OTP: ")

    if otp.strip() == otp:
        print("Given OTP was correct")
    else:
        print("Given OTP was incorrect")