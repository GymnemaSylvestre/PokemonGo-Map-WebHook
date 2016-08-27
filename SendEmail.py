from __future__ import print_function
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

SUBTYPE	 = "plain"
SUBJECT	 = "Subject"
FROM	 = "From"
TO		 = "To"
DATE	 = "Date"

GMAP	 = "http://maps.google.com/maps?q="

class SendEmail:
	
	def __init__(self, smtp, port, account, password, emailAddr, subject):
		self.smtp		 = smtp
		self.port		 = int(port)
		self.account	 = account
		self.password	 = password
		self.toAddr		 = emailAddr
		self.fromAddr	 = emailAddr
		self.charset	 = "UTF-8"
		self.subject	 = subject
		
	
	def sendMail(self, name, latitude, longitude, time_until_hidden_ms):
		intTime = int(time_until_hidden_ms)
		temp = intTime / 1000
		minute = int(temp / 60)
		second = int(temp - (minute * 60))
		
		body = name + "(" + str(minute) + "m" +str(second) + "s) " + GMAP + str(latitude) + "," + str(longitude)
		subject = name + " - " + self.subject
		
		msg = MIMEText(body, SUBTYPE, self.charset)
		msg[SUBJECT] = Header(subject, self.charset)
		msg[FROM]	 = self.fromAddr
		msg[TO]		 = self.toAddr
		msg[DATE]	 = formatdate(localtime = True)
		
		#TLS
		smtp = smtplib.SMTP(self.smtp.strip(), self.port)
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(self.account, self.password)
		smtp.sendmail(self.fromAddr, self.toAddr, msg.as_string())
		smtp.quit()
		
	




