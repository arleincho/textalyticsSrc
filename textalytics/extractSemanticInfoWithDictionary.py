 # -#- coding: utf-8 -#-

"""
 uses Textalytics Semantic Publishing API  to tag a text using information defined in a user-defined dictionary. 
 
 The examples creates a dictionary and add three entries: two entities and a concept.
  
 Text is analyzed including the user-defined dictionary and the detected entities and concepts are shown. 
 You can attach your own information to your entities including type, aliases or themes. 
 
 Finally, the dictionary is deleted - you don't need to do this every time. 
 

 To run this example, the license key  for the Semantic Publishing API must be included
 in the KEY variable  in 'config.py' file. 
 If you don't know your key, check your personal area at Textalytics (https://textalytics.com/personal_area)
 
 @author     Textalytics
 @version    1.0 -- 02/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""


from config import KEY
from SemPubClient import SemPubClient
from SemPubException import SemPubException
from Domain import Dictionary, Entity, Concept

textalytics = SemPubClient(KEY)

dictionary = Dictionary('got', 'en', 'Entities and concepts from A Song of Ice and Fire.');

try: 
  print "\n ******** Creating user-defined dictionary... ********"
  textalytics.createDictionary(dictionary)

  print "\n ******** Creating the entity \"King's Landing\"... ********"
  kingsLanding = Entity('01', "King's Landing")
  kingsLanding.setType('Top>Location>GeoPoliticalEntity>City')
  kingsLanding.addTheme('Top>Society>Military')
  kingsLanding.addTheme('Top>Society>Politics')
  textalytics.createEntity(kingsLanding, dictionary)

  print "\n ******** Creating the entity \"Jon Snow\"... ********"
  jon = Entity('02', "Jon Snow")
  jon.setType('Top>Person>FullName')
  jon.addAlias("Ned Stark's bastard")
  jon.addAlias('Bastard of Winterfell')
  jon.addTheme('Top>Society>Military')
  jon.addTheme('Top>Society>Politics')
  textalytics.createEntity(jon, dictionary)

  print "\n ******** Creating the concept \"direwolf\"... ********"
  direwolf = Concept('03', "direwolf")
  direwolf.setType('Top>LivingThing>Animal>Vertebrate>Mammal')
  direwolf.addAlias('direwolves')
  textalytics.createConcept(direwolf, dictionary)

  text = "On Tuesday, author George R.R. Martin stated that his novels take place in an universe meant to be a completely alternate and separate world not linked to our own in any way . It's easy to tell the difference when the plot concerns direwolves, dragons or skinchangers, but the power games that take place in King's Landing could very well be taken from any of the European royal families in Middle Ages, down to the abundance — and associated taint — of children conceived out of marriage, as we see with Ned Stark's bastard."; 

  # filter_data = 'n' provides all information for entities and concepts
  textalytics.setAnalysisFilterData('n')

  print "\n ******** Analyzing the text... ********"
  result = textalytics.analyzeText(text,'en', dictionary)

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
    if 'dictionary' in entity.keys():
      print "\tdictionary: " + entity['dictionary']
    print '\tvariant_list:'
    for variant in entity['variant_list']:
      print '\t\t' + variant['form'] + ', ' + variant['inip'] + ', ' + variant['endp']
    print '\trelevance: ' + entity['relevance']
    if 'dictionary' in entity.keys():
      print "\tid: " + entity['id']
  print 

  print '------------------\nCONCEPTS\n------------------'
  for concept in  result['concept_list']:
    print 'Concept:'
    print '\tform: ' + concept['form'] + "\n\ttype: " + concept['type']
    if 'dictionary' in concept.keys():
      print "\tdictionary: " + concept['dictionary']
    print '\tvariant_list:'
    for variant in concept['variant_list']:
      print '\t\t' + variant['form'] + ', ' + variant['inip'] + ', ' + variant['endp']
    print '\trelevance: ' + concept['relevance']
    if 'dictionary' in concept.keys():
      print "\tid: " + concept['id']
  print 

  print '------------------\nTIME EXPRESSIONS\n------------------'
  for timex in  result['time_expression_list']:
    print 'Time Expression:'
    print '\tform: ' + timex['form'] + '\n\tdate: ' + timex['date'] + '\n\tinip: ' + timex['inip'] + '\n\tendp: ' + timex['endp']
  print

except SemPubException as e:
  print 'Error: ' + str(e)
finally:
  try:
    print "\n ******** Deleting the user-defined dictionary... ********"
    result = textalytics.deleteDictionary(dictionary)
  except SemPubException as e:
    print 'Error: ' + str(e)

