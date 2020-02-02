#!/usr/bin/env python
# coding: utf-8

# In[321]:


import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import nltk
import re
import string
import json
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from bs4 import BeautifulSoup
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from gensim.models import word2vec
import sys
who=sys.argv[1]
answer=keywords(who)
jans = json.loads(answer)
print(json.dumps(jans))

#print (jans)
# from gensim.models.phrases import Phrases


# In[581]:
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import csv


def webcrawler(category):
    cname=category
    csv_file = open(r'C:\Users\manan\Desktop\Data.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Companies_worked_for', 'School_attended', 'Job_titles_held' , 'Degrees', 'Skills','R_Link'])

    driver=webdriver.Chrome("C:\Program Files\Selenium Driver\chromedriver")
    driver.get("https://www.livecareer.com/resume-search/")

    list2 = [cname]
    list3 = []
    companies=[]
    schools=[]
    jobs=[]
    degrees=[]
    skills=[]
    links=[]


    for x in list2:
        driver.find_element_by_id("txtJobTitle").send_keys(x)
        driver.find_element_by_id("btnFind").click() 
        k=1
        while(k<9):
            m=str(k)
            URL="https://www.livecareer.com/resume-search/search?jt=java&pg="+m
            driver.get(URL)
            k=k+1
            page=requests.get(URL)
            soup=BeautifulSoup(page.text,"html.parser")
            list3=[]
            for link in soup.find_all('a', href=True):
                string=link['href']
                if(string!="javascript:void(0);" and string!="javascript:void(0)"):
                    if "java" in string:
                        list3.append(string)
                y=1
                for y in list3:
                    companies=[]
                    schools=[]
                    jobs=[]
                    degrees=[]
                    skills=[]
                    links=[]
                    URL2="https://www.livecareer.com/"+y
                    driver.get(URL2)
                    page=requests.get(URL2)
                    soup=BeautifulSoup(page.text,"html.parser")
                    first = driver.find_elements_by_xpath("//div[@class = 'row font14']")
                    second = driver.find_elements_by_xpath("//div[@class = 'row font14 mt10']")
                    third = driver.find_elements_by_xpath("//td[@class = 'field twocol_1']")
                    c=""
                    for first1 in first:
                        c+=first1.text
                    i=c.find("Companies Worked For:")
                    j=c.find("School Attended")
                    company=c[i+21:j]
                    school=c[j+15:]
                    c=""
                    for second1 in second:
                        c+=second1.text
                    i=c.find("Job Titles Held:")
                    j=c.find("Degrees")
                    job=c[i+16:j]
                    degree=c[j+7:]
                    c=""
                    for third1 in third:
                        c+=third1.text
                    skill=c
                    companies.append(company)
                    schools.append(school)
                    jobs.append(job)
                    degrees.append(degree)
                    skills.append(skill)
                    links.append(URL2)
                    csv_writer.writerow([companies,schools,jobs,degrees,skills,links])
                list3=[]


sentences=pd.read_csv(r"C:\Users\manan\Desktop\Data.csv'", encoding='ISO-8859-1')


# In[582]:


sentences.head()


# In[583]:


# category=[]
# for i in range(len(sentences)):
#     category.append('Educator')

# len(category)
# sentences['Category']=category


# In[584]:


# for i in lines.Category.unique():
#     print(i)


# In[585]:


# preprocessing 

sentences.Skills=sentences.Skills.astype(str)
sentences.Skills=sentences.Skills.apply(lambda x : re.sub("\\n", " ", x))
sentences.Skills=sentences.Skills.apply(lambda x : re.sub("\\\\n", " ", x))
sentences.Skills=sentences.Skills.apply(lambda x: BeautifulSoup(x).get_text())
sentences.Skills=sentences.Skills.apply(lambda x : re.sub("[^a-zA-Z]", " ", x))
sentences.Skills=sentences.Skills.apply(lambda x: x.lower())
stop_words = stopwords.words('english')
print(stop_words)
[word for word in test.Skills if word not in stop_words]


# In[586]:


# sentences.Skills


# In[587]:


from nltk import word_tokenize
sentences.Skills=sentences.Skills.apply(lambda x : word_tokenize(x))


# In[588]:


# print(sentences.Skills)
# lines.dropna(inplace=True)


# In[589]:


# lines=sentences
lines=lines.append(sentences, ignore_index=True)


# In[590]:


#lines


# In[591]:


test=lines
test = test.sample(frac=1).reset_index(drop=True)
test.Skills=test.Skills.astype(str)
test.Skills=test.Skills.apply(lambda x : re.sub("\[\]", "", x))
test


# In[592]:


test=test[test.Skills!='']
        


# In[593]:


# print(test.Skills)
test.reindex(i for i in range(len(test)))
#test


# In[594]:




# In[595]:


fl=[]
for item in test.Skills:
    
    item=item[2:-2]
    item=re.sub("', '", " ", item)
     
    li = list(item.split(" "))
    
    fl.append(li)


# In[596]:


# print(fl)


# In[597]:


num_features=400
min_word_count=500
min_workers=1
context=10
downsampling=1e-4



    
model=word2vec.Word2Vec(fl, workers=min_workers, size=num_features, window=context, sample=downsampling)
model.init_sims(replace=True)
model_name='Resume_details'
model.save(model_name)


# In[598]:


model.doesnt_match("python java z boy".split())
Xx = list(model.wv.vocab)
#print(Xx)


# In[614]:


data=model.wv.most_similar('java')
#print(data[1][1])


# In[600]:


Encoder=LabelEncoder()
yy=Encoder.fit_transform(test.Category)


# In[601]:


X_train, X_test, y_train, y_test = train_test_split(test['Skills'], yy, test_size=0.2)
# mod=XGBClassifier()
# mod.fit(X_train, y_train)
# y_pred=mod.predict(X_test)
# accuracy=accuracy_score(y_test, y_pred)


# In[602]:


from sklearn.feature_extraction.text import TfidfVectorizer

Tfidf_vect=TfidfVectorizer(max_features=1000)
Tfidf_vect.fit(test['Skills'])

x_train_tfidf=Tfidf_vect.transform(X_train)
x_test_tfidf=Tfidf_vect.transform(X_test)


# In[603]:


# import pickle 

# saved_model = pickle.dumps(mod) 
# model_from_pickle = pickle.loads(saved_model) 
# model_from_pickle.predict(X_test) 


# In[604]:


#print(x_train_tfidf)


# In[605]:


from sklearn import svm

SVM=svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
svm1=SVM.fit(x_train_tfidf, y_train)

SVM_predictions=svm1.predict(x_test_tfidf)

predictions = [round(value) for value in SVM_predictions]


# In[606]:


#print("Accuracy score:", accuracy_score(predictions, y_test))


# In[464]:


#predictions


# In[607]:


test.to_csv('../resume_classification_dataset.csv', index=False)


# In[608]:


from sklearn.externals import joblib

filename = 'finalized_model.sav'
joblib.dump(SVM, filename)


# In[609]:


def keywords(text):
    data=model.wv.most_similar(text)
    res={i : data[i] for i in range(0, len(data), 5)}
    return data


# In[611]:





# In[612]:


#import json

#print(json.dumps(answer))


# In[ ]:

