import requests
url='https://api.telegram.org/bot7008391655:AAHhlcoplGN6_qk0jzfpJwAU97kNQ3qAuNk/sendMessage?chat_id=1274684718&text=Hello eblo'
response=requests.get(url)
print(response.text)
