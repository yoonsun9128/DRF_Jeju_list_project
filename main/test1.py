from django.shortcuts import render

# Create your views here.
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pprint import pprint
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm
from django.conf import settings
import time
from main.models import Store, Tags, Reviews
# 포문 하나로 뭉친거
def GetStoreId():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-shm-usage")

        # df = pd.read_csv('main/jejulist.csv', encoding='cp949')
    df1 = pd.read_csv('main/jejulist.csv', encoding='utf-8')
    df = df1.head(1)

    jeju_store = df[['업소명','소재지','메뉴']]
    print(jeju_store.head())
    jeju_store.columns = [ 'name','address','menu']

    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    jeju_store['kakao_keyword'] = jeju_store['address'] # "%20"는 띄어쓰기를 의미합니다.

    # 상세페이지 주서 따기
    # store_info = []
    for i, keyword in enumerate(jeju_store['kakao_keyword'].tolist()):
        print("이번에 찾을 키워드 :", i, f"/ {df.shape[0] -1} 행", keyword)
        kakao_map_search_url = f"https://map.kakao.com/?q={keyword}"

        driver.get(kakao_map_search_url)
        time.sleep(1)
        df.iloc[i,-1] = driver.find_element(By.CSS_SELECTOR,"#info\.search\.place\.list > li > div.info_item > div.contact.clickArea > a.moreview").get_attribute('href')

        url = df.iloc[i,-1]
        store_id = url.split('/')[-1]
        store = Store(store_id=store_id)

        driver.get(url)
        time.sleep(2)
        # review = Reviews(content=review_info['contents'])
        review_info = {
            'store': '',
            'star': '',
            'address':''
        }
        tags_list = {
            'name':[],
        }
        review_list = {
            'content':[]
        }
        review_model = Reviews()
        tag_model = Tags()
        review_info['star'] = driver.find_element(By.CLASS_NAME,"ahead_info").find_element(By.CLASS_NAME,"grade_star").find_element(By.CLASS_NAME, "num_rate").text
        review_info['store'] = driver.find_element(By.CLASS_NAME,"inner_place").find_element(By.CLASS_NAME,"tit_location").text
        review_info['address'] = driver.find_element(By.CLASS_NAME,"location_detail").find_element(By.CLASS_NAME,"txt_address").text
        reviews = driver.find_element(By.CLASS_NAME,"list_evaluation").find_elements(By.TAG_NAME, "li")
        for review in reviews:
            review_content = {}
            review_tags = set()
            if not review.text : #or driver.find_element(By.CLASS_NAME,"group_likepoint").find_elements(By.TAG_NAME, "span"):
                continue
            try:
                tags = review.find_element(By.CLASS_NAME, "group_likepoint").find_elements(By.TAG_NAME, "span")
                review_tags = [x.text for x in tags]
            except NoSuchElementException:
                review_tags = None
            try:
                review_content = review.find_element(By.CLASS_NAME, "txt_comment").text
            except NoSuchElementException:
                # 식별값(있지만 없어도 되는 값)
                review_content = None
            review_list['content'].append(review_content)
            tags_list['name'].append(review_tags)

        print(review_info)

        tag_model.name = tags_list
        review_model.content = review_list['content']
        store.star = review_info['star']
        store.save()
        review_model.store = store
        tag_model.save()
        review_model.save()

        # 태그만 먼저 뽑아내서 중복 삭제 태그에 저장
        # 태그의 아이디로 리뷰 저장

GetStoreId()