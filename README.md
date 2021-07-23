# discord-vc-notify

このスクリプトはdiscordのボイスチャットに入退室したときに指定されたチャンネルに通知を
送信するものです。

## Docker を使用する

### docker compose を使用する

#### 1. tokenを設定する

`./docker-compose.yaml`ファイル内の`TOKEN`, `CHANNEL_ID`を各自の物に変更してください。

`TOKEN`は機密情報ですからPushしないように気をつけください。

#### 2.  サーバを起動する

`docker-compose up -d`でサーバを起動出来ます。

## pipenv を使用する

`pipenv install`で環境を整えてください。

次に`pipenv run add_auth_data.py`で認証情報を保存してください。
この時、チャンネルIDとアクセストークンが必要です。

任意のサーバで動かしてください。

## publish status
![docker hub](https://github.com/Azuki-bar/discord-vc-notify/actions/workflows/uploadDockerHub.yaml/badge.svg)

![GitHub Container Registory](https://github.com/Azuki-bar/discord-vc-notify/actions/workflows/uploadGhcrio.yml/badge.svg)
