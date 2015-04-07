# -*- coding: utf-8 -*-

"""
 This script analyzes a text with the Semantic tagging service.
 The semantic tagging service identifies relevant information in your content and helps you to annotate it.
 This service analyzes the text with semantic annotations like:
   - Entity extraction
   - Concept extraction
   - Document categorization
   - Linked Open Data
   - Other relevant data (money expressions, url, phones and e-mails)

 To analyze the text there are two options
   1. Analyze with a Document object
   2. Analyze directly with the text
 In this example it used the option 2
 
 @author     Textalytics
 @version    1.0 -- 03/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""

from config import KEY
from SemPubClient import SemPubClient
from SemPubException import SemPubException

text = "On Tuesday, author George R.R. Martin stated that his novels take place in an universe meant to be a completely alternate and separate world not linked to our own in any way . It's easy to tell the difference when the plot concerns direwolves, dragons or skinchangers, but the power games that take place in King's Landing could very well be taken from any of the European royal families in Middle Ages, down to the abundance — and associated taint — of children conceived out of marriage, as we see with Ned Stark's bastard."; 

try:
  textalytics = SemPubClient(KEY)
  result = textalytics.analyzeText(text, 'en')

  print '------------------\nCATEGORIES\n------------------'
  for category in  result['category_list']:
    print 'Category:'
    print '\tcode: ' + category['code']  + "\n\trelevance: " + category['relevance']
    print '\tlabel _list:\n\t\t' +  ' - '.join(category['label_list'])
  print 

  print '------------------\nENTITIES\n------------------'
  for entity in  result['entity_list']:
    print 'Entity:'
    print '\tform: ' + entity['form'] + "\n\ttype: " + entity['type']
    print '\tvariant_list:'
    for variant in entity['variant_list']:
      print '\t\t' + variant['form'] + ', ' + variant['inip'] + ', ' + variant['endp']
    print '\trelevance: ' + entity['relevance']
  print 

  print '------------------\nCONCEPTS\n------------------'
  for concept in  result['concept_list']:
    print 'Concept:'
    print '\tform: ' + concept['form'] + "\n\ttype: " + concept['type']
    print '\tvariant_list:'
    for variant in concept['variant_list']:
      print '\t\t' + variant['form'] + ', ' + variant['inip'] + ', ' + variant['endp']
    print '\trelevance: ' + concept['relevance']
  print 

  print '------------------\nTIME EXPRESSIONS\n------------------'
  for timex in  result['time_expression_list']:
    print 'Time Expression:'
    print '\tform: ' + timex['form'] + '\n\tdate: ' + timex['date'] + '\n\tinip: ' + timex['inip'] + '\n\tendp: ' + timex['endp']
  print 
except SemPubException as e:
  print 'Error: ' + str(e)
