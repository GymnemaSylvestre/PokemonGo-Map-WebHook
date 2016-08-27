from __future__ import print_function
import socket
import select

# try to import C parser then fallback in pure python parser.
try:
    from http_parser.parser import HttpParser
except ImportError:
    from http_parser.pyparser import HttpParser

#Jisaku Class
from BodyParser import BodyParser
from RecieverConfig import RecieverConfig
from ReadNoticePokemonCsv import ReadNoticePokemonCsv
from SendEmail import SendEmail

def main():
	backlog = 128
	bufsize = 8192
	
	recieverConfig = RecieverConfig()
	try:
		recieverConfig.readConfig()
		
	except  Exception as e:
		print("Error:recieverConfig.readConfig()." + str(e.message))
	
	readNoticePokemonCsv = ReadNoticePokemonCsv()
	try:
		readNoticePokemonCsv.readCSV()
		
	except  Exception as e:
		print("Error:readNoticePokemonCsv.readCSV()." + str(e.message))
	
	sendEmail = SendEmail(
		 recieverConfig.getConfigSmtp()
		,recieverConfig.getConfigSmptPort()
		,recieverConfig.getConfigAccount()
		,recieverConfig.getConfigPassword()
		,recieverConfig.getConfigMailAddr()
		,recieverConfig.getConfigSubject()
	)
	
	server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	inputs = set([server_sock])
	
	try:
		server_sock.bind((recieverConfig.getConfigHost(), int(recieverConfig.getConfigPort())))
		server_sock.listen(backlog)

		while True:
			readable, writable, exceptional = select.select(inputs, [], [])
			
			for sock in readable:
				if sock is server_sock:
					connect, address = server_sock.accept()
					inputs.add(connect)
					
				else:
					msg = sock.recv(bufsize)
					
					if len(msg) == 0:
						sock.close()
						inputs.remove(sock)
						
					else:
						recved = len(msg)
						
						#HTTP Parser
						httpParser = HttpParser()
						
						nparsed = httpParser.execute(msg, recved)
						assert nparsed == recved
						
						if httpParser.is_partial_body():
							#Json Parser
							bodyParser = BodyParser()
							bodyParser.setBody(httpParser.recv_body())
							
							if bodyParser.isPokemon():
								
								if readNoticePokemonCsv.isNoticePokemon(bodyParser.getPokemonId()):
									print("Send Mail:PokemonId=" + str(bodyParser.getPokemonId()))
									sendEmail.sendMail(
										 readNoticePokemonCsv.getNoticePokemonName(bodyParser.getPokemonId())
										,bodyParser.getLatitude()
										,bodyParser.getLongitude()
										,bodyParser.getTimeUntilHiddenMs()
									)
							
						
				
	finally:
		for sock in inputs:
			sock.close()
		
	return

if __name__ == '__main__':
	main()


