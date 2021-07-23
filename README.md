# discord-vc-notify

このスクリプトはdiscordのボイスチャットに入退室したときに指定されたチャンネルに通知を
送信するものです。

この Bot に関して書いたブログ [https://azukibar.dev/blog/2021/07/discord-vc/](https://azukibar.dev/blog/2021/07/discord-vc/) も参考にしてください。

## Docker を使用する

## ダウンロード先

このリポジトリから作成されたDockerイメージはGitHub Container Registry とDocker Hubにアップロードされています。

ダウンロードは以下のどちらかでお願いします。

```
docker pull ghcr.io/azuki-bar/discord-vc-notify
# or
docker pull azukibar/discord-vc-notify
```


### docker compose を使用する

以下の`docker-compose.yml`を好きな場所に置いてください。
```yaml
version: '3'
services:
  server:
    image: ghcr.io/azuki-bar/discord-vc-notify:latest
    environment:
      TOKEN: "YOUR TOKEN"
      CHANNEL_ID: "NOTIFY CHANNEL ID"`
```

その後`docker-compose up -d`で起動してください。

## pipenv を使用する

`pipenv install`で環境を整えてください。

次に`pipenv run add_auth_data.py`で認証情報を保存してください。
この時、チャンネルIDとアクセストークンが必要です。

任意のサーバで動かしてください。

## publish status
![latest release](https://github.com/Azuki-bar/discord-vc-notify/actions/workflows/publishDockerImageLatest.yml/badge.svg)

![GitHub Container Registory](https://github.com/Azuki-bar/discord-vc-notify/actions/workflows/publishDockerImageTags.yml/badge.svg)
