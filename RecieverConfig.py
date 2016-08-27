from __future__ import print_function
import ConfigParser

DEFAULT_SETTING = {
	 "host": "127.0.0.1"
	,"port": "41111"
}

FILE_NAME			 = "config.ini"
SECTION_SETTINGS	 = "Settings"
SETTINGS_KEY_HOST	 = "host"
SETTINGS_KEY_PORT	 = "port"
SECTION_MAIL		 = "Mail"
MAIL_KEY_ADDRESS	 = "address"
MAIL_KEY_SUBJECT	 = "subject"
MAIL_KEY_SMTP		 = "smtp"
MAIL_KEY_PORT		 = "port"
MAIL_KEY_ACCOUNT	 = "account"
MAIL_KEY_PASSWORD	 = "password"

class RecieverConfig:
	
	def __init__(self):
		self.host		 = ""
		self.port		 = ""
		self.mailAddr	 = ""
		self.subject	 = ""
		self.smtp		 = ""
		self.smptPort	 = ""
		self.account	 = ""
		self.password	 = ""
		
	
	def readConfig(self):
		config = ConfigParser.SafeConfigParser(DEFAULT_SETTING)
		config.read(FILE_NAME)
		
		self.host		 = config.get(SECTION_SETTINGS, SETTINGS_KEY_HOST)
		self.port		 = config.getint(SECTION_SETTINGS, SETTINGS_KEY_PORT)
		
		self.mailAddr	 = config.get(SECTION_MAIL, MAIL_KEY_ADDRESS)
		self.subject	 = config.get(SECTION_MAIL, MAIL_KEY_SUBJECT)
		self.smtp		 = config.get(SECTION_MAIL, MAIL_KEY_SMTP)
		self.smptPort	 = config.get(SECTION_MAIL, MAIL_KEY_PORT)
		self.account	 = config.get(SECTION_MAIL, MAIL_KEY_ACCOUNT)
		self.password	 = config.get(SECTION_MAIL, MAIL_KEY_PASSWORD)
		
	
	def getConfigHost(self):
		return self.host
	
	def getConfigPort(self):
		return self.port
	
	def getConfigMailAddr(self):
		return self.mailAddr
	
	def getConfigSubject(self):
		return self.subject
	
	def getConfigSmtp(self):
		return self.smtp
	
	def getConfigSmptPort(self):
		return self.smptPort
	
	def getConfigAccount(self):
		return self.account
	
	def getConfigPassword(self):
		return self.password
	




