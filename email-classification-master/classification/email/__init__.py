

from classification.email.trailmail.start import extract as extract_mail_body
from classification.email.disclaimer.start import extract as remove_disclaimer
from classification.email.signature.start import remove_sig as remove_signature
from classification.language.start import translate
from classification.language import Language
from util.utils import get_sender_details,remove_stopword,apply_stemming, remove_external_mail_marker
from config import getLogger
from bs4 import BeautifulSoup
import re
import copy

LOGGER = getLogger(__name__)

def replace_with_newlines(element):
    text = ''
    #print(element.string)
    for elem in element.recursiveChildGenerator():
        if isinstance(elem, str):
            text += elem.strip()
        elif elem.name == 'br':
            text += '\n'
    return text + '\n'

def cleanup_mail(subject, body, sender_name, sender_email):
    '''
    method to cleanup incomming mail
    
    subject - subject if incoming mail
    body - original body of the mail
    sender_name - name of the sender
    sender_email - email id of sender
    '''
    
    '''Removing HTML Tags from body if have'''
    soup = BeautifulSoup(body,features="lxml",from_encoding="utf-8")
    for p in soup.find_all("p"):
        p.replace_with(replace_with_newlines(p))
    for br in soup.find_all("br"):
        br.replace_with("\n")
    
    [tag.decompose() for tag in soup("style")]
    [tag.decompose() for tag in soup("script")]
    body = soup.get_text()
    #replace non ascii word
    # Lo unicode categories needs to be allow which includes all caharachter of differenct country like Chinese, Rusian, Arebic
    body = re.sub(r'[^\x00-\x7f]',r'', body)
    '''convert text in englist if it is not'''
    # subject = translate(subject, Language.English)
    # body = translate(body, Language.English)
    # print('for sender name')
    # sender_name = translate(sender_name, Language.English)
    
    body = body.strip()
    #fatching non empty line
    non_empty = [line for line in body.splitlines() if line.strip()]
    
    #return body if it is empty
    if len(non_empty) == 0:
        return [body], [body]

    '''
    spilts original mail based on seprate trail
    '''
    mails_for_entity = []
    mails = extract_mail_body(non_empty)
    LOGGER.info('THis is simple log from cleanup')
    if(len(mails) > 0):
        '''removing desclaimer'''
        for index, mail in  enumerate(mails):
            
            '''striping the body'''
            #print('before : ' + str(type(mails[index])))
            mails[index] = list(map(str.strip, mail))
            #print('after : ' + str(type(mails[index])))
            '''striping the body'''
            #print('before printing11')
            #for line in mails[index]:
            #    print(str(index)+'@' + line + '@')
            #print('before : ' + str(type(mails[index])))
            mails[index] = remove_disclaimer(mails[index])
            #print('after : ' + str(type(mails[index])))
            #print('before printing' + len(mails[index]))
            #for line in mails[index]:
            #    print(str(index)+'@' + line + '@')
        '''removing signature'''
        for index, mail in enumerate(mails):
            '''getting data of sender from trail mail'''

            if index == 0:
                sender_dtl = ''.join([sender_name,'<',sender_email,'>']) if sender_name != None and sender_name != '' else sender_email 
                # if(sender_email is not Non)
                if(sender_dtl is not None):
                    mails[index] = remove_signature(mail, sender_email, sender_name)
            else:
                sub, sender_dtl, body = get_sender_details(mail)
                LOGGER.info('!@#$')
                LOGGER.info( (sub, sender_dtl, body) )
                #print( (sub, sender_dtl, body) )
                if(sender_dtl is not None):
                    mails[index] = remove_signature(body, sender_dtl, None)
            
                '''getting data of sender from trail mail'''
                LOGGER.info('after removing signature')
                #print('after removing signature')
                LOGGER.info(mails[index])
                #print(mails[index])
           
            ''' removing externla mail keyword'''
            mails[index] = remove_external_mail_marker(mails[index])
            ''' removing externla mail keyword'''
            
            '''coping emails for entity'''
            mails_for_entity.append(copy.deepcopy(mails[index]))
            '''coping emails for entity'''
            
            ''' Removes punctuations, stop words and Stamming from mails'''
            for idx,line in enumerate(mails[index]):
                mails[index][idx] = remove_stopword(line) 
                
    return mails, mails_for_entity
