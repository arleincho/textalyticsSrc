# -#- coding: utf-8 -#-

"""
 A manager for Category resources 

 @author     Textalytics
 @version    1.0 -- 03/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""

import requests
from config import MANAGE_SERVICE_ENDPOINT
from Domain import Category
from SemPubException import SemPubException

COLLECTION = "/model_list/"
TYPE = "category"
LIST = "category_list"
ID = "id"

class CategoryManager:

  @staticmethod
  def endpoint(modelName, id = None):
    if (id == None):
      return MANAGE_SERVICE_ENDPOINT + COLLECTION + modelName + "/" + LIST
    else:
      return MANAGE_SERVICE_ENDPOINT + COLLECTION + modelName + "/" + LIST + "/" + id

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


  def getList(self, modelName, query):
    payload = {'key': self.key, 'query': query, 'src': 'sdk-python-1.0' }
    endpoint = CategoryManager.endpoint(modelName)
    response = requests.get(endpoint, params = payload)
    return CategoryManager.parse(response, LIST)


  def read(self, id, modelName):
    payload = {'key': self.key, 'src': 'sdk-python-1.0'} 
    endpoint = CategoryManager.endpoint(modelName, id)
    response = requests.get(endpoint, params = payload)
    return CategoryManager.parse(response, TYPE)


  def create(self, Category, modelName):
    payload = {'key': self.key, TYPE: str(Category), 'src': 'sdk-python-1.0' }
    endpoint = CategoryManager.endpoint(modelName)
    response = requests.post(endpoint, data = payload)
    return CategoryManager.parse(response, ID)


  def update(self, Category, modelName):
    payload = {'key': self.key, TYPE : str(Category), 'src': 'sdk-python-1.0' }
    name = Category['code']
    endpoint = CategoryManager.endpoint(modelName, name)
    response = requests.put(endpoint, data = payload)
    return CategoryManager.parse(response, ID)

  def delete(self, id, modelName):
    payload = {'key': self.key, 'src': 'sdk-python-1.0'}
    endpoint = CategoryManager.endpoint(modelName, id)
    response = requests.delete(endpoint, params = payload)
    return CategoryManager.parse(response, ID)
