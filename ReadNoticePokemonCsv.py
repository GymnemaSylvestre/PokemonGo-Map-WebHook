""" [NAME] Config of Notice Mail.

[DESCRIPTION] CSV wo parse shimasu.
"""

from __future__ import print_function
import csv


class ReadNoticePokemonCsv:
	
	def __init__(self):
		self.filename			 = "NoticePokemon.csv"
		self.dictNoticePokemon	 = {}
		self.dictPokemonName	 = {}
		
	
	def readCSV(self):
		obj = open(self.filename, "rb")
		
		reader = csv.reader(obj)
		
		for row in reader:
			self.dictNoticePokemon[row[0]] = row[2]
			self.dictPokemonName[row[0]] = row[1]
		
		#for key, value in self.dictNoticePokemon.iteritems():
		#	print(key, value)
		
	
	def isNoticePokemon(self, id):
		if self.dictNoticePokemon.get(str(id)) == "1":
			return True
		
		else:
			return False
		
	
	def getNoticePokemonName(self, id):
		return self.dictPokemonName.get(str(id)).strip()
	

__author__	= "GymnemaSylvestre"
__version__	= "1.0.0"

