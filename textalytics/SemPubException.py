# -#- coding: utf-8 -#-

"""
 Semantic Publishing exception wraps errors provided by Textalytics API 

 @author     Textalytics
 @version    1.0 -- 03/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""

class SemPubException(Exception):
  def __init__(self, http_code, status):
    self.code = status['code']
    self.message = status['message']
    self.http_code = http_code
    self.moreInfo = status['moreInfo']

  def __str__(self):
    return '' + str(self.code)  + ' (HTTP ' + str(self.http_code) + ') ' + str(self.message) + " - moreInfo: " + str(self.moreInfo)
