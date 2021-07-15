import requests
name = ['tak', 'tony', 'eric', 'musk']
url = 'https://api.agify.io/?name='
for i in name:
    response = requests.get(url+i)
    result = response.json()
    print(i,' : ',result['age'])
