from util.helper import rc

#Email pattern
EMAIL_ADDRESS = rc('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

#URL pattern
URL = rc('https?:\/\/|www\.[\S]+\.[\S]')

#Phone number pattern
PHONE_NO = rc('(\(? ?[\d]{2,3} ?\)?.{,3}?){2,}')

#Thanks
#Regards
#Thank you
#Best Regards
#Kind Regards
#With Kind Regards
#With Best Regards
#Thanx
#Many Thanks
'''
Reg ex for matching the above words
'''
SIGNATURE_WORD_GRP1 = rc('^((((M|m)any )|(T|t)han(k|)((x|s|) (Y|y)ou|))|((W|w)ith |((B|b)est|(K|k)ind) |(R|r)egards))')

#Thanks & Regards
#Thanks and Regards
#Thank you and best regards
#Thanks and best regards
#Thanks & best regards
'''
Reg ex for matching the above words
'''
SIGNATURE_WORD_GRP2 = rc('^((((T|t)han(k|)((x|s|)))( |)(((Y|y)ou)|)) (&|(A|a)nd) (((B|b)est )|((R|r)egards)))')

#Thanks in advance
#Thank you in advance
#Thanks a lot
#Thank you very much in advance
'''
Reg ex for matching the above words
'''
SIGNATURE_WORD_GRP3 = rc('^((((T|t)han(k|)((x|s|)))( |)(((Y|y)ou)|)( |)(((V|v)ery)|)( |)(((M|m)uch)|)) (((I|i)n (a|A)dvance)|((a|A) (l|L)ot)))')

#Tx
#BR
#KR
#Rgds
'''
Reg ex for matching the above words
'''
SIGNATURE_WORD_GRP4 = rc('^(((T|t)x)|((B|b)(R|r))|((K|k)(R|r))|((R|R)gds))')

#warmest regards
SIGNATURE_WORD_GRP5 = rc('^((((W|w)arm(est|))|)(| )(((R|r)egard(s|))|)(,|))$')