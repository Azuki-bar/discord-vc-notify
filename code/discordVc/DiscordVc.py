from . import DetectVoiceState, ChannelNotFoundError
import discord
from typing import Type
import logging

logging.basicConfig(level=logging.WARNING)


class DiscordVc(DetectVoiceState):
    def __init__(self, client: discord.Client, channel_id: int):
        super(DiscordVc, self).__init__()
        self._member = None
        self._message = None
        self._channel_id = channel_id
        self._client = client
        self._channel = self._client.get_channel(self._channel_id)

    @property
    def member(self) -> Type[discord.Member]:
        return self._member

    @member.setter
    def member(self, value):
        if isinstance(value, (discord.Member, type(None))):
            self._member = value
        else:
            raise TypeError("value type is", type(value))

    def _retrieve_message(self):
        user_name = self._member.display_name
        before_channel = self._before.channel
        after_channel = self._after.channel
        # return (user_name, before_channel, after_channel)
        if before_channel is None:
            res = f'{user_name}さんが{after_channel}に入室しました'
        elif after_channel is None:
            res = f'{user_name}さんが{before_channel}から退室しました'
        elif before_channel != after_channel:
            res = f'{user_name}さんが{before_channel}から{after_channel}へ移動しました'
        else:
            res = None
        self._message = res

    @property
    def channel_id(self) -> int:
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        if isinstance(value, int):
            self._channel_id = value
        elif value is None:
            raise ChannelNotFoundError
        else:
            raise TypeError

    @property
    def content(self) -> Type[str]:
        return self._message

    @content.setter
    def content(self, value):
        if isinstance(value, str) or value is None:
            self._message = value
        else:
            raise TypeError

    @property
    def channel(self):
        if self._channel is None:
            self._channel = self._client.get_channel(self._channel_id)
        return self._channel

    @channel.setter
    def channel(self, value):
        if isinstance(value, discord.ChannelType):
            self._channel = value
        else:
            raise TypeError

    async def send_message(self):
        self.voice_channel_diff()
        if self._channel_status is not None:
            self._retrieve_message()
            await self._channel.send(self.content)
