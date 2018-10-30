PROGRAM 4
import smtplib
import getpass

myemail=input("your email id : ")
password=getpass.getpass()
recemail=input("Reciever's email id :")

#create SMTP session
s=smtplib.SMTP('smtp.gmail.com',587)

#start TLS for security
s.starttls()

#authentication
s.login(myemail,password)

#message to be sent
message="Hey bro9ther"

#sending the mail
s.sendmail(myemail,recemail,message)

#terminating the sesion
s.quit()
OUTPUT
your mail id : alapatisai10@gmail.com
password
Receiver's mail id :pramodhkprem@gmail.com
