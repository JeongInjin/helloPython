import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%85%8C%EC%8A%AC%EB%9D%BC")
html = response.text

soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")
# print(links)

for link in links:
    title = link.text
    url = link.attrs['href']
    print(title, url)
