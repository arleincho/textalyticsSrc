# -*- coding: utf-8 -*-

from config import KEY, TAGGING_SERVICE_ENDPOINT, CHECK_SERVICE_ENDPOINT


from DictionaryManager import DictionaryManager
from EntityManager import EntityManager
from ConceptManager import ConceptManager
from SemPubException import SemPubException


from ModelManager import ModelManager
from CategoryManager import CategoryManager

from Domain import Document, Dictionary, Model, Category,  Entity, Concept
import requests

"""
 SemPubClient is a client for Textalytics Semantic Publishing API 
 It provide access to all the functionality including: 
  - semantic tagging of entities, concepts and other relevant data 
  - text proofreading and suggestions 
  - user-defined dictionaries 
  - used-defined classification models

 @author     Textalytics
 @version    1.0 -- 03/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""  

class SemPubClient:

  def __init__(self,key):
    """Constructor for a client object
    """
    self.key = key;
    self.dictionaryManager = DictionaryManager(key)
    self.entityManager = EntityManager(key)
    self.conceptManager  = ConceptManager(key)
    self.modelManager = ModelManager(key)
    self.categoryManager = CategoryManager(key)

    # Default parameter values for /semantic_tagging 
    self.fields = ''
    self.filter_data = 'y'

    # Default parameter values for /check 
    self.mode = 'all'
    self.group_errors = '2'
    self.check_spacing = 'n' 


  # Setters for configuration parameters
  def setAnalysisFields(self, fields):
    self.fields = fields


  def setAnalysisFilterData(self, filter_data):
    self.filter_data = filter_data


  def setCheckMode(self, mode):
    self.model = mode


  def setCheckGroupErrors(self, group_errors):
    self.group_errors = group_errors


  def setCheckSpacing(self, check_spacing):
    self.check_spacing = check_spacing


  def __parseResponse(self, response):
    """
      Helper method that parses the result or throws an Exception if the service returns an error
    """

    if response.status_code == requests.codes.ok:
      r = response.json()
      return r['result']
    else: 
      r = response.json()
      raise SemPubException(response.status_code, r['status'])



    # Semantic tagging service operations
  def analyzeDocument(self, document, dictionary = None, models = None):
    """ Returns the text of the document analyzed including all the extracted semantic information. 
      It takes into account document metadata (language, source, timeref) to build a more accurate analysis
      
      :param document: :class:'Document' to be analyzed 
      :param dictionary (optional): a user defined :class:'Dictionary' to include for tagging 
      :param models (optional): a list of user defined :class:'Model: to include for classification
    """
    payload = {
      'key': self.key, 
      'doc': str(document), 
      'filter_data' : self.filter_data, 
      'fields' : self.fields 
    }
    if (dictionary is not None):
       payload['dictionary'] = dictionary['name']    
    if (models is not None):
      if (isinstance(models, list)):
        modelnames = map(lambda x: x['name'], models)
        payload['model'] = modelnames
      else:
        payload['model'] = models['name']
    payload['src'] = 'sdk-python-1.0'
    endpoint = TAGGING_SERVICE_ENDPOINT
    response = requests.post(endpoint, data = payload)
    return self.__parseResponse(response)


  def analyzeText(self, text, lang, dictionary = None, models = None):
    """ Returns the text analyzed including all the extracted semantic information
      
      :param text: text to be analyzed 
      :param lang: language of the text 
      :param dictionary (optional): a user defined :class:'Dictionary' to include for tagging 
      :param models (optional): a list of user defined :class:'Model: to include for classification
    """
    doc = Document(1, text)
    doc['language'] = lang;
    return self.analyzeDocument(doc, dictionary, models);



  # Text proofreading service operations
  def checkDocument(self, document, doc_offset = 0, dictionary = None):
    """ Returns the proofreading issues found in the document text 
      It takes into account document metadata (language)
      
      :param document: :class:'Document' to be analyzed 
      :param doc_offset: offset in characters from where to start proofreading 
      :param dictionary (optional): a user defined :class:'Dictionary' that marks words in our dictionary as known 
    """
    payload = {
      'key': self.key, 
      'doc': str(document) , 
      'doc_offset': doc_offset, 
      'mode': self.mode, 
      'group_errors': self.group_errors, 
      'check_spacing': self.check_spacing 
    }
    if (dictionary is not None):
      payload['dictionary'] = dictionary['name']            
    payload['src'] = 'sdk-python-1.0'
    endpoint = CHECK_SERVICE_ENDPOINT
    response = requests.post(endpoint, data = payload)
    return self.__parseResponse(response)


  def checkText(self, text, lang, doc_offset = 0, dictionary = None):
    """ Returns the proofreading issues found in the text
      
      :param text: text to be analyzed 
      :param lang: language of the text
      :param doc_offset: offset in characters from where to start proofreading 
      :param dictionary (optional): a user defined :class:'Dictionary'that marks words in our dictionary as known 
    """
    doc = Document(1, text)
    doc['language'] = lang;
    return self.checkDocument(doc, doc_offset, dictionary);



  # CRUD operations on Dictionary  
  def getDictionaryList(self, query, lang):
    """ List of user-defined dictionaries

      :param query: regular expresion to filter dictionaries
      :param lang: filter dictionaries in this language, use 'all' if a multilingual dictionary  
    """ 
    return self.dictionaryManager.getList(query, lang)

  def createDictionary(self, dictionary):
    return self.dictionaryManager.create(dictionary)

  def readDictionary(self, name):
    return self.dictionaryManager.read(name)

  def updateDictionary(self, dictionary):
    return self.dictionaryManager.update(dictionary)

  def deleteDictionary(self, name):
    return self.dictionaryManager.delete(name)

  def deleteDictionary(self, dictionary):
    return self.dictionaryManager.delete(dictionary.getId())



  # CRUD operations on Entity  
  def getEntityList(self, dictionary, query):
    """ Shows a list of entities (:class:'Entity') included in the dictionary matching the query  

      :param dictionary: a :class:'Dictionary' object 
      :param query: a regular expression
    """
    return self.entityManager.getList(dictionary.getId(), query)

  def createEntity(self, entity, dictionary):
    return self.entityManager.create(entity, dictionary.getId())

  def readEntity(self, id, dictionary):
    return self.entityManager.read(id, dictionary.getId())

  def updateEntity(self, entity, dictionary):
    return self.entityManager.update(entity, dictionary.getId())

  def deleteEntity(self, id, dictionary):
    return self.entityManager.delete(id, dictionary.getId())

  def deleteEntity(self, entity, dictionary):
    return self.entityManager.delete(entity.getId(), dictionary.getId())



    # CRUD operations on Concept  
  def getConceptList(self, dictionary, query):
    """ Shows a list of concepts (:class:'Concept') included in the dictionary matching the query  

      :param dictionary: a :class:'Dictionary' object 
      :param query: a regular expression
    """
    return self.conceptManager.getList(dictionary.getId(), query)

  def createConcept(self, concept, dictionary):
    return self.conceptManager.create(concept, dictionary.getId())

  def readConcept(self, id, dictionary):
    return self.conceptManager.read(id, dictionary.getId())

  def updateConcept(self, concept, dictionary):
    return self.conceptManager.update(concept, dictionary.getId())

  def deleteConcept(self, id, dictionary):
    return self.conceptManager.delete(id, dictionary.getId())

  def deleteConcept(self, concept, dictionary):
    return self.conceptManager.delete(concept.getId(), dictionary.getId())



    # CRUD operations on Model  
  def getModelList(self, query, lang):
    """ List of user-defined models

      :param query: regular expresion to filter dictionaries
      :param lang: filter dictionaries in this language 
    """ 
    return self.modelManager.getList(query, lang)

  def createModel(self, model):
    return self.modelManager.create(model)

  def readModel(self, name):
    return self.modelManager.read(name)

  def updateModel(self, model):
    return self.modelManager.update(model)

  def deleteModel(self, name):
    return self.modelManager.delete(name)

  def deleteModel(self, model):
    return self.modelManager.delete(model.getId())



  # CRUD operation on Category  
  def getCategoryList(self, model, query):
    """ Show a list of categories (:class:'Category') included in the model matching the query  

      :param model: a :class:'Model' object 
      :param query: a regular expression
    """
    return self.categoryManager.getList(model.getId(), query)

  def createCategory(self, category, model):
    return self.categoryManager.create(category, model.getId())

  def readCategory(self, id, model):
    return self.categoryManager.read(id, model.getId())

  def updateCategory(self, category, model):
    return self.categoryManager.update(category, model.getId())

  def deleteCategory(self, id, model):
    return self.categoryManager.delete(id, model.getId())

  def deleteCategory(self, category, model):
    return self.categoryManager.delete(category.getId(), model.getId())


