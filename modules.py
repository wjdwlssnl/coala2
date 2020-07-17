#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re
from konlpy.tag import *


# In[2]:


# 두 csv 하나로 합치는 append 함수 정의 
def append(df1, df2, filename):
    # NaN 행 제거
    print("appending...")
    df1=df1.dropna(axis=0) 
    df2=df2.dropna(axis=0) 

    print("df1.shape : ",df1.shape)
    print("df2.shape : ",df2.shape)

    # 광고, 후기 하나로 합치기
    df=pd.concat([df1,df2],axis=0)

    # 중복 행, content가 비어있는 행 제거
    df=df.drop_duplicates()
    df.head()

    # 불필요한 열 : num, widget 제거
    df_a=df.drop(['num','widget'],axis=1)
    y_data=np.array(df.isad.tolist()) #종속변수 isad

    # 합쳐진 dataframe 저장
    path="appended/"+filename+".csv"
    df_a.to_csv(path, header=True, index=False)
    
    #return
    return df_a


# In[3]:


#전처리 함수 정의: 문장을 IN
def cleaning(x):
    x=re.sub('<(/)?([a-zA-Z0-9]*)(\\s[a-zA-Z0-9]*=[^>]*)?(\\s)*(/)?>',' ',x) #html 태그 제거
    x=re.sub('\W', ' ', x) #특수문자 제거
    x=re.sub('([ㄱ-ㅎㅏ-ㅣ]+)', ' ', x) #한글 자음 모음 제거
    x=re.sub('\d','', x) #번호 제거
    x=x.replace('SE TEXT','')
    x=x.replace('원고료', '') #상세검색 mustin키워드 제거
    x=x.replace('소정', '')
    x=x.replace('내돈', '') 
    return x


# In[4]:


# 품사 추출 함수 정의; 품사가 부착된 리스트를 IN
def PosPicker(sentence):
    clean_words=[]
    #품사 리스트를 함수 내에서 불러오자
    pos=pd.read_csv('pos_table.txt', header=None, names='p')
    poslist=pos.p.tolist()
    for word in sentence:
        if word[1] in poslist: # 품사가 분석대상 리스트에 있으면
            clean_words.append(word[0]) # 해당 단어를 clean_words에 추가한다
    x=' '.join(clean_words)
    return x


# In[5]:


# 불용어 제거 함수 정의: 형태소 기준으로 나뉜 리스트를 IN 
def DelStops(sentence): 
    result=[]
    # 불용어 리스트도 함수 내에서 불러오자
    stopwords=pd.read_excel("stopwords.xlsx")
    stoplist=np.array(stopwords.words.tolist())
    for word in sentence:
        if word not in stoplist:
            result.append(word)
    return result


# In[6]:


# 단어 리스트를 한 문장으로 합치는 함수 정의 : 단어 리스트 IN
def wordjoin(x):
    return ' '.join(x)


# In[ ]:




