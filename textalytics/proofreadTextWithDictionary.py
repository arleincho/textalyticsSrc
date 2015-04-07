 # -*- coding: utf-8 -*-
 
""" 
 This script runs an instance of SemPubClient in order to use Textalytics Semantic Publishing API
 services to proofread a text using a user-defined dictionary. Before the analysis, the script will
 create a dictionary and then it will add three entries: two entities and a concept. Once this has
 been done, the text will be proofread. There are two ways of proofreading a text, either by sending
 a json Document object (option 1) or just sending the text to analyze (option 2). Once this has
 been done, the dictionary will be deleted.

 In order to run this example, the license key obtained for the Semantic Publishing API must be included
 in the KEY variable  in 'config.inc' file. If you don't know your key, check your personal area at
 Textalytics (https://textalytics.com/personal_area)
  
 @author     Textalytics
 @version    1.0 -- 03/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""


from config import KEY
from SemPubClient import SemPubClient
from SemPubException import SemPubException
from Domain import Dictionary, Model, Category, Entity, Concept


textalytics = SemPubClient(KEY)

try:
  print "\n ******** Creating user-defined dictionary... ********"
  dictionary = Dictionary('got', 'en', 'Entities and concepts from A Song of Ice and Fire.');
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

  text = "On Tuesday, author George R.R. Martin stated that his novels take place in an universe meant to be a completely alternate and separate world not linked to our own in any way . It's easy to tell the difference when the plot concerns direwolves or dragons, but the power games that take place in King's Landing could very well be taken from any of the European royal families in Middle Ages, down to the abundance — and associated taint — of children conceived out of marriage, as we see with Ned Stark's bastard."; 

  print "\n ******** Analyzing the text... ********"
  result = textalytics.checkText(text,'en', 0, dictionary)

  print "------------------\nISSUES\n------------------\n"
  for issue in  result['issue_list'] :
    print 'Issue:\n' + '\ttext: ' + issue['text'] + '\n\ttype: ' + issue['type']
    print '\tmsg: ' + issue['msg'] + '\n\tSuggestions:'

    for suggestion in  issue['sug_list']:
      print '\t\tform: ' + suggestion['form'] + "\n\t\tconfidence: " + suggestion['confidence']
    print '\tinip: ' + issue['inip'] + '\n\tendp: ' + issue['endp']
  print 

except SemPubException as e:
  print 'Error: ' + str(e)
finally:
  try:
    print "\n ******** Deleting the user-defined dictionary... ********"
    result = textalytics.deleteDictionary(dictionary)
  except SemPubException as e:
    print 'Error: ' + str(e)
