import requests
print('hello world')


url = 'https://phishstats.info:2096/api/phishing?_where=(date,gt,1900-01-06T12:03:00.000Z)&_p=1&_size=100'

test = requests.get(url)
print(test.json())
