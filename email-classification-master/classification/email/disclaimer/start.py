# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:15:23 2017
@author: Dhwanil.shah
"""

from classification.email.disclaimer.extract import remove_disclaimer

#from util import get_delimiter
import logging

log = logging.getLogger(__name__)

def extract(body):
    '''function that returns body of mail after removing desclaimer
    from the mail body
    
    first it will split body line by line and remove the extra space and tabs
    line by line from body and genrate new Body which will pass to other 
    method to remove disclaimer.
    '''
    try:
       
        #remove disclaimer from the mail body
        body=remove_disclaimer(body)
        #print ('############################',body)
    except Exception as e:
        log.exception('ERROR when seasrching trail mail from body ', str(e))
    
    return body