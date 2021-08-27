import unittest
from ..VoiceState import VoiceState
import discord
import pytest


class TestVoiceState(unittest.TestCase):
    def setUp(self) -> None:
        self._before_status = discord.VoiceState
        self._after_status = discord.VoiceState
        self.voice_state = VoiceState()

    def tearDown(self) -> None:
        pass

    def test_get_before(self):
        assert type(self.voice_state.before) == type(discord.VoiceState)

    def test_get_after(self):
        assert type(self.voice_state.after) == type(discord.VoiceState)


if __name__ == '__main__':
    pytest.main([__file__])
