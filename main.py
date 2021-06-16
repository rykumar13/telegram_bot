import json
import instaloader
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


def get_unfollows():

    # login
    L = instaloader.Instaloader()
    L.login(auth.insta_username, auth.insta_password)
    profile = instaloader.Profile.from_username(L.context, auth.insta_username)

    # retrieve & store current followers to file
    current_file = open('current.txt', 'w')
    current_followers = []
    for follower in profile.get_followers():
        current_file.write(follower.username + '\n')
        current_followers.append(follower.username)
    current_file.close()

    # open current followers from file
    current_followers = open('current.txt').readlines()

    # open old followers from file
    old_followers = open('old.txt').readlines()

    # calculate differences in followers
    s = set(current_followers)
    difference = [x for x in old_followers if x not in s]

    # find unfollows
    for x in difference:
        if x in old_followers and x not in current_followers:
            unfollwer = x.strip('\n')
            send_message(f'{unfollwer} unfollowed you.')

    # store current followers into old file
    old_file = open('old.txt', 'w')
    for follower in current_followers:
        old_file.write(follower)
    old_file.close()


if __name__ == '__main__':
    get_unfollows()