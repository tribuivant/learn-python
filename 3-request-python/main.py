'''
Trước tiên phải cài đặt module requests
pip install requests

Ref: https://realpython.com/python-requests/
'''

import requests
response = requests.get('https://api.github.com')
# print(response.text)
# print(response.json()['user_repositories_url'])