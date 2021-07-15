#요청을 보내주는 requests 를 가져온다
import requests

url = 'https://api.agify.io/?name=michael'
response = requests.get(url)
result = response.json()
print(result['age'])
print('tak, tony, eric, musk')

#기본코드 

#1 url
url1 = 'https://api.agify.io?name=tak'
url2 = 'https://api.agify.io?name=tony'
url3 = 'https://api.agify.io?name=eric'
url4 = 'https://api.agify.io?name=musk'
response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
response4 = requests.get(url4)

# 2 json
result1 = response1.json()
result2 = response2.json()
result3 = response3.json()
result4 = response4.json()

print(result1['age'])
print(result2['age'])
print(result3['age'])
print(result4['age'])

## 추가 코드
#tak, tony, eric, musk

