# -*- coding: utf-8 -*-

from classification.email.signature.start import extract

body = "Hi Tom,\r\nkafsdlfjldsjf;l s;dfks;lkfl;dskf;kl;eewesds\r\nuriewuroiweuroweuin skdjf skjddfsd kjdf kjjsdf kjdkfjkasdsjfkl kjsdklf\r\njfdklsjflsd sdfdsdddgfd sdfsddv ga ad zdsddf efdsds\r\nMany thanks\r\nAndrea\r\nAndrea Jenkinson, Administrative Assistant\r\nPrologis | Local partner to global tradeTM\r\nPrologis House | 1 Monkspath Hall Road | Solihull | West Midlands B90 4FY | UK\r\nDirect +44 121 224 8700 | email ajenkinson@prologis.com"
#body = "Please check\r\nThanks,\r\nMitul"
#body = "Thanks Tom,\r\nkafsdlfjldsjf;l s;dfks;lkfl;dskf;kl;eewesds\r\nuriewuroiweuroweuin skdjf\r\nThank you in advance.\r\nKind regards,\r\nMariola Iwaniuk\r\nPrologis Germany Management GmbH Peter-Müller-Straße 16 | 40468 Düsseldorf (Airport City) | Germany"
#body = "Hi jack,\r\n1 jfklsdj sdflksjkl lkjflksdf kjflk\r\n2 lskfj sdflkj sdfk jkj kjf fjsdf\r\n3 ksdlfom jsdkfj ksjdf jfksd\r\n4 dkfjslkjf sdkdjfkls klsjdflk dlkfj\r\n5 slkdjflks skldjfdlksf sklsdldjfl lksdjfl\r\n6 lkdsjf kdskfj lskdsjflk sldkdfjls sdlksdfj slksdjf\r\n7 kldfjnkdjf kdjf dfjkdf sifsd nskdjf sdfjklsdld jk kjlk\r\nBest regards,\r\nBea\r\nBeatrice Burzlaff, Assistant Northern Germany\r\nPrologis | Local partner to global tradeTM\r\nPrologis Germany Management GmbH | Heykenaukamp 10 | 21147 Hamburg | Germany\r\nDirect +49 211 542 310 39 | Mobile +49 173 542 13 27 | Fax +49 40 49 21 93 95\r\nbburzlaff@prologis.com | www.prologisgermany.com"
#,'Jenkinson.Andrea@gmail.com'
#Andrea Jenkinson
#Meier, Bryan <Bryan.Meier@oldcastle.com>
#Jenkinson, Andrea <Andrea.Jenkinson@gmail.com>
#Mariola.Iwaniuk@gmail.com
data = extract(body.splitlines(),'Jenkinson, Andrea <Andrea.Jenkinson@gmail.com>')
#data = extract(body.splitlines(),'Mariola Iwaniuk')
#data = extract(body.splitlines(),'Beatrice Burzlaff')
print 'Result = '+str(data)