# -#- coding: utf-8 -#-

"""
 Textalytics Semantic Publishing API 1.0 
 Python Configuration file 

 @author     Textalytics
 @version    1.0 -- 03/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""


PROTOCOL = "http"
HOST = "textalytics.com"
SERVICE_ENDPOINT = "/api/sempub/1.0"
TAGGING_SERVICE_ENDPOINT = PROTOCOL+"://"+HOST+SERVICE_ENDPOINT+'/semantic_tagging'
CHECK_SERVICE_ENDPOINT = PROTOCOL+"://"+HOST+SERVICE_ENDPOINT + '/check'
MANAGE_SERVICE_ENDPOINT = PROTOCOL+"://"+HOST+SERVICE_ENDPOINT + '/manage'

KEY = "1bbef26a43c34b453b1713039c49a513"


