from util.helper import rc

#-----Comman words comes in the disclaimer-----
DISCLAIMER_MESSAGE_WORD = rc('(unauthorized transmission)|(inadmissible)|(exclusively)|(designated)|(confidential)|(privileged)|(intended)|(Strictly)|(prohibited)|(legally privileged)|(notify the sender)|(contains)|(recipient)|(individual user)|(copying)|(distributing)|(dissemination)|(received)|(intended recipient)|(disclaimer)')

#---- Check if the string contains disclaimer word.
DISCLAIMER_KEYWORD = rc('disclaimer')

FIREWALL_MESSAGES=rc('(T|t)his message has been scanned for malware')