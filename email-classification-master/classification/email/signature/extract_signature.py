# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:54:31 2017

@author: mitul.kantliwala
"""
from __future__ import absolute_import
from fuzzywuzzy import fuzz
from util.helper import binary_regex_search, extractAlphabaets, to_unicode
from classification.email.signature import EMAIL_ADDRESS,URL,SIGNATURE_WORD_GRP1,SIGNATURE_WORD_GRP2,SIGNATURE_WORD_GRP3,SIGNATURE_WORD_GRP4, SIGNATURE_WORD_GRP5

TOO_LONG_SIGNATURE_LINE = 30
SIGNATURE_MAX_LINES = 20

def is_signature_line(line, sender_email, sender_name):
    '''
    Checks if the line has signature
    Returns True or False
    '''
    if len(line.strip()) > TOO_LONG_SIGNATURE_LINE:
        return False
    elif has_signature_word(line) or has_sender_name(line, sender_email, sender_name):
        return True
    elif (#binary_regex_search(PHONE_NO)(line) > 0 or
          binary_regex_search(EMAIL_ADDRESS)(line) > 0 or
          binary_regex_search(URL)(line) > 0):
        return True

def has_signature(body, sender_email, sender_name):
    '''
    Checks if signature is present in body
    Returns True or False
    '''
    for line in body:
        if is_signature_line(line, sender_email, sender_name):
            return True
    return False

def get_stripped_body(body, sender_email, sender_name):
    '''
    Strips any signature lines from mail body
    Returns stripped body
    '''
    #Consider last few lines from body for signature
    candidate = body
    # if(len(body) > 2):
    #     candidate = body[2:]

    candidate = candidate[-min(SIGNATURE_MAX_LINES, len(candidate)):]
    #print ('candidate = ',str(candidate))

    #Get the lines from body which are not in candidate
    nonCandidate = [line for line in body if line not in candidate]
    #print('nonCandidate = '+str(nonCandidate))

    signature_index = -1
    for index,line in enumerate(candidate):
        #print ('sig line = '+line+'---- is sig = '+str(is_signature_line(line,sender)))
        if(is_signature_line(line,sender_email, sender_name)):
            signature_index = index
            #Check next 3 lines and see if it has signature
            if(index + 3 < len(candidate)):
                upvotes = 0
                for sub_index in range(index + 1, index + 3):
                    if(is_signature_line(candidate[sub_index], sender_email, sender_name)):
                        upvotes += 1
                if(upvotes >= 1):
                    signature_index = index
            else:
                upvotes = 0
                for sub_index in range(index + 1, len(candidate)):
                    if(is_signature_line(candidate[sub_index], sender_email, sender_name)):
                        upvotes += 1
                if(upvotes >= 1):
                    signature_index = index
        if(signature_index != -1):
            break
    #print('signature_index = '+str(signature_index))
    if(signature_index != -1):
        nonCandidate.extend(candidate[:signature_index])
        return nonCandidate
    else:
        return body

def has_signature_word(line):
    '''
    Checks if line contains signature words
    return True or False
    '''
    if(binary_regex_search(SIGNATURE_WORD_GRP1)(line) > 0 or
       binary_regex_search(SIGNATURE_WORD_GRP2)(line) > 0 or
       binary_regex_search(SIGNATURE_WORD_GRP3)(line) > 0 or
       binary_regex_search(SIGNATURE_WORD_GRP4)(line) > 0 or
       binary_regex_search(SIGNATURE_WORD_GRP5)(line) > 0):
        return True
    return False

def has_sender_name(line, sender_email, sender_name):
    '''
    Checks if line contains sender name or email address
    If sender name has email address remove domain part
    return True or False
    '''
    # Old Logic
    # line = to_unicode(extractAlphabaets(line.lower()),precise=True)

    # if(binary_regex_search(EMAIL_ADDRESS)(sender) > 0):
    #     sender = " ".join(filter(None,list(set(map(str.strip,extractAlphabaets(sender.split('@')[0]).split(' '))))))
    # else:
    #     sender = extractAlphabaets(sender)
    # return fuzz.partial_ratio(line,sender) > 75

    # New Logic
    line = to_unicode(extractAlphabaets(line.lower()),precise=True).strip()

    if line != '' and sender_name != None and sender_name != '':
        sender = sender_name.lower()
    elif line != '' and sender_email != None and sender_email != '' and binary_regex_search(EMAIL_ADDRESS)(sender_email) > 0:
        sender = " ".join(filter(None,list(set(map(str.strip,extractAlphabaets(sender_email.split('@')[0]).split(' '))))))
    else:
        return False

    return fuzz.partial_ratio(line,sender) >= 75
