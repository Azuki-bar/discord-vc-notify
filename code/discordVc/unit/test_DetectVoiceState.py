import unittest
from unittest.mock import MagicMock
from ..DetectVoiceState import DetectVoiceState
import discord


class TestDetectVoiceState(unittest.TestCase):
    def setUp(self) -> None:
        self.detect_voice_state = DetectVoiceState()

    def tearDown(self) -> None:
        pass

    def test_voice_channel_diff(self):
        self.detect_voice_state._before = MagicMock(discord.VoiceState)
        self.detect_voice_state._after = MagicMock(discord.VoiceState)
        before_channel = "BEFORE_CHANNEL"
        after_channel = "AFTER_CHANNEL"

        self.detect_voice_state._before.channel = None
        self.detect_voice_state._after.channel = after_channel
        self.detect_voice_state.voice_channel_diff()
        assert self.detect_voice_state._channel_status == self.detect_voice_state.IN

        self.detect_voice_state._before.channel = before_channel
        self.detect_voice_state._after.channel = None
        self.detect_voice_state.voice_channel_diff()
        assert self.detect_voice_state._channel_status == self.detect_voice_state.OUT

        self.detect_voice_state._before.channel = before_channel
        self.detect_voice_state._after.channel = after_channel
        self.detect_voice_state.voice_channel_diff()
        assert self.detect_voice_state._channel_status == self.detect_voice_state.moved

        self.detect_voice_state._before.channel = None
        self.detect_voice_state._after.channel = None
        self.detect_voice_state.voice_channel_diff()
        assert self.detect_voice_state._channel_status is None
