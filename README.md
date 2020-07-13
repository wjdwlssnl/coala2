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
