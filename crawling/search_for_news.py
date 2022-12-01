import requests
from bs4 import BeautifulSoup
import pyautogui

# pyautogui 설치
# pip install pyautogui
# keyword = input("검색어 입력:")
keyword = pyautogui.prompt("검색어 입력:")
last_page = pyautogui.prompt("마지막 페이지번호를 입력해 주세요:")
page_num = 1
for i in range(1, int(last_page) * 10, 10):
    print(f"{page_num} 페이지 입니다.===========================================================================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tap_jum&query={keyword}&start={i}")
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit")
    # print(links)

    for link in links:
        title = link.text
        url = link.attrs['href']
        print(title, url)
    page_num = page_num + 1