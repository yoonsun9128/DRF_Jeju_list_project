import pandas as pd
import numpy as np
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")

# df = pd.read_csv('main/jejulist.csv', encoding='cp949')
df1 = pd.read_csv('main/jejulist.csv', encoding='cp949')
df = df1.head(2)
# print(df.head())x

jeju_store = df[['업소명','소재지','메뉴']]
print(jeju_store.head())
jeju_store.columns = [ 'name','address','menu']

chromedriver = '/Users/azaleachoiyoonsun/Desktop/chromedriver' # 셀레늄이 이용할 크롤링 드라이버 디렉토리를 입력
driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
# chrome_options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)



# 네이버 지도 검색창에 [~동 @@식당]으로 검색해 정확도를 높여야 합니다. 검색어를 미리 설정해줍시다.

jeju_store['naver_keyword'] = jeju_store['address'] # "%20"는 띄어쓰기를 의미합니다.
jeju_store['naver_map_url'] = ''

naver_map_star_review_stars_list = []
naver_map_star_review_qty_list = []
# 본격적으로 가게 상세페이지의 URL을 가져옵시다

for i, keyword in enumerate(jeju_store['naver_keyword'].tolist()):
    print("이번에 찾을 키워드 :", i, f"/ {df.shape[0] -1} 행", keyword)
    try:
        naver_map_search_url = f"https://map.kakao.com/?q={keyword}"

        driver.get(naver_map_search_url)
        time.sleep(3.5)
        star_review_stars = driver.find_element(By.CSS_SELECTOR,"#info\.search\.place\.list > li > div.rating.clickArea > span.score > em").text
        star_review_qty = driver.find_element(By.CSS_SELECTOR,"#info\.search\.place\.list > li > div.rating.clickArea > span.score > a").text

        naver_map_star_review_stars_list.append(star_review_stars)
        naver_map_star_review_qty_list.append(star_review_qty)

    except Exception as e1:
        if "li:nth-child(1)" in str(e1):  # -> "child(1)이 없던데요?"
            try:
                jeju_store.iloc[i,-1] = driver.find_element(By.CSS_SELECTOR,"#info\.search\.place\.list > li > div.info_item > div.contact.clickArea > a.moreview").get_attribute('href')

                time.sleep(1)
            except Exception as e2:
                print(e2)
                jeju_store.iloc[i,-1] = np.nan
                time.sleep(1)
        else:
            pass

print(jeju_store)
print(naver_map_star_review_stars_list)
print(naver_map_star_review_qty_list)

driver.quit()

# 이때 수집한 것은 완전한 URL이 아니라 URL에 들어갈 ID (data-cid 라는 코드명으로 저장된) 이므로, 온전한 URL로 만들어줍니다

# jeju_store['naver_map_url'] = "https://place.map.kakao.com/" + jeju_store['naver_map_url']


# # URL이 수집되지 않은 데이터는 제거합니다.
# jeju_store = jeju_store.loc[~jeju_store['naver_map_url'].isnull()]

# naver_map_name_list = []
# naver_map_type_list = []
# blog_review_qty_list = []
# naver_map_star_review_stars_list = []
# naver_map_star_review_qty_list = []
# chromedriver = '/Users/azaleachoiyoonsun/Desktop/chromedriver'

# # 메인 드라이버 : 별점 등을 크롤링
# driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
# # 서브 드라이버 : 블로그 리뷰 텍스트를 리뷰 탭 들어가서 크롤링
# sub_driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)

# for i, url in enumerate(tqdm(jeju_store['naver_map_url'])):

#     driver.get(url)
#     sub_driver.get(url+"/review/ugc")
#     time.sleep(2)


#     try:

#         # 간단 정보 가져오기

#         # 네이버 지도의 유형 분류
#         # naver_map_type = driver.find_element_by_css_selector("#_title > span._3ocDE").text

#         # 블로그 별점 점수
#         star_review_stars = driver.find_element_by_css_selector("#mArticle > div.cont_essential > div:nth-child(1) > div.place_details > div > div > a:nth-child(3) > span.color_b").text

#         # 블로그 별점 평가 수
#         star_review_qty = driver.find_element_by_css_selector("#mArticle > div.cont_essential > div:nth-child(1) > div.place_details > div > div > a:nth-child(3) > span.color_g").text

#         # naver_map_type_list.append(naver_map_type)
#         naver_map_star_review_stars_list.append(star_review_stars)
#         naver_map_star_review_qty_list.append(star_review_qty)

#     # 리뷰가 없는 업체는 크롤링에 오류가 뜨므로 표기해둡니다.
#     except Exception as e1:
#         print(f"{i}행 문제가 발생")

#         # 리뷰가 없으므로 null을 임시로 넣어줍니다.
#         naver_map_type_list.append('null')
#         blog_review_qty_list.append('null')
#         naver_map_star_review_stars_list.append('null')
#         naver_map_star_review_qty_list.append('null')



# driver.quit()
# sub_driver.quit()


# jeju_store['naver_store_type'] = naver_map_type_list  # 네이버 상세페이지에서 크롤링한 업체 유형
# jeju_store['naver_star_point'] = naver_map_star_review_stars_list  # 네이버 상세페이지에서 평가한 별점 평점
# jeju_store['naver_star_point_qty'] = naver_map_star_review_qty_list  # 네이버 상세페이지에서 별점 평가를 한 횟수
# jeju_store['naver_blog_review_qty'] = blog_review_qty_list  # 네이버 상세페이지에 나온 블로그 리뷰의 총 개수

# # jeju_store = jeju_store.loc[~(jeju_store['naver_star_point'].str.contains('null'))]

# # # 별점 평균, 수 같은 데이터 역시 스트링 타입으로 크롤링이 되었으므로 numeric으로 바꿔줍니다.
# # jeju_store[['naver_star_point', 'naver_star_point_qty']] = jeju_store[['naver_star_point', 'naver_star_point_qty']].apply(pd.to_numeric)
