import os
import json


class GetId:
    def __init__(self):
        pass

    def channel_id(self):
        pass

    def access_token(self):
        pass


class GetIdEnvVals(GetId):
    def __init__(self):
        super(GetIdEnvVals, self).__init__()
        self.TOKEN_ENV_VAL = 'TOKEN'
        self.CHANNEL_ID_ENV_VAL = 'CHANNEL_ID'

    @property
    def channel_id(self):
        return int(os.environ[self.CHANNEL_ID_ENV_VAL])

    @property
    def access_token(self):
        return os.environ[self.TOKEN_ENV_VAL]

    def check_env_vals(self) -> bool:
        return self.TOKEN_ENV_VAL in os.environ and \
               self.CHANNEL_ID_ENV_VAL in os.environ


class GetIdJson(GetId):
    def __init__(self, service='discord'):
        super(GetIdJson, self).__init__()
        self.service = service
        self.json_data = None

    def get_json(self, json_file):
        if not os.path.exists(json_file):
            raise FileNotFoundError

        with open(json_file, "r") as f:
            raw_json = json.load(f)
        return raw_json[self.service]

    def fetch_json_file(self, json_file_path):
        self.json_data = self.get_json(json_file_path)

    @property
    def channel_id(self):
        return int(self.json_data[self.service]['channel_id'])

    @property
    def access_token(self):
        return self.json_data[self.service]['access_token']
