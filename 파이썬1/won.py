#환율 알려주는 코딩

import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'

response = requests.get(url).text

data = BeautifulSoup(response,"html.parser")

won = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print(f'달러 환율은 {won}원입니다.')