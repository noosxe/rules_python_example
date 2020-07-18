import requests

response = requests.get('https://google.com')

print(f'response status code was {response.status_code}')
