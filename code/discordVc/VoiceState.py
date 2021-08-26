import discord
from typing import Type


class VoiceState:
    def __init__(self):
        self._before_status = discord.VoiceState
        self._after_status = discord.VoiceState

    @property
    def before(self) -> Type[discord.VoiceState]:
        return self._before_status

    @property
    def after(self) -> Type[discord.VoiceState]:
        return self._after_status

    @before.setter
    def before(self, before: discord.VoiceState):
        if isinstance(before, discord.VoiceState):
            self._before_status = before
        else:
            raise TypeError

    @after.setter
    def after(self, after: discord.VoiceState):
        if isinstance(after, discord.VoiceState):
            self._after_status = after
        else:
            raise TypeError
