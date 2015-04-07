# -#- coding: utf-8 -#-

"""
 This script runs an instance of SemPubClient in order to use Textalytics Semantic Publishing API
 services to tag semantic information in a text using a user-defined text classification model.
 Before the analysis, the script will create a model and then it will add two categories.
 Once this has been done, the text will be analyzed. There are two ways of analyzing a text, either
 by sending a json Document object (option 1) or just sending the text to analyze (option 2). When the
 analysis is finished, the model will be deleted.
 
 To run this example, the license key  for the Semantic Publishing API must be included in the KEY 
 variable  in 'config.py' file.  If you don't know your key, check your personal area at Textalytics 
 (https://textalytics.com/personal_area)
 
 @author     Textalytics
 @version    1.0 -- 03/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""

from config import KEY
from SemPubClient import SemPubClient
from SemPubException import SemPubException
from Domain import Model, Category


textalytics = SemPubClient(KEY)

model = Model('got_geography_model', 'en', 'A Song of Ice and Fire geography classification model.');

try: 
  print "\n ******** Creating the user-defined text classification model... ********"
  textalytics.createModel(model)

  # Westeros category definition
  w_positive = "beyond+the+wall|the+iron+islands|the+vale+of+arryn|the+north|the+riverlands|the+westerlands|the+crownlands|the+reach|the+stormlands|the+wall|dorne|the+seven+kingdoms|free+folk|iron+throne|faith+of+the+seven|old+gods|drowned+god|oldtown|lannisport|gulltown|white+harbor|king+landing"
  w_relevant = "house_baratheon~baelish~martell~greyjoy~arryn~stark~tyrell~lannister|harrenhall|eyrie|casterly+rock|children+of+the+forest|giant|giants|others|white+walkers|white+walker|direwolf|direwolves|lizard-lion|lizard-lions|mammoth|mammoths|raven|ravens|shadowcat|shadowcats"
  w_irrelevant = "beyond+the+narrow+sea|eastern+continent|the+east|free+cities|dothraki+sea|shivering+sea|valyrian+peninsula|slaver|ghiscar|lhazar|qarth|eastern+essos|essos|dothraki|ghiscari|lhazareen|qartheen|ibbenese|jogos+nhai"
  w_training_text = "The continent of Westeros is long and relatively narrow, extending from Dorne in the south to the Lands of Always Winter in the far north, where a large amount of land remains uncharted, due to the extremely cold temperatures and hostile inhabitants known as wildlings. Although no scale appears on the maps in the books themselves, George R. R. Martin has stated that the Wall is a hundred leagues long, or three hundred miles. Thus the continent stretches for about 3,000 miles from north to south and for some 900 miles at its widest point east to west. Its eastern coast borders on the narrow sea; across those waters lies the eastern continent of Essos and the island chain known as the Stepstones. To the south is located the Summer Sea, and within it the Summer Islands. The northern lands of Westeros are less densely populated than the south despite their roughly equivalent size. The five major cities of Westeros are, in order of size: King's Landing, Oldtown, Lannisport, Gulltown, and White Harbor. Westeros was originally divided into several independent kingdoms before the consolidation of the War of Conquest. After this war and the eventual incorporation of Dorne, all the regions south of the Wall were united under the rule of House Targaryen into a nation that is known as the Seven Kingdoms."
  westeros = Category('01','Westeros - far west of the known world',w_positive, '', w_relevant, w_irrelevant, w_training_text);

  print "\n ******** Creating the category \"Westeros - far west of the known world\"... ********"
  textalytics.createCategory(westeros, model)

  # Essos category definition 
  e_positive = 'the+free+cities|the+dothraki+sea|the+shivering+sea|valyrian+peninsula|slaver|ghiscar|lhazar|qarth|eastern+essos'
  e_relevant = 'dothraki|lhazareen|qartheen|ibbenese|jogos+nhai|ghiscari'
  essos = Category('02','Essos - beyond the narrow sea',  e_positive, '', e_relevant);

  print "\n ******** Creating the category \"Essos - beyond the narrow sea\"... ********"
  textalytics.createCategory(essos, model)

  text = "On Tuesday, author George R.R. Martin stated that his novels take place in an universe meant to be a completely alternate and separate world not linked to our own in any way . It's easy to tell the difference when the plot concerns direwolves, dragons or skinchangers, but the power games that take place in King's Landing could very well be taken from any of the European royal families in Middle Ages, down to the abundance — and associated taint — of children conceived out of marriage, as we see with Ned Stark's bastard."; 

    # you may submit several user-defined models for text classification 
    # usa a list of models then [model1. model2, ..., modelN]
  print "\n ******** Analyzing the text... ********"
  result = textalytics.analyzeText(text, 'en', None, [model])

  print '------------------\nCATEGORIES\n------------------'
  for category in  result['category_list']:
    print 'Category:'
    print '\tcode: ' + category['code']  + "\n\trelevance: " + category['relevance']
    print '\tlabel _list:\n\t\t' +  ' - '.join(category['label_list'])
  print

  print "------------------\nUSER'S CATEGORIES\n------------------"
  for category in  result['got_geography_model_list']:
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
    print "\n ******** Deleting the user-defined model... ********\n"
    textalytics.deleteModel(model)
  except SemPubException as e:
    print 'Error: ' + str(e)
