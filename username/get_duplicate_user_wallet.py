import os
import re

import requests

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")


def get_user_currencies(user_id):
    url = f"https://admin.laiwan.io/admin/wallet/{user_id}"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.json())
    if "result" not in response.json():
        return [{}]

    result = response.json()["result"]

    if "currencies" not in result:
        return [{}]

    currencies = result["currencies"]
    return currencies


file_path = "user_info_1.txt"
output_file_path = 'duplicate_user_wallet.txt'
# line_num = 0

with open(file_path, 'r') as file:
    for line in file:
        # line_num += 1
        # if line_num < 2755:
        #     continue
        match = re.search(r'username: (\w+)\s+user_id: ([\w-]+)', line)
        if match:
            # 提取匹配到的username和user_id
            username = match.group(1)
            user_id = match.group(2)
            # 输出结果

        currencies = get_user_currencies(user_id)

        with open(output_file_path, 'a') as output_file:
            if len(currencies) == 0:
                print(f"{username}\n")
                output_file.write(
                    f"{username}\n"
                )
                continue

            if len(currencies) == 1:
                print(
                    f"{username} {currencies[0]['code']}: {currencies[0]['total_amount']}"
                    f" created_at: {currencies[0]['created_at']} "
                    f"last_changed_at: {currencies[0]['last_changed_at']}"
                )
                output_file.write(
                    f"{username} {currencies[0]['code']}: {currencies[0]['total_amount']}"
                    f" created_at: {currencies[0]['created_at']} "
                    f"last_changed_at: {currencies[0]['last_changed_at']}\n"
                )
                continue

            print(
                f"{username} {currencies[0]['code']}: {currencies[0]['total_amount']}"
                f" created_at: {currencies[0]['created_at']} "
                f"last_changed_at: {currencies[0]['last_changed_at']}"
                f" {currencies[1]['code']}: {currencies[1]['total_amount']}"
                f" created_at: {currencies[1]['created_at']} "
                f"last_changed_at: {currencies[1]['last_changed_at']}"
            )
            output_file.write(
                f"{username} {currencies[0]['code']}: {currencies[0]['total_amount']}"
                f" created_at: {currencies[0]['created_at']} "
                f"last_changed_at: {currencies[0]['last_changed_at']}"
                f" {currencies[1]['code']}: {currencies[1]['total_amount']}"
                f" created_at: {currencies[1]['created_at']} "
                f"last_changed_at: {currencies[1]['last_changed_at']}\n"
            )
