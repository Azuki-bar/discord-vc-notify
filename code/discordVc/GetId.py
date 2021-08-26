import os
import json

TOKEN_ENV_VAL = 'TOKEN'
CHANNEL_ID_ENV_VAL = 'CHANNEL_ID'


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
        pass

    @property
    def channel_id(self):
        try:
            return int(os.environ[CHANNEL_ID_ENV_VAL])
        except ValueError:
            exit("please check your Channel ID")

    @property
    def access_token(self):
        return os.environ[TOKEN_ENV_VAL]

    def check_env_vals(self) -> bool:
        return TOKEN_ENV_VAL in os.environ and CHANNEL_ID_ENV_VAL in os.environ


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

    @property
    def channel_id(self):
        try:
            return int(self.json_data[self.service])
        except ValueError:
            exit("please check your Channel ID")

    @property
    def access_token(self):
        return self.json_data[self.service]
