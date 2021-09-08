# -*- coding: utf-8 -*-

#from talon.trailmail.start import extract
#from util.utils.helper import binary_regex_search
from classification.email.trailmail import ORIGINAL_MESSAGE_WORD, FORWARDED_MESSAGE_WORD, BEGIN_FORWARDED_MESSAGE, TRAIL_WITH_MESSAGE_FROM_WORD, TRAIL_WITH_SENT_DATE, TRAIL_WITH_FROM_TO
from start import extract

body = """  

 
Thanks & regards,
Hitesh N. Patel
 
From: Meier, Bryan [mailto:Bryan.Meier@oldcastle.com] 
Sent: 28 March 2013 08:08
To: Rahul Jain
Cc: Hitesh Patel
Subject: RE: Kwik Tag Functionality
 
1.       I removed Ps as that was a duplicate of PsKey.

2.       Yes, the name will be the filename minus the extension.

3.       Yes this is the location of the file on our end. We can use a UNC path to the file right?

5.       I added the letter A to the beginning of the key.

 
Below is a screenshot of what the file will now look like with the given changes.

 
Bryan Meier
Oldcastle Precast | Software Engineer | w: 253.876.2329 | c: 253.495.7202 | f: 866.608.4903
 
From: Rahul Jain [mailto:rahul.jain@akritiv.com] 
Sent: Thursday, March 28, 2013 3:38 AM
To: Meier, Bryan
Cc: Hitesh Patel
Subject: Re: Kwik Tag Functionality
 
Hi Bryan,
 
Thank you for sending the files
 
Below are my comments on the Packing Slip file
1)      PSkey and Ps are two different column in file with same data . Can we remove one column ?
 
2)      Name column in file is Image name am I right ?
 
3)     Body Column in file should have the path (e.g: D:\PackingSlips\410SP091834-410119406.pdf) where the image stored on the local machine will be loaded by Old Castle into Akritiv using the data loader.
 
4)      Folder Id  - This will be given by Akritiv this will be common for every record in the Packing Slip File
 
5)      In the present file packing slip key starts with the number- Can you please update and start with any letter(As per the screen shot below I have added “A” before your packing key)
 
Present pskey
Required pskkey
410SP091834
A410SP091834
410SP091835
A410SP091835
410SP091836
A410SP091836
410SP091837
A410SP091837
410SP091838
A410SP091838
410SP091839
A410SP091839
410SP091840
A410SP091840
410SP091841
A410SP091841
410SP091842
A410SP091842
410SP091843
A410SP091843
 
 
Please let us know your feedback
 
Thank You,
Rahul Jain
Akritiv Technologies
 
On Wed, Mar 27, 2013 at 9:55 PM, Meier, Bryan <Bryan.Meier@oldcastle.com> wrote:
Here you go…
 
Bryan Meier
Oldcastle Precast | Software Engineer | w: 253.876.2329 | c: 253.495.7202 | f: 866.608.4903
 
From: Rahul Jain [mailto:rahul.jain@akritiv.com] 
Sent: Wednesday, March 27, 2013 9:04 AM

To: Meier, Bryan
Subject: Re: Kwik Tag Functionality
 
Hi Bryan,
 
Could you please dial below conference number i have opened the bridge 
 
US - 8552251637 Code - 9157658743
 
 
 
On Wed, Mar 27, 2013 at 9:26 PM, Meier, Bryan <Bryan.Meier@oldcastle.com> wrote:
I am available for the next couple hours. Give me a call in the office when you are ready.
 
Bryan Meier
Oldcastle Precast | Software Engineer | w: 253.876.2329 | c: 253.495.7202 | f: 866.608.4903
 
From: Rahul Jain [mailto:rahul.jain@akritiv.com] 
Sent: Wednesday, March 27, 2013 8:54 AM
To: Meier, Bryan

Subject: Re: Kwik Tag Functionality
 
Hi Bryan,
 
Thank you for the information !!
 
We have a few questions in terms of file and would like to discuss with you 
 
Could you please confirm what time are you available today so i can share the call details
 
Thank You
 
Rahul Jain
 
On Wed, Mar 27, 2013 at 2:49 AM, Meier, Bryan <Bryan.Meier@oldcastle.com> wrote:
I have completed the job to do the pulling from KwikTag, converting the TIFF files to PDF, and finally create the CSV file. So I am ready for the data loader for this project whenever you are ready.
 
Bryan Meier
Oldcastle Precast | Software Engineer | w: 253.876.2329 | c: 253.495.7202 | f: 866.608.4903
 
From: Rahul Jain [mailto:rahul.jain@akritiv.com] 
Sent: Wednesday, March 20, 2013 12:05 PM

To: Meier, Bryan
Cc: Tushar Kothare (tushar.kothare@akritiv.com); Nolan, Josh; Hitesh Patel
Subject: Re: Kwik Tag Functionality
 
Hi Bryan,
 
Yes , you can delete the "Packing Slip Name" coloumn from CSV.
 
We would use Image name as Packing Slip Name- Since its a mandatory coloumn to load the data
 
Thank You
 
Rahul Jain
 
On Wed, Mar 20, 2013 at 10:58 PM, Meier, Bryan <Bryan.Meier@oldcastle.com> wrote:
We don’t name our packing slips. So, can we just leave it blank?
 
Bryan Meier
Oldcastle Precast | Software Engineer | w: 253.876.2329 | c: 253.495.7202 | f: 866.608.4903
 
From: Rahul Jain [mailto:rahul.jain@akritiv.com] 
Sent: Wednesday, March 20, 2013 10:27 AM
To: Meier, Bryan
Cc: Tushar Kothare (tushar.kothare@akritiv.com); Nolan, Josh; Hitesh Patel

Subject: Re: Kwik Tag Functionality-
 
 
Hi Bryan,
Packing Slip # is nothing but Packing Slip Name -( I have also change in the format below)
Packing Slip Key is Unique Identifier 
Please let us know if you need any additional information from us
 
Thank You
 
Rahul Jain
 
 
On Wed, Mar 20, 2013 at 10:45 PM, Meier, Bryan <Bryan.Meier@oldcastle.com> wrote:
I have question about the CSV file for this project.  According to the document that was sent the CSV file should look like what I have below. What would be the difference between the Packing Slip Key and the Packing Slip #? To us, these are one in the same.
 
Source
Batch#
Packing Slip Key
Invoice Key
Packing Slip Name
Folder ID
Name
Body
Type
AX
02022013
P00001
A00001
P1
A01900
Logo
C:\logo.png
png
 
 
Bryan Meier
Oldcastle Precast | Software Engineer | w: 253.876.2329 | c: 253.495.7202 | f: 866.608.4903
 
From: Nolan, Josh 
Sent: Tuesday, March 12, 2013 2:10 PM
To: Rahul Jain; Jaeger, Cindy
Cc: Meier, Bryan; Tushar Kothare (tushar.kothare@akritiv.com)
Subject: RE: Kwik Tag Functionality
 
Rahul,
After our call today I had some time to think about and discuss with my team. We can discuss in more detail tomorrow to help give you a better understanding of how we are expecting this functionality to work. As for the image format of the packing slips we feel it would be best from our customer’s standpoint to have the files converted into a PDF format. This reduce the number of calls or complaints we get from our customers saying they can’t open an attached TIFF file.
 
Again, thanks for your time and I look forward to discussing this in more detail tomorrow.
 
Joshua T. Nolan, CCE
Director of Credit Management
Oldcastle Precast, Inc.
P: (253) 561-0496 C: (253) 326-6168 F: (866) 713-6830
 
From: Rahul Jain [mailto:rahul.jain@akritiv.com] 
Sent: Monday, March 11, 2013 10:18 AM
To: Nolan, Josh; Jaeger, Cindy
Subject: Kwik Tag Functionality
 
Hi Josh,
 
Further to our conversation on Friday regarding Kwik Tag Functionality.
 
Please find the attached document.
 
Let us know your feedback
 
Thanks And Regards
 
Rahul Jain
Akritiv Technologies


 
-- 
Thanks And Regards
 
Rahul Jain
Akritiv Technologies


 
-- 
Thanks And Regards
 
Rahul Jain
Akritiv Technologies


 
-- 
Thanks And Regards
 
Rahul Jain
Akritiv Technologies


 

-- 
Thanks And Regards
 
Rahul Jain
Akritiv Technologies


 
-- 
Thanks And Regards
 
Rahul Jain
Akritiv Technologies"""

data = extract(body) 
print len(data)
for d in data:
    print d
    print "--------------------------------------------------------"


'''
print binary_regex_search(ORIGINAL_MESSAGE_WORD)("-----Original Message-----")
print binary_regex_search(FORWARDED_MESSAGE_WORD)("-----Original Message-----")
print binary_regex_search(BEGIN_FORWARDED_MESSAGE)("-----Original Message-----")
print binary_regex_search(TRAIL_WITH_MESSAGE_FROM_WORD)("-----Original Message-----")
print binary_regex_search(TRAIL_WITH_SENT_DATE)("-----Original Message-----")
print binary_regex_search(TRAIL_WITH_FROM_TO)("-----Original Message-----")
'''
