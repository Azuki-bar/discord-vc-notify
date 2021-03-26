import os
import json


def add_auth(file_path='./.auth_file.json', service='discord'):
    if os.path.exists(file_path):
        print('ファイルが存在しています。 File exists.')
        print('Enterを押すと続行します。終了は C-c')
        input()

    print(f'{service}の認証情報を保存します。')
    channel_id = int(input("Channel ID >>> "))
    access_token = input("access_token >>> ")
    json_data = dict([(service, None)])
    json_data[service] = {
        "channel_id": channel_id,
        "access_token": access_token
    }
    with open(file_path, 'w') as f:
        json.dump(json_data, f, indent=2)


if __name__ == '__main__':
    add_auth()
