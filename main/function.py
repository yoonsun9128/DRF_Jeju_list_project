import pandas as pd
from tqdm import tqdm_notebook
import re
from urllib.request import urlopen
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Store

stores = pd.read_csv('main/storedata.csv', encoding='UTF-8')

# head() 안에 숫자를 넣지 않으면 5개만 나온다
# stores = stores.head()
stores['합침'] = (stores['store_name']) + (stores['content'])
# print(stores['합침'][0])
#결측값을 빈 값으로 대체
stores['합침'] = stores['합침'].fillna('')
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(stores['content'])
# print('TF-IDF 행렬의 크기(shape):',tfidf_matrix.shape)

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
# print('코사인 유사도 연산 결과 :',cosine_sim.shape)

# 순서를 부여
indices = pd.Series(stores.index, index=stores['store_name']).drop_duplicates()
# print(indices.head())

# 가게 인덱스 값 확인하기
title_to_index = dict(zip(stores['store_name'], stores.index))
# print("두번째",title_to_index)
idx = title_to_index['풍천만가']
# print(idx)

def get_recommendations(title, cosine_sim=cosine_sim):
    # 선택한 영화의 타이틀로부터 해당 영화의 인덱스를 받아온다.
    idx = title_to_index[title]
    print(idx)

    # 해당 영화와 모든 영화와의 유사도를 가져온다.
    sim_scores = list(enumerate(cosine_sim[idx]))
    print("함수",sim_scores)

    # 유사도에 따라 영화들을 정렬한다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    print("함수2",sim_scores)

    # 가장 유사한 10개의 영화를 받아온다.
    sim_scores = sim_scores[1:10]
    print("함수3",sim_scores)

    # 가장 유사한 10개의 영화의 인덱스를 얻는다.
    store_indices = [idx[0] for idx in sim_scores]
    print("함수4",store_indices)

    # 가장 유사한 10개의 영화의 제목을 리턴한다.
    print(stores['store_name'].iloc[store_indices])

# get_recommendations('풍천만가')