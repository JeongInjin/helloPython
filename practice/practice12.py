# pip install
# google pypi 검색
# ex ) pip install beautifulsoup4
# pip list
# pip show beautifulsoup4
# pip install --upgrade beautifulsoup4
# pup uninstall beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())