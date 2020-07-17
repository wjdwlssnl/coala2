#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import re
import joblib
from konlpy.tag import *
from modules import *
from sklearn.feature_extraction.text import TfidfVectorizer


# In[5]:


def preprocessing(df_a, matrixname):
    # 사용자 사전
    komoran=Komoran(userdic='userdict.txt')
    
    # 전체 행에서 불필요 텍스트 제거
    print('cleaning...')
    df_a['content']=df_a.content.apply(cleaning)
    
    # 토큰화 시작
    print('tokenizing...')
    
    # 전체 행에 품사 부착 -> 각 행은 ('word', '품사') 튜플의 리스트 <-오래걸림 
    df_a['content']=df_a.content.apply(komoran.pos)
    
    # 전체 행에 품사추출함수 적용
    df_a['content']=df_a.content.apply(PosPicker)

    # 전체 행을 다시 형태소 리스트로 변환
    df_a['content']=df_a.content.apply(komoran.morphs)
    
    # 전체 행에 불용어 제거 함수 적용
    print('erasing stopwords...')
    df_a['content']=df_a.content.apply(DelStops)
    
    # 전체 행에 대해 문장화 적용
    df_a.content=df_a.content.apply(wordjoin)
    
    # 인코딩 시작
    print('encoding...')
    
    # TFID 생성
    tfid=TfidfVectorizer()

    # 문장 벡터화 (TFID)
    tfid.fit_transform(df_a.content)
    print("number of encoded features :", len(tfid.get_feature_names()))

    # matrix로 저장 (TFID) -> 문장 수 * 단어 수 크기의 matrix가 생성된다
    feature_matrix2=tfid.transform(df_a.content)
    print("dimension of feature_matrix :",feature_matrix2.shape)
    
    # tfid 저장
    tfidname="tfid/"+matrixname+".pkl"
    joblib.dump(tfid, tfidname)
    print(tfidname,"is saved")    

    # matrix에 img, sticker, video, tags 열을 추가
    print("adding columns...")
    new_matrix=np.zeros((feature_matrix2.shape[0], feature_matrix2.shape[1]+4))

    new_matrix[:,:-4]=feature_matrix2.toarray()
    new_matrix[:,-4]=df_a.img
    new_matrix[:,-3]=df_a.sticker
    new_matrix[:,-2]=df_a.video
    new_matrix[:,-1]=df_a.tags

    print("4 columns added successfully :", new_matrix.shape)
    
    #matrix 저장
    filename="matrix/"+matrixname
    np.save(filename, new_matrix)
    print(filename,"is saved")
    
    #return
    return new_matrix


# In[ ]:




