#https://www.postman.com/ — testing api
import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'ZTNkYjdjYzAtMmY3My00MmE1LTliZjMtZDU1NjZlYmYwOWY5OjI1YzZkNDQ1NTU4OTQzZjZhYjE0OWRiNzJmNjY4Mjcy'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
    token = auth.text
    print('Вошли в систему')
    while True:
        word = input('Введите слово для перевода: ')
        if word:
            headers_translate = {
                'Authorization': 'Bearer ' + token
            }
            params = {
                'text': word,
                'srcLang': 1049,
                'dstLang': 1033
            }
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params )
            res = r.json()

            try:
                print(res['Translation']['Translation'])
            except: 
                print('не найдено варианта для перевода')

else:
    print('Error!')
