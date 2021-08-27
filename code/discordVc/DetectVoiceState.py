from .VoiceState import VoiceState


class DetectVoiceState(VoiceState):
    def __init__(self):
        super(DetectVoiceState, self).__init__()
        # self._voice_status = VoiceState()
        self.IN = 'IN'
        self.OUT = "OUT"
        self.moved = "MOVED"
        self._channel_status = None

    def voice_channel_diff(self):
        before_channel = self.before.channel
        after_channel = self.after.channel

        if before_channel is None and after_channel is not None:
            self._channel_status = self.IN
        elif before_channel is not None and after_channel is None:
            self._channel_status = self.OUT
        elif before_channel != after_channel:
            self._channel_status = self.moved
        else:
            self._channel_status = None
