import discord
from typing import Type


class VoiceState:
    def __init__(self):
        self._before = discord.VoiceState
        self._after = discord.VoiceState

    @property
    def before(self) -> Type[discord.VoiceState]:
        return self._before

    @property
    def after(self) -> Type[discord.VoiceState]:
        return self._after

    @before.setter
    def before(self, before: discord.VoiceState):
        if isinstance(before, discord.VoiceState):
            self._before = before
        else:
            raise TypeError

    @after.setter
    def after(self, after: discord.VoiceState):
        if isinstance(after, discord.VoiceState):
            self._after = after
        else:
            raise TypeError
