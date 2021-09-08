# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:34:41 2017

@author: mekyush.jariwala
"""
from util.helper import binary_regex_search
from . import ORIGINAL_MESSAGE_WORD, FORWARDED_MESSAGE_WORD, BEGIN_FORWARDED_MESSAGE, TRAIL_WITH_MESSAGE_FROM_WORD, TRAIL_WITH_SENT_DATE, TRAIL_WITH_FROM_TO, TRAIL_WITH_ON_WORD
import logging

log = logging.getLogger(__name__)

def has_trailmail(body):
    '''
    check, if message have trail mail or not
    return True or False
    '''
    for line in body:
        if (binary_regex_search(ORIGINAL_MESSAGE_WORD)(line) > 0 or 
            binary_regex_search(FORWARDED_MESSAGE_WORD)(line) > 0 or
            binary_regex_search(BEGIN_FORWARDED_MESSAGE)(line) > 0 or
            binary_regex_search(TRAIL_WITH_MESSAGE_FROM_WORD)(line) > 0 or
            binary_regex_search(TRAIL_WITH_SENT_DATE)(line) > 0 or
            binary_regex_search(TRAIL_WITH_ON_WORD)(line) > 0 or
            binary_regex_search(TRAIL_WITH_FROM_TO)(line) > 0):
            return True
    return False

def get_trail_mail(body):
    lst_idx = get_trail_index(body)
    body_arr = []
    for tup in lst_idx:
        body_arr.append(body[tup[0]:tup[1]])
    return body_arr


def get_trail_index(body):    
    start_idx = 0
    from_to_started = False
    is_prev_line_static = False
    lst = []
    curr_idx=0
    for line in body:
        #print (curr_idx, ' ',line)
        if (binary_regex_search(ORIGINAL_MESSAGE_WORD)(line) > 0):
            #print ('into 1 ', curr_idx)
            lst.append((start_idx,curr_idx))
            start_idx = curr_idx+1
            is_prev_line_static = True
        elif (binary_regex_search(FORWARDED_MESSAGE_WORD)(line) > 0 or
            binary_regex_search(BEGIN_FORWARDED_MESSAGE)(line) > 0 or
            binary_regex_search(TRAIL_WITH_MESSAGE_FROM_WORD)(line) > 0):
            #print ('into 1 ', curr_idx)
            if(curr_idx == 0):
                lst.append((start_idx,curr_idx))
            else:
                lst.append((start_idx,curr_idx))
                start_idx = curr_idx+1
            is_prev_line_static = True
        elif (binary_regex_search(TRAIL_WITH_FROM_TO)(line) > 0):
            #print ('into 3' , from_to_started)
            if not(from_to_started):
                from_to_started = True
                if(not(is_prev_line_static)):
                    if(curr_idx == 0):
                        lst.append((start_idx,curr_idx))
                    else:
                        lst.append((start_idx,curr_idx))
                        start_idx = curr_idx
            is_prev_line_static = False
        elif(binary_regex_search(TRAIL_WITH_SENT_DATE)(line) > 0 or binary_regex_search(TRAIL_WITH_ON_WORD)(line) > 0):
            #print ('into 2 ', curr_idx)
            if(curr_idx == 0):
                lst.append((start_idx,curr_idx))
            else:
                lst.append((start_idx,curr_idx))
                start_idx = curr_idx
            is_prev_line_static = False
        else:
            #print ('into 4')
            from_to_started = False
            is_prev_line_static = False
        curr_idx+=1        
    lst.append((start_idx,len(body)))    
    return lst