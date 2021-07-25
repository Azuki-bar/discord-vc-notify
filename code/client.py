import discord
import os
import sys
import time
import json

TOKEN_ENV_VAL = 'TOKEN'
CHANNEL_ID_ENV_VAL = 'CHANNEL_ID'


class ChannelNotFoundError(Exception):
    pass


class GetId:
    def __init__(self):
        pass

    def channel_id(self):
        pass

    def access_token(self):
        pass


class GetIdJson(GetId):
    def __init__(self, json_data_path, service='discord'):
        super(GetIdJson, self).__init__()
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


class GetIdEnvVals(GetId):
    def __init__(self):
        super(GetIdEnvVals, self).__init__()
        pass

    def channel_id(self):
        try:
            return int(os.environ[CHANNEL_ID_ENV_VAL])
        except ValueError:
            exit("please check your Channel ID")

    def access_token(self):
        return os.environ[TOKEN_ENV_VAL]


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
    discord_auth = None
    if TOKEN_ENV_VAL in os.environ and CHANNEL_ID_ENV_VAL in os.environ:
        discord_auth = GetIdEnvVals()
    else:
        discord_auth = GetIdJson('./.auth_file.json')
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
            channel = client.get_channel(channel_id)
            if (channel is None):
                raise ChannelNotFoundError
            await channel.send(res)

    client.run(discord_auth.access_token())