"# Email-Classification-MLH" 
The project has two main modules. One is the testing based Flask Restful application for email classification. Whereas the other is producion based (Salesforce) Django Rest API. The third RASA approach was used initially for testing purposes


The project can be overall broadly divided into three parts:
1. Data cleaning and processing:
It has around 80-100 different functions of nltk and regex to remove stopwords, signature and trailmail from data as it can be classified as noise. 

2. Modelling:
Subsequently the data passes through the two different models that I test - 1. Google Auto ML 2. Rasa NLU for categorizing the mails. 

3. Building REST API:
The whole REST API has been made in two ways: 1. Flask for testing purpose 2. Django for production purpose.

Also, in the production phase, database connection is required for Salesforce where I am using Postgressql and certain frameworks like Tabula to extract the data from mails and check them with the actual database using fuzzy logic as the incoming mails can be dynamically of any style. Finally for basic testing, the project is deployed on Heroku and for production, it is deployed on AWS

P.S. This project is one of the five projects I during my 2 years tenure at Sailfin Technologies and contains some confidential information of data which has been removed. Kindly excuse.
