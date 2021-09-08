# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:54:31 2017

@author: mitul.kantliwala
"""
from classification.email.signature.extract_signature import has_signature, get_stripped_body

def remove_sig(body, sender_email, sender_name):
    '''
    Strips signature from the body of the message.

    Returns stripped body with signature removed
    If no signature is found then retruns the original body
    '''
    if has_signature(body, sender_email, sender_name):
        body = get_stripped_body(body, sender_email, sender_name)
    return body