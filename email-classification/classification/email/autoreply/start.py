# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 11:26:49 2017

@author: hiren.soni
"""
from util.helper import binary_regex_search
from classification.email.autoreply import AUTOMATIC_REPLY_WORD
#subject='Re: Meeting Minutes 2/27 - Genpact - Topcoder getting started project '

#checking auto keyword from subject like Out Of Office,Automatic reply,Undeliverable
#If contains this keyword then it return true else it return false

def is_autoreplyemail(subject):
        if (binary_regex_search(AUTOMATIC_REPLY_WORD)(subject) > 0):
            return True
        return False


