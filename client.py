import discord
import os
import sys
import time
import json


class GetID:
    def __init__(self, json_data_path, service='discord'):
        self.service = service
        self.json_data = self.get_json(json_data_path)

    def get_json(self, json_file):
        if not os.path.exists(json_file):
            raise FileNotFoundError

        with open(json_file, "r") as f:
            raw_json = json.load(f)
        return raw_json[self.service]

    def channel_id(self):
        return self.json_data['channel_id']

    def access_token(self):
        return self.json_data['access_token']


def detect_voice_diff(before_voice_status, after_voice_status):
    before_channel = before_voice_status.channel
    after_channel = after_voice_status.channel

    if before_channel is None and after_channel is not None:
        return 'in'
    elif before_channel is not None and after_channel is None:
        return 'out'
    elif before_channel != after_channel:
        return 'moved'
    else:
        return None


def message(member, before, after):
    user_name = member.display_name
    before_channel = before.channel
    after_channel = after.channel

    if before_channel is None:
        res = f'{user_name}さんが{after_channel}に入室しました'
    elif after_channel is None:
        res = f'{user_name}さんが{before_channel}から退室しました'
    elif before_channel != after_channel:
        res = f'{user_name}さんが{before_channel}から{after_channel}へ移動しました'
    else:
        res = None
    return res


if __name__ == '__main__':
    proxy = None
    if "HTTP_PROXY" in os.environ:
        proxy = os.environ["HTTP_PROXY"]
    client = discord.Client(proxy=proxy)
    discord_auth = GetID('./.auth_file.json')
    channel_id = discord_auth.channel_id()


    @client.event
    async def on_ready():
        print("login success")


    @client.event
    async def on_voice_state_update(member, before, after):
        if member.bot:
            return

        voice_status = detect_voice_diff(before, after)
        if voice_status is not None:
            res = message(member, before, after)
            await client.get_channel(channel_id).send(res)


    client.run(discord_auth.access_token())
