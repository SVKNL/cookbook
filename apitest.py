import requests
import time
api_url='https://api.telegram.org/bot'
bot_token='7008391655:AAHhlcoplGN6_qk0jzfpJwAU97kNQ3qAuNk'
text: str='you are eblo!'
max_counter:int = 100
offset:int=-2
counter:int=0
chat_id:int

while counter<=max_counter:
    print(f'number of messages= {counter}')
    updates = requests.get(f'{api_url}{bot_token}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text={text}')

    time.sleep(1)
    counter += 1




response=requests.get(url)
print(response.text)
