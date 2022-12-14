import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = 'game_data_01.xlsx'
wb = openpyxl.load_workbook(fpath)
# 현재 활성화된 시트 선택
ws = wb.active

# 종목 코드 리스트
codes = [
    '005930',
    '000660',
    '035720',
]
row = 2
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(",", "")
    print(price)
    ws[f'B{row}'] = int(price)
    row = row + 1

wb.save(fpath)