# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:21:29 2017

@author: mekyush.jariwala
"""

from classification.email.trailmail.extract import has_trailmail, get_trail_mail
import logging

log = logging.getLogger(__name__)

def extract(body):
    try:
        #body = body.strip()
        
        #fatching non empty line
        #non_empty = [line for line in body.splitlines() if line.strip()]
        
        #return body if it is empty
        #if len(non_empty) == 0:
        #    return [body]

        if has_trailmail(body):
            '''
            split body into seprate mails based on trails
            '''
            return get_trail_mail(body)
            
    except Exception as e:
        log.exception('ERROR when searching trail mail from body ', str(e))
    
    return [body]