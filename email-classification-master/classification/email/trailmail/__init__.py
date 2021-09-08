

from util.helper import rc


#-----Original Message-----
ORIGINAL_MESSAGE_WORD = rc('(?<=-)( |)((O|o)riginal (M|m)essage)( |)(?=-)')


#---------- Forwarded message ----------
FORWARDED_MESSAGE_WORD = rc('(?<=-)( |)((F|f)orwarded (M|m)essage)( |)(?=-)')


#Begin forwarded message:
BEGIN_FORWARDED_MESSAGE = rc('(((B|b)egin) ((F|f)orwarded) ((M|m)essage))(?=:)')


#----- Message from "Bertolini-Bosga, Kim" > on Wed, 18 Nov 2015 17:38:10 +0000 -----
TRAIL_WITH_MESSAGE_FROM_WORD = rc('(?<=-)( |)((M|m)essage (F|f)rom).*')


#2015-11-26 13:06 GMT+01:00 Nemethova, Andrea >:
#2016-09-29 11:01 GMT+02:00 Fischerova, Nikola < nfischerova@prologis.com >: 
TRAIL_WITH_SENT_DATE = rc('^((\d{1,2})|(\d{4}))[ /.-]((\d{1,2})|(((J|j)(an|anuary))|((F|f)(eb|ebruary))|((M|m)(ar|arch))|((A|a)(pr|pril))|((M|m)ay)|((j|j)(un|une))|((J|j)(ly|uly))|((A|a)(ug|ugust))|((S|s)(sep|eptember))|((O|o)(ct|ctober))|((N|n)(ov|ovember))|((D|d)(ec|ecember))))[ /.-]((\d{1,2})|(\d{4})) \d{1,2}:\d{1,2} GMT(\+|-)\d{1,2}:\d{1,2} \w*')

#On Wed, Jan 23, 2013 at 10:18 PM, Meier, Bryan <Bryan.Meier@oldcastle.com> wrote:
# TRAIL_WITH_ON_WORD = rc('^((O|o)n)( |)((((M|m)(onday|on))|((T|t)(uesday|ue))|((W|w)(ednesday|ed))|((T|t)(hursday|hu))|((F|f)(riday|ri))|((S|s)(aturday|st))|((S|s)(unday|un))),|)( |)((\d{1,2})|(\d{4}))[ /.-]((\d{1,2})|(((J|j)(an|anuary))|((F|f)(eb|ebruary))|((M|m)(ar|arch))|((A|a)(pr|pril))|((M|m)ay)|((j|j)(un|une))|((J|j)(ly|uly))|((A|a)(ug|ugust))|((S|s)(sep|eptember))|((O|o)(ct|ctober))|((N|n)(ov|ovember))|((D|d)(ec|ecember))))[ /.-]((\d{1,2})|(\d{4}))')
TRAIL_WITH_ON_WORD = rc('^((O|o)n)( |)((((M|m)(onday|on))|((T|t)(uesday|ue))|((W|w)(ednesday|ed))|((T|t)(hursday|hu))|((F|f)(riday|ri))|((S|s)(aturday|st))|((S|s)(unday|un))),|)( |)((\d{1,2})|(\d{4})|(((J|j)(an|anuary))|((F|f)(eb|ebruary))|((M|m)(ar|arch))|((A|a)(pr|pril))|((M|m)ay)|((J|j)(un|une))|((J|j)(ly|uly))|((A|a)(ug|ugust))|((S|s)(sep|eptember))|((O|o)(ct|ctober))|((N|n)(ov|ovember))|((D|d)(ec|ecember))))[ .\- ]((\d{1,2})|(((J|j)(an|anuary))|((F|f)(eb|ebruary))|((M|m)(ar|arch))|((A|a)(pr|pril))|((M|m)ay)|((J|j)(un|une))|((J|j)(ly|uly))|((A|a)(ug|ugust))|((S|s)(sep|eptember))|((O|o)(ct|ctober))|((N|n)(ov|ovember))|((D|d)(ec|ecember))))[ .\-,](| )((\d{1,2})|(\d{4}))')

'''
From: Gimblett, Jonathan
Sent/Date: Wednesday, December 02, 2015 12:32 PM
To: Prieto, Sayra >
Cc: Kraak-Weggemans, Anita >; Driessen, Pieter-Jan >
Subject: Fwd: Invoices
'''
TRAIL_WITH_FROM_TO = rc('^(\*|)(((F|f)rom:)|((S|s)en(t|d):)|((D|d)ate:)|((T|t)o:)|((C|c)c:)|((B|b)cc:)|((S|s)ubject:)|((I|i)mportance:))')