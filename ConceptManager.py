# -#- coding: utf-8 -#-

"""
 A manager for Concept resources 

 @author     Textalytics
 @version    1.0 -- 03/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""

import requests
from config import MANAGE_SERVICE_ENDPOINT
from Domain import Concept
from SemPubException import SemPubException

COLLECTION = "/dictionary_list/"
TYPE = "concept"
LIST = "concept_list"
ID = "id"


class ConceptManager:

  @staticmethod
  def endpoint(dictionaryName, id = None):
    if (id == None):
      return MANAGE_SERVICE_ENDPOINT + COLLECTION + dictionaryName + "/" + LIST
    else:
      return MANAGE_SERVICE_ENDPOINT + COLLECTION + dictionaryName + "/" + LIST + "/" + id

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

  def getList(self, dictionaryName, query):
    payload = {'key': self.key, 'query': query, 'src': 'sdk-python-1.0'}
    endpoint = ConceptManager.endpoint(dictionaryName)
    response = requests.get(endpoint, params = payload)
    return ConceptManager.parse(response, LIST)

  def read(self, id, dictionaryName):
    payload = {'key': self.key, 'src': 'sdk-python-1.0'} 
    endpoint = ConceptManager.endpoint(dictionaryName, id)
    response = requests.get(endpoint, params = payload)
    return ConceptManager.parse(response, TYPE)

  def create(self, concept, dictionaryName):
    payload = {'key': self.key, TYPE: str(concept), 'src': 'sdk-python-1.0' }
    endpoint = ConceptManager.endpoint(dictionaryName)
    response = requests.post(endpoint, data = payload)
    return ConceptManager.parse(response, ID)

  def update(self, concept, dictionaryName):
    payload = {'key': self.key, TYPE: str(concept), 'src': 'sdk-python-1.0' }
    endpoint = ConceptManager.endpoint(dictionaryName, concept['id'])
    response = requests.put(endpoint, data = payload)
    return ConceptManager.parse(response, ID)

  def delete(self, id, dictionaryName):
    payload = {'key': self.key, 'src': 'sdk-python-1.0'}
    endpoint = ConceptManager.endpoint(dictionaryName, id)
    response = requests.delete(endpoint, params = payload)
    return ConceptManager.parse(response, ID)
