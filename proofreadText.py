 # -*- coding: utf-8 -*-

"""  
 This script runs an instance of SemPubClient in order to use Textalytics Proofreading API service to
 proofread a text. There are two ways of proofreading a text, either by sending a json Document object
 (option 1) or just sending the text to analyze (option 2).
 
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

text = "On Tuesday, author George R.R. Martin stated that his novels take place in an universe meant to be a completely alternate and separate world not linked to our own in any way . It's easy to tell the difference when the plot concerns direwolves or dragons, but the power games that take place in King's Landing could very well be taken from any of the European royal families in Middle Ages, down to the abundance — and associated taint — of children conceived out of marriage, as we see with Ned Stark's bastard."; 

textalytics = SemPubClient(KEY)

try: 
  result = textalytics.checkText(text,'en')

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
