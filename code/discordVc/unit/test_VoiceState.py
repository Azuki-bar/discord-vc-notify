import unittest
from unittest.mock import MagicMock
from ..VoiceState import VoiceState
import discord
import pytest


class TestVoiceState(unittest.TestCase):
    def setUp(self) -> None:
        self._before_status = MagicMock(discord.VoiceState)
        self._after_status = MagicMock(discord.VoiceState)
        self.voice_state = VoiceState()

    def tearDown(self) -> None:
        pass

    def test_before_setter(self):
        with pytest.raises(TypeError):
            self.voice_state.before = "BEFORE"

        self.voice_state.before = self._before_status
        assert self.voice_state._before == self._before_status

    def test_before_getter(self):
        self.voice_state._before = self._before_status
        assert self.voice_state.before == self._before_status

    def test_after_setter(self):
        with pytest.raises(TypeError):
            self.voice_state.after = "AFTER"

        self.voice_state.after = self._after_status
        assert self.voice_state._after == self._after_status

    def test_after_getter(self):
        self.voice_state._after = self._after_status
        assert self.voice_state.after == self._after_status


if __name__ == '__main__':
    pytest.main([__file__])
