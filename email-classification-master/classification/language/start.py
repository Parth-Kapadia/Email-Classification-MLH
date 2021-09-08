# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:04:56 2017

@author: hiren.soni
"""
#Load google translate python library
from googletrans import Translator
#The maximum character limit on a single text is 15k

CHAR_LIMIT=4000
    
#This method use to detect language from input text
def detect(original_text):
    translator = Translator()
    
    if(original_text != ""):
        if(len(original_text) > CHAR_LIMIT):
            #print('having more then 5000 character len ', len(' '.join(original_text.splitlines())[:5000]))
            #print('having more then 5000 character', ' '.join(original_text.splitlines())[:5000])
            return translator.detect(' '.join(original_text.splitlines())[:CHAR_LIMIT])
        else:
            return translator.detect(original_text)
    return None

#This method use to detect language & translate text from input text
def translate(original_text,destination_language):
    translator = Translator()
    try:
        language_name=detect(original_text)
        if language_name.lang != destination_language:
            translatedText=''
            if(len(original_text) > CHAR_LIMIT):
                idx = 0
                while True:
                    if(len(original_text) <= ( (idx+1) * CHAR_LIMIT)):
                        translatedText = translatedText + translator.translate(text=original_text[(idx*CHAR_LIMIT)], dest=destination_language).text
                        break
                    else:
                        translatedText = translatedText + translator.translate(text=original_text[(idx*CHAR_LIMIT) : ( (idx+1) * CHAR_LIMIT )], dest=destination_language).text
                    idx=idx+1                    
            else:
                translatedText=translator.translate(text=original_text, dest=destination_language).text
            return translatedText
        else:
            return original_text
    except Exception as e:
        print('Error while google translation : ' + str(e))
        return original_text
    