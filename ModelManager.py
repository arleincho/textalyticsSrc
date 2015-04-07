# -#- coding: utf-8 -#-

"""
 This class makes the requests that correspond to model resources operations in the User
 Resources Management service.
 
 @author     Textalytics
 @version    1.0 -- 03/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""

import requests
from config import MANAGE_SERVICE_ENDPOINT,KEY
from SemPubException import SemPubException

TYPE = "model"
LIST = TYPE + "_list"
ID = 'id'

class ModelManager:

  @staticmethod
  def endpoint(resourceId = None):
    if (resourceId == None):
       return MANAGE_SERVICE_ENDPOINT + "/" + LIST
    else: 
       return MANAGE_SERVICE_ENDPOINT + "/" + LIST + "/" + resourceId

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
    payload = {'key': self.key, 'query': query, 'language': language, 'src': 'sdk-python-1.0'}
    endpoint = ModelManager.endpoint()
    response = requests.get(endpoint, params = payload)
    return ModelManager.parse(response, LIST)


  def read(self, name):
    payload = {'key': self.key, 'src': 'sdk-python-1.0'}
    endpoint = ModelManager.endpoint(name)
    response = requests.get(endpoint, params = payload)
    return ModelManager.parse(response, TYPE)


  def create(self, model):
    payload = {'key': self.key, TYPE: str(model), 'src': 'sdk-python-1.0' }
    endpoint = ModelManager.endpoint()
    response = requests.post(endpoint, data = payload)
    return ModelManager.parse(response, ID)


  def update(self, model):
    payload = {'key': self.key, TYPE: str(model), 'src': 'sdk-python-1.0' }
    name = model['name']
    endpoint = ModelManager.endpoint(name)
    response = requests.put(endpoint, data = payload)
    return ModelManager.parse(response, ID)


  def delete(self, name):
    payload = {'key': self.key, 'src': 'sdk-python-1.0'}
    endpoint = ModelManager.endpoint(name)
    response = requests.delete(endpoint, params = payload)
    return ModelManager.parse(response, ID)
