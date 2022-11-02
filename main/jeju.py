import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from tqdm import tqdm

jeju_store = pd.read_csv('jejulist.csv', encoding='cp949')
# print(df.head())
jeju_store = jeju_store[['업소명','소재지','메뉴']]
print(jeju_store.head(4))
jeju_store.columns = [ 'name','address','menu']

chromedriver = '/Users/ksh40/Desktop/chromedriver' 
driver = webdriver.Chrome(chromedriver) 

# 포스팅 작성 당시 크롬 버젼 : 92

# 네이버 지도 검색창에 [~동 @@식당]으로 검색해 정확도를 높여야 합니다. 검색어를 미리 설정해줍시다.

jeju_store['naver_keyword'] = jeju_store['address'] # "%20"는 띄어쓰기를 의미합니다.
jeju_store['naver_map_url'] = ''


# 본격적으로 가게 상세페이지의 URL을 가져옵시다

for i, keyword in enumerate(jeju_store['naver_keyword'].tolist()):
    print("이번에 찾을 키워드 :", i, f"/ {jeju_store.shape[0] -1} 행", keyword)
    try:
        naver_map_search_url = f"https://m.map.naver.com/search2/search.naver?query={keyword}&sm=hty&style=v5"
        
        driver.get(naver_map_search_url)
        time.sleep(3.5)
        jeju_store.iloc[i,-1] = driver.find_element_by_css_selector("#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute('data-cid')
        # 네이버 지도 시스템은 data-cid에 url 파라미터를 저장해두고 있었습니다.
        # data-cid 번호를 뽑아두었다가 기본 url 템플릿에 넣어 최종적인 url을 완성하면 됩니다.
        
        #만약 검색 결과가 없다면?
    except Exception as e1:
        if "li:nth-child(1)" in str(e1):  # -> "child(1)이 없던데요?"
            try:
                jeju_store.iloc[i,-1] = driver.find_element_by_css_selector("#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute('data-cid')
                time.sleep(1)
            except Exception as e2:
                print(e2)
                jeju_store.iloc[i,-1] = np.nan
                time.sleep(1)
        else:
            pass


driver.quit()


# 이때 수집한 것은 완전한 URL이 아니라 URL에 들어갈 ID (data-cid 라는 코드명으로 저장된) 이므로, 온전한 URL로 만들어줍니다

jeju_store['naver_map_url'] = "https://m.place.naver.com/restaurant/" + jeju_store['naver_map_url']


# URL이 수집되지 않은 데이터는 제거합니다.
jeju_stored = jeju_store.loc[~jeju_store['naver_map_url'].isnull()]


# 각 데이터들을 미리 리스트에 담은 다음, 마지막에 데이터 프레임에 합칠 것입니다.

naver_map_name_list = []
naver_map_star_review_stars_list = []
naver_map_star_review_qty_list = []
chromedriver = '/Users/ksh40/Desktop/chromedriver' 

# 메인 드라이버 : 별점 등을 크롤링
driver = webdriver.Chrome(chromedriver) 

# 서브 드라이버 : 블로그 리뷰 텍스트를 리뷰 탭 들어가서 크롤링
sub_driver = webdriver.Chrome(chromedriver)

for i, url in enumerate(tqdm(jeju_store['naver_map_url'])):

    driver.get(url)
    sub_driver.get(url+"/review/ugc")
    time.sleep(2)


    try:

        # 간단 정보 가져오기
        
        # 네이버 지도의 유형 분류
        naver_map_type = driver.find_element_by_css_selector("#_title > span._3ocDE").text

        # 블로그 별점 점수
        star_review_stars = driver.find_element_by_css_selector("#app-root > div > div > div.place_detail_wrapper > div.place_section.no_margin.GCwOh > div > div > div._3XpyR > div > span._1Y6hi._1A8_M > em").text

        # 블로그 별점 평가 수
        star_review_qty = driver.find_element_by_css_selector("#app-root > div > div > div.place_detail_wrapper > div.place_section.no_margin.GCwOh > div > div > div._3XpyR > div > span:nth-child(2) > a > em").text
       

        naver_map_name_list.append(naver_map_type)
        naver_map_star_review_stars_list.append(star_review_stars)
        naver_map_star_review_qty_list.append(star_review_qty)

    # 리뷰가 없는 업체는 크롤링에 오류가 뜨므로 표기해둡니다.
    except Exception as e1:
        print(f"{i}행 문제가 발생")
        
        # 리뷰가 없으므로 null을 임시로 넣어줍니다.
        naver_map_name_list.append('null')
        naver_map_star_review_stars_list.append('null')
        naver_map_star_review_qty_list.append('null')


        
driver.quit()
sub_driver.quit()


jeju_store['naver_store_type'] = naver_map_name_list  # 네이버 상세페이지에서 크롤링한 업체 유형
jeju_store['naver_star_point'] = naver_map_star_review_stars_list  # 네이버 상세페이지에서 평가한 별점 평점
jeju_store['naver_star_point_qty'] = naver_map_star_review_qty_list  # 네이버 상세페이지에서 별점 평가를 한 횟수
