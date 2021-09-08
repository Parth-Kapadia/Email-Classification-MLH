#
"""
Created on Sat Oct 28 11:26:49 2017

@author: hiren.soni
"""
from util.helper import rc

#Out Of Office Re: Meeting Minutes 2/27 - Genpact - Topcoder getting started project 
#Automatic reply: Reminder Notification ::[ref:_Case-000182692:ref] 2
#Automatic reply on Case Create from outlook header log
#Undeliverable: RE: MHIA Invoice Processing

AUTOMATIC_REPLY_WORD=rc('^((((A|a)utomatic) ((R|r)eply))|(((O|o)ut) ((O|o)f) ((O|o)ffice)))(:|)')#