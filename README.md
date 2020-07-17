# coala2
sample.xlsx 는 테스트용 샘플 리뷰 데이터  
stopwords.xlsx 는 한국어 불용어 사전  
userdict.txt 고유명사, 신조어 등을 새로 등록  
pos_table.txt 분석대상 품사를 등록  

<전처리>  
공백, 문장부호 등 제거  
형태소 기준 토큰화 (문장을 단어로 쪼개기)  
불필요한 품사 제외   
불용어 제거  
정수 인코딩 (TF-IDF 방식 이용)  
인코딩된 행렬에 좋아요 수, 이웃 수 등의 열 추가  

<모델링>  
랜덤포레스트,  
나이브베이즈 모델 작동 확인됨

1. 전처리 모듈화: 모델 실험하기 쉽게 modules, module_preprocessing 제작
1-1. 제품군별로 하나의 df로 합치기: modules의 append 함수
1-2. 제품군별로 인코딩까지 끝내 matrix로 저장하기: module_preprocessing의 preprocessing 함수
1-3. 인코딩 과정에서 만들어진 tfid 저장하기
