import os

import requests

from dotenv import load_dotenv

load_dotenv()


token = os.getenv("TOKEN")


def get_user(username):
    url = "https://admin.laiwan.io/admin/user/search?username=" + username
    payload = {}
    headers = {
        'App-ID': 'laiwan',
        'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.json())
    if "result" not in response.json():
        return {'user_id': None, 'username': username}

    result = response.json()["result"]
    return result


def get_user_statements(user_id):
    url = f"https://admin.laiwan.io/admin/wallet/{user_id}/statement?page_size=10"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.json())
    if "result" not in response.json():
        return [{}]

    result = response.json()["result"]

    if "statements" not in result:
        return [{}]

    statements = result["statements"]
    return statements


file_path = "duplicate_usernames.txt"
output_file_path = 'user_info.txt'
# line_num = 0

with open(output_file_path, 'a') as output_file:
    with open(file_path, 'r') as file:
        for line in file:
            # line_num += 1
            # if line_num < 2755:
            #     continue
            username = line.strip()

            user = get_user(username)
            user_id = user["user_id"]

            statements = get_user_statements(user_id)
            if statements == []:
                statements = [{}]
            print(f"username: {username}  user_id: {user_id} statements: {statements[0]}")
            output_file.write(f"username: {username}  user_id: {user_id} statements: {statements[0]}\n")
