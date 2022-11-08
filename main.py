import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'

params = {
'q': 'Python Developer',
'l': 'New York State',
'vjk': 'fba8a8a2fd21f8c8'
}
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
res = requests.get(url, params=params, headers=headers)
print(res.status_code)