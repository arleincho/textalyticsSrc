# -#- coding: utf-8 -#-

"""
  A manager for Dictionary resources 

 @author     Textalytics
 @version    1.0 -- 03/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""

import requests
from config import MANAGE_SERVICE_ENDPOINT,KEY
from Domain import Dictionary
from SemPubException import SemPubException

TYPE = "dictionary"
LIST = TYPE + "_list"
ID = 'id'


class DictionaryManager:

	@staticmethod
	def endpoint(dictionaryName=None):
		if (dictionaryName == None):
 			return MANAGE_SERVICE_ENDPOINT + "/" + LIST
 		else:
 			return MANAGE_SERVICE_ENDPOINT + "/" + LIST + "/" + dictionaryName

 	@staticmethod
	def parse(response, element):
		if response.status_code == requests.codes.ok:
			r = response.json()
			return r[element]
		else: 
			r = response.json()
			raise SemPubException(response.status_code, r['status'])
	

	def __init__(self, key):
		self.key = key
		self.input  = "json" # JSON input and output are used
		self.output = "json"

	def getList(self, query, language):
		payload = {'key': self.key, 'query' : query, 'language' : language, 'src': 'sdk-python-1.0'}
		endpoint = DictionaryManager.endpoint()
		response = requests.get(endpoint, params = payload)
		return DictionaryManager.parse(response, LIST)

	def read(self, name):
		payload = {'key': self.key, 'src': 'sdk-python-1.0'}
		endpoint = DictionaryManager.endpoint(name)
		response = requests.get(endpoint, params = payload)
		return DictionaryManager.parse(response, TYPE)

	def create(self, dictionary):
		payload = {'key': self.key, TYPE : str(dictionary), 'src': 'sdk-python-1.0' }
		endpoint = DictionaryManager.endpoint()
		response = requests.post(endpoint, data = payload)
		return DictionaryManager.parse(response, ID)

	def update(self, dictionary):
		payload = {'key': self.key, TYPE : str(dictionary), 'src': 'sdk-python-1.0' }
		name = dictionary['name']
		endpoint = DictionaryManager.endpoint(name)
		response = requests.put(endpoint, data = payload)
		return DictionaryManager.parse(response, ID)

	def delete(self, name):
		payload = {'key': self.key, 'src': 'sdk-python-1.0'}
		endpoint = DictionaryManager.endpoint(name)
		response = requests.delete(endpoint, params = payload)
		return DictionaryManager.parse(response, ID)
