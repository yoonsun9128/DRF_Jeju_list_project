import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm
import time
from main.models import Store

# 포문 하나로 뭉친거
def GetStoreId():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-shm-usage")
        # df = pd.read_csv('main/jejulist.csv', encoding='cp949')

    df = pd.read_csv('main/jejulist.csv', encoding='utf-8')

    jeju_store = df[['업소명','소재지']]
    jeju_store.columns = [ 'name','address']

    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    jeju_store['kakao_keyword'] = jeju_store['address'] + "%20" + jeju_store['name'] # "%20"는 띄어쓰기를 의미합니다.

    for i, keyword in enumerate(jeju_store['kakao_keyword'].tolist()):
        print("이번에 찾을 키워드 :", i, f"/ {df.shape[0] -1} 행", keyword)
        kakao_map_search_url = f"https://map.kakao.com/?q={keyword}"
        driver.get(kakao_map_search_url)
        time.sleep(2)
        try:
            df.iloc[i,-1] = driver.find_element(By.CSS_SELECTOR,"#info\.search\.place\.list > li > div.info_item > div.contact.clickArea > a.moreview").get_attribute('href')
        except NoSuchElementException:
            continue
        url = df.iloc[i,-1]
        store_id = url.split('/')[-1]
        store = Store(store_url=store_id)
        driver.get(url)

        time.sleep(2)
        # review = Reviews(content=review_info['contents'])
        review_info = {
            'store_name': [],
            'star': '',
            'content': [],
            'img': [],
            'address':''
        }
        # tags_list = {
        #     'name':[],
        # }
        # tag_model = Tags()
        review_info['store_name'] = driver.find_element(By.CLASS_NAME, "inner_place").find_element(By.CLASS_NAME, "tit_location").text
        try:
            review_info['address'] = driver.find_element(By.CLASS_NAME,"details_placeinfo").find_element(By.CLASS_NAME,"placeinfo_default").find_element(By.CLASS_NAME,"txt_address").text
        except NoSuchElementException:
            continue

        try:
            review_info['star'] = driver.find_element(By.CLASS_NAME,"ahead_info").find_element(By.CLASS_NAME,"grade_star").find_element(By.CLASS_NAME, "num_rate").text
        except NoSuchElementException:
            review_info['star'] = None
        try:
            image = driver.find_element(By.CLASS_NAME, "photo_area").find_element(By.CLASS_NAME, "link_photo").get_attribute("style").split('"')[1]
            review_info['img'] = image
        except NoSuchElementException:
            review_info['img'] = None

        try:
            reviews = driver.find_element(By.CLASS_NAME,"list_evaluation").find_elements(By.TAG_NAME, "li")
        except NoSuchElementException:
            continue
        try:
            while True:
                more_button = driver.find_element(By.CLASS_NAME,"link_more")
                if "접기" in more_button.text:
                    break
                more_button.click()
        except BaseException:
            pass

        for review in reviews:
            review_content_str = {}
            if not review.text :
                continue
            try:
                review_content = review.find_element(By.CLASS_NAME, "txt_comment").text
                result = ''.join(s for s in review_content)
                review_content_str = result.replace("\n", "")
            except NoSuchElementException:
                # 식별값(있지만 없어도 되는 값)
                review_content_str = None
            review_info['content'].append(review_content_str)
        review_info['content'] = ''.join(map(str,review_info['content']))
        store.store_name = review_info['store_name']
        store.content = review_info['content']
        store.star = review_info['star']
        store.img = review_info['img']
        store.address = review_info['address']
        store.save()


