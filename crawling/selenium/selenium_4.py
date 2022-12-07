from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager # 크롬 드라이버 자동 업데이트

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://naver.com")












