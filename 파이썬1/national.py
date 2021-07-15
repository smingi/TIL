import requests
name = ['tak', 'tony', 'eric']
url = 'https://api.nationalize.io/?name='
for i in name:
    response = requests.get(url+i)
    result = response.json()
    result2 = result['country'][0]['country_id']
    
    print(i,' : ',result2)