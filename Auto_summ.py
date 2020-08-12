# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 00:08:19 2020

@author: subham
"""
#importing libraries
try:
    import requests
    from bs4 import BeautifulSoup
    import re
    import nltk
    import heapq
except:
    print("Error while loading the Libraries")

#fetching the data from the link
topic="Elon_Musk"
url="https://en.wikipedia.org/wiki/{}".format(topic)
page=requests.get(url)

#checking connection
print("Connected {} ".format(page.status_code==200))
soup=BeautifulSoup(page.text, 'html.parser')
data=soup.findAll('p')

#collecting all the text in p tag
data_text=''
for index in data:
    data_text += index.text

#removing the values like [9][10] from data_text
data_text=re.sub(r'\[[0-9]*\]',' ',data_text)

#removing all the space
data_text=re.sub(r'\s+',' ',data_text)

#creating tokens for words
sentence_token=nltk.sent_tokenize(data_text)

#removing all numeric value
data_text=re.sub(r'[^a-zA-z]',' ',data_text)

#removing all the space
data_text=re.sub(r'\s+',' ',data_text)

#creating tokens for words
word_token=nltk.word_tokenize(data_text)

#getting the stopwords from ntkl.corpus library
stopwords=nltk.corpus.stopwords.words('english')

#iterating word frequency
word_freq={}

for index in word_token:
    if index not in stopwords:
        if index not in word_freq.keys():
            word_freq[index]=1
        else:
            word_freq[index]+=1
            
#scaling down the freq
max_value=max(word_freq.values())
for index in word_freq.keys():
    word_freq[index]=word_freq[index]/max_value
    
#iterating sentence 
sentence_freq={}
for index in sentence_token:
    for index_1 in nltk.word_tokenize(index.lower()):
        if index_1 in word_freq.keys():
            if(len(index.split(" ")) < 25):
                if index not in sentence_freq.keys():
                    sentence_freq[index]=word_freq[index_1]
                else:
                    sentence_freq[index]+=word_freq[index_1]
                    
summary=heapq.nlargest(10,sentence_freq , key=sentence_freq.get)
print(summary)