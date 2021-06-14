import requests
import auth

base_url = 'https://api.telegram.org/bot'


def test_bot():
    response = requests.get(base_url + auth.secret_token + '/getMe')

    if response.status_code == 200:
        print('im alive')
        return
    print(response.content)


def get_updates():
    response = requests.get(base_url + auth.secret_token + '/getUpdates')
    print(response.content)


def send_message(message):
    payload = {'chat_id': auth.chat_id, 'text': message}
    response = requests.get(base_url + auth.secret_token + '/sendMessage', params=payload)

    if response.status_code == 200:
        print('Message sent successfully')
        return
    print(response.status_code)


if __name__ == '__main__':
    # get_updates()
    # test_bot()
    send_message('Hello this is a test notification')
