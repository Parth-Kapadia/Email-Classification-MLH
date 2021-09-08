# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:28:51 2017
@author: Dhwanil.shah
"""

from util.helper import binary_regex_count
from . import DISCLAIMER_MESSAGE_WORD, DISCLAIMER_KEYWORD, FIREWALL_MESSAGES
import logging

log = logging.getLogger(__name__)

def has_disclaimer(line):
    '''
    check, if message line contain disclaimer
    it return true if disclaimer word is there in string 
    or mre then 2 combination of comman word found in the disclaimer
    else return false
    '''
    lowerstr=line.lower()
    if (binary_regex_count(DISCLAIMER_KEYWORD)(lowerstr) > 0 or binary_regex_count(DISCLAIMER_MESSAGE_WORD)(lowerstr) > 2 or binary_regex_count(FIREWALL_MESSAGES)(lowerstr) > 0):
        return True
    return False

def remove_disclaimer(body):
    '''
    this method accept Mail body and check for disclaimer index 
    and remove it from the mail body.
    this method returns mail body after removing disclaimer
    '''
    dis_idx = get_disclaimer_index(body)
    #body_arr = []
    if(dis_idx!=0):
        return body[0:dis_idx]
    else:
        return body
    
def get_disclaimer_index(body):
    '''
    this method accept Mail body and check for disclaimer index 
    if disclaimer found in the body then return its starting index
    else return 0
    '''
    start_idx = 0
    curr_idx=0
    for line in body:
        if(start_idx==0):
            if (has_disclaimer(line)):
                start_idx=curr_idx
        else:
            break
        curr_idx+=1
    return start_idx