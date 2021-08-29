import unittest
from unittest.mock import MagicMock
from ..DiscordVc import DiscordVc
import pytest
import discord


class TestDiscordVc(unittest.TestCase):
    def setUp(self) -> None:
        self.channel_mock = MagicMock(discord.ChannelType)
        self.member_mock = MagicMock(discord.Member)
        self.discord_vc = DiscordVc(self.channel_mock)

    def test_set_member(self):
        with pytest.raises(TypeError) as e:
            self.discord_vc.member = "MEMBER"

        self.discord_vc.member = None
        assert self.discord_vc._member is None

        self.discord_vc.member = self.member_mock
        assert self.discord_vc._member == self.member_mock

    def test_get_member(self):
        self.discord_vc._member = self.member_mock
        assert self.discord_vc.member == self.member_mock

    def test_retrieve_message(self):
        user_name = "USERNAME"
        before_channel = "BEFORE_CHANNEL"
        after_channel = "AFTER_CHANNEL"

        self.discord_vc._member = MagicMock(discord.Member)
        self.discord_vc._member.display_name = user_name
        self.discord_vc._before = MagicMock(discord.VoiceState)
        self.discord_vc._after = MagicMock(discord.VoiceState)

        self.discord_vc._before.channel = None
        self.discord_vc._after.channel = after_channel

        retrieve_message = self.discord_vc._retrieve_message

        retrieve_message()
        assert self.discord_vc._message == \
               f'{user_name}さんが{after_channel}に入室しました'

        self.discord_vc._before.channel = before_channel
        self.discord_vc._after.channel = None
        retrieve_message()
        assert self.discord_vc._message == \
               f'{user_name}さんが{before_channel}から退室しました'

        self.discord_vc._before.channel = before_channel
        self.discord_vc._after.channel = after_channel
        retrieve_message()
        assert self.discord_vc._message == \
               f'{user_name}さんが{before_channel}から{after_channel}へ移動しました'

        self.discord_vc._before.channel = before_channel
        self.discord_vc._after.channel = self.discord_vc._before.channel
        retrieve_message()
        assert self.discord_vc._message is None

    def test_send_message(self):
        self.discord_vc._channel.send = MagicMock(
            name='discord.TextChannel.send')
        self.discord_vc._member = MagicMock(discord.Member)
        self.discord_vc._before = MagicMock(discord.VoiceState)
        self.discord_vc._after = MagicMock(discord.VoiceState)
        before_channel = "BEFORE_CHANNEL"
        after_channel = "AFTER_CHANNEL"

        self.discord_vc._before.channel = None
        self.discord_vc._after.channel = after_channel
        self.discord_vc.send_message()

        self.discord_vc._before.channel = before_channel
        self.discord_vc._after.channel = None
        self.discord_vc.send_message()

        self.discord_vc._before.channel = before_channel
        self.discord_vc._after.channel = after_channel
        self.discord_vc.send_message()

        self.discord_vc._before.channel = None
        self.discord_vc._after.channel = None
        self.discord_vc.send_message()

        assert self.discord_vc._channel.send.call_count == 3


if __name__ == '__main__':
    unittest.main()
