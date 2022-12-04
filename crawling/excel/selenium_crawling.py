# 셀레니움
# 1.크롬 드라이버 다운로드: https://chromedriver.chromium.org/downloads
# 2.셀레니움 설치 pip install selenium

# from selenium import webdriver

# browswer = webdriver.Chrome('/Users/chromedriver')
# browswer.get("https://www.naver.com")
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# find_element_by_css_selector 를 쓰기위해..
# https://hyunsooworld.tistory.com/entry/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EC%98%A4%EB%A5%98-AttributeError-WebDriver-object-has-no-attribute-findelementbycssselector-%EC%98%A4%EB%A5%98%ED%95%B4%EA%B2%B0
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
browser.get("https://www.naver.com")
# 로딩이 끝날 때까지 2초 기다려준다.
browser.implicitly_wait(2)
# 메뉴클릭
browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click()
time.sleep(2)
# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, 'input._searchInput_search_text_3CUDs')
search.click()
# 검색어 입력
search.send_keys("아이폰 14")
search.send_keys(Keys.ENTER)

