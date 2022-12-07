# 셀레니움
# 1.크롬 드라이버 다운로드: https://chromedriver.chromium.org/downloads
# 2.셀레니움 설치 pip install selenium

# from selenium import webdriver

# browswer = webdriver.Chrome('/Users/chromedriver')
# browswer.get("https://www.naver.com")
#

from selenium.webdriver.common.keys import Keys
import time
import csv

# 4버전
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # 크롬 드라이버 자동 업데이트
from selenium.webdriver.chrome.service import Service

# find_element_by_css_selector 를 쓰기위해..
# https://hyunsooworld.tistory.com/entry/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EC%98%A4%EB%A5%98-AttributeError-WebDriver-object-has-no-attribute-findelementbycssselector-%EC%98%A4%EB%A5%98%ED%95%B4%EA%B2%B0
from selenium.webdriver.common.by import By



# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
# browser = webdriver.Chrome(service=service, options=chrome_options)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# csv
f = open("/Users/injinjeong/jeong_workspace/python_workspace/hellopython/crawling/selenium/data.csv", 'w', encoding='CP949', newline='')
csvWirter = csv.writer(f)


# 웹페이지 해당 주소 이동
browser.get("https://www.naver.com")
# 로딩이 끝날 때까지 2초 기다려준다.
browser.implicitly_wait(1)
# 메뉴클릭
browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click()
time.sleep(1)
# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, 'input._searchInput_search_text_3CUDs')
search.click()
# 검색어 입력
search.send_keys("아이폰 14")
search.send_keys(Keys.ENTER)

before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤 내리기
    browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)

    # 스크롤 로딩시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")
    # print("before_h:", before_h, "after_h:", after_h)

    if after_h == before_h:
        break
    before_h = after_h

# 상품 정보 div
print("===")
items = browser.find_elements(By.CSS_SELECTOR, '.basicList_info_area__TWvzp')
for item in items:
    name = item.find_element(By.CSS_SELECTOR, '.basicList_title__VfX3c > a').text
    try:
        price = item.find_element(By.CSS_SELECTOR, '.price_num__S2p_v').text
    except:
        price = "판매중단"
        link = item.find_element(By.CSS_SELECTOR, '.basicList_title__VfX3c > a').get_attribute('href')
    print(name, price, link)
    csvWirter.writerow([name, price, link])

# 파일 닫기
f.close()
