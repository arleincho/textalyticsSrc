"""
  Domain classes for Textalytics Semantic Publishing API 

 @author     Textalytics
 @version    1.0 -- 03/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""

import json

class Document(dict):
	"Wrap a document information included in textaytics.com requests. Id and text are required values"
	def __init__(self, id, txt):
		self['id'] = id
		self['txt'] = txt

	def __str__(self):
		return '{ "document" : ' + json.dumps(self) + '}'

class Dictionary(dict):
	"User-defined Dictionary may contain your own Entities and Concepts to tailor the results of semantic tagging and proofreading"
	def __init__(self, name, language, description):
		self['name'] = name 
		self['language'] = language
		self['description'] = description 

	def getId(self):
		return self['name']

	def __str__(self):
		return '{ "dictionary" : ' + json.dumps(self) + "}";

class Entity(dict):
	" An entity represents a real world object with a proper name. You can add aliases, a type and related themes "
	def __init__(self, id, form):
		self['id'] = id
		self['form'] = form
		self['alias_list'] = []
		self['theme_list'] = []

	def getId(self):
		return self['id']

	def addAlias(self, alias):
		self['alias_list'].append(alias)

	def setType(self, type):
		self['type'] = type;

	def addTheme(self, theme):
		self['theme_list'].append(theme);

	def __str__(self):
		return '{ "entity" : ' + json.dumps(self) + '}'


class Concept(dict):
	" A concept or a class of objects that is represented with a word. You can add aliases, a type and related themes "
	def __init__(self, id, form):
		self['id'] = id
		self['form'] = form
		self['alias_list'] = []
		self['theme_list'] = []

	def getId(self):
		return self['id']

	def addAlias(self, alias):
		self['alias_list'].append(alias)

	def setType(self, type):
		self['type'] = type;

	def addTheme(self, theme):
		self['theme_list'].append(theme);

	def __str__(self):
		return '{ "concept" : ' + json.dumps(self) + "}";


class Model(dict):
	"User-defined classification models may contain your own models with many :class:'Category' to classify text with semantic tagging. You may have several models to classify a single document."
	def __init__(self, name, language, description):
		self['name'] = name 
		self['language'] = language
		self['description'] = description 
	
	def getId(self):
		return self['name']

	def __str__(self):
		return '{ "model" : ' + json.dumps(self) + "}";

class Category(dict):
	"""  A Category represents a label that may be assigned to a document with respect to a classification model. You can include training text to model categories and rules. 

    	:param code: the unique code that identifies the category
    	:param label: a human readable label 
    	:param positive: positive terms - if the term appeat the document will be  classified with this category. The syntax for complex terms is detailed in the API documnentation 
    	:param negative: negative terms mute this category if appear 
		:param relevant: relevant terms vote up this category when they appear 
		:param irrelevant: irrrelevant terms vote down this category when they appear 
    """	
	def __init__(self, code, label, positive=None, negative=None, relevant=None, irrelevant=None, text=None):
		self['code'] = code
		self['label'] = label	
		if (positive != None):
			self['positive'] = positive
		if (negative != None):
			self['negative'] = negative
		if (relevant != None):
			self['relevant'] = relevant
		if (irrelevant != None):
			self['irrelevant'] = irrelevant
		if (text != None):
			self['text'] = text

	def getId(self):
		return self['code']

	def __str__(self):
		return '{ "category" : ' + json.dumps(self) + "}";



