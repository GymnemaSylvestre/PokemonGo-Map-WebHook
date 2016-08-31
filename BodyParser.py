""" [NAME] Perse of JSON(PokemonGo-Map WebHook).

[DESCRIPTION] JSON wo parse shimasu.
"""
__author__	= "GymnemaSylvestre"
__version__	= "1.0.0"

from __future__ import print_function
import json

class BodyParser:
	
	def __init__(self):
		self.body					 = []
		self.message				 = []
		self.type					 = ""
		self.time_until_hidden_ms	 = ""
		self.last_modified_time		 = ""
		self.disappear_time			 = ""
		self.pokemon_id				 = ""
		self.latitude				 = ""
		self.spawnpoint_id			 = ""
		self.encounter_id			 = ""
		self.longitude				 = ""
	
	def setBody(self, body):
		self.body = json.loads(body)
		
		bodyKeys = self.body.keys()
		
		for key in bodyKeys:
			
			if key == "message":
				self.message = json.loads(json.dumps(self.body[key]))
				
			
			elif key == "type":
				self.type = self.body[key]
			
		
		messageKeys = self.message.keys()
		
		for key in messageKeys:
			if key == "time_until_hidden_ms":
				self.time_until_hidden_ms = self.message[key]
			
			elif key == "last_modified_time":
				self.last_modified_time = self.message[key]
			
			elif key == "disappear_time":
				self.disappear_time = self.message[key]
			
			elif key == "pokemon_id":
				self.pokemon_id = self.message[key]
			
			elif key == "latitude":
				self.latitude = self.message[key]
			
			elif key == "spawnpoint_id":
				self.spawnpoint_id = self.message[key]
			
			elif key == "encounter_id":
				self.encounter_id = self.message[key]
			
			elif key == "longitude":
				self.longitude = self.message[key]
			
		
	
	def getType(self):
		return self.type
	
	def getTimeUntilHiddenMs(self):
		return self.time_until_hidden_ms
	
	def getLastModifiedTime(self):
		return self.last_modified_time
	
	def getDisappearTime(self):
		return self.disappear_time
	
	def getPokemonId(self):
		return self.pokemon_id
	
	def getLatitude(self):
		return self.latitude
	
	def getSpawnpointId(self):
		return self.spawnpoint_id
	
	def getEncounterId(self):
		return self.encounter_id
	
	def getLongitude(self):
		return self.longitude
	
	def isPokemon(self):
		if self.getType() == "pokemon":
			return True
		
		else:
			return False
	

