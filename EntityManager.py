# -#- coding: utf-8 -#-

"""
  A manager for Entity resources 

 @author     Textalytics
 @version    1.0 -- 03/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""

import requests
from config import MANAGE_SERVICE_ENDPOINT
from Domain import Entity
from SemPubException import SemPubException

COLLECTION = "/dictionary_list/"
TYPE = "entity"
LIST = "entity_list"
ID = "id"

class EntityManager:
  
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
    self.input = "json" # JSON input and output are used
    self.output = "json"

  def getList(self, dictionaryName, query):
    payload = {'key': self.key, 'query': query, 'src': 'sdk-python-1.0' }
    endpoint = EntityManager.endpoint(dictionaryName)
    response = requests.get(endpoint, params = payload)
    return EntityManager.parse(response, LIST)

  def read(self, id, dictionaryName):
    payload = {'key': self.key, 'src': 'sdk-python-1.0'} 
    endpoint = EntityManager.endpoint(dictionaryName, id)
    response = requests.get(endpoint, params = payload)
    return EntityManager.parse(response, TYPE)

  def create(self, entity, dictionaryName):
    payload = {'key': self.key, TYPE: str(entity), 'src': 'sdk-python-1.0' }
    endpoint = EntityManager.endpoint(dictionaryName)
    response = requests.post(endpoint, data = payload)
    return EntityManager.parse(response, ID)

  def update(self, entity, dictionaryName):
    payload = {'key': self.key, TYPE: str(entity), 'src': 'sdk-python-1.0' }
    name = entity['id']
    endpoint = EntityManager.endpoint(dictionaryName, name)
    response = requests.put(endpoint, data = payload)
    return EntityManager.parse(response, ID)

  def delete(self, id, dictionaryName):
    payload = {'key': self.key, 'src': 'sdk-python-1.0'}
    endpoint = EntityManager.endpoint(dictionaryName, id)
    response = requests.delete(endpoint, params = payload)
    return EntityManager.parse(response, ID)
