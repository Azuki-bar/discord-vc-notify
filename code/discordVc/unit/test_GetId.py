import unittest
from ..GetId import GetIdJson, GetIdEnvVals
import json
import time
import os
import random
import pytest
import pytest_mock


class TestGetIdJson(unittest.TestCase):
    def setUp(self):
        self.service = 'discord'
        self.channel_id = 1111111
        self.access_token = "AAA"

        self.GetIdJson = GetIdJson(service=self.service)
        self.GetIdJson.json_data = {
            self.service: {
                "channel_id": self.channel_id,
                "access_token": self.access_token
            }
        }

    def test_channel_id(self):
        self.assertIsInstance(self.GetIdJson.channel_id, int)
        self.assertEqual(self.channel_id, self.GetIdJson.channel_id)

    def test_access_token(self):
        self.assertEqual(self.access_token, self.GetIdJson.access_token)

    def test_get_json(self):
        with self.assertRaises(FileNotFoundError):
            self.GetIdJson.get_json("")


class TestGetIdEnvVals(unittest.TestCase):
    def setUp(self) -> None:
        self.get_id_env_vals = GetIdEnvVals()
        random.seed(time.time())
        self.get_id_env_vals.TOKEN_ENV_VAL = "TEST_TOKEN" + str(random.random())
        self.get_id_env_vals.CHANNEL_ID_ENV_VAL = "TEST_ID" + str(
            random.random()
        )
        self.token = "XXXXXXX"
        self.channel_id = 1111111
        os.environ[self.get_id_env_vals.TOKEN_ENV_VAL] = self.token
        os.environ[self.get_id_env_vals.CHANNEL_ID_ENV_VAL] = str(
            self.channel_id)

    def tearDown(self) -> None:
        os.environ.pop(self.get_id_env_vals.TOKEN_ENV_VAL, None)
        os.environ.pop(self.get_id_env_vals.CHANNEL_ID_ENV_VAL, None)

    def test_access_token(self):
        self.assertEqual(self.token, self.get_id_env_vals.access_token)

    def test_channel_id(self):
        self.assertIsInstance(self.get_id_env_vals.channel_id, int)
        self.assertEqual(self.channel_id, self.get_id_env_vals.channel_id)

    def test_check_env_vals(self):
        self.assertTrue(self.get_id_env_vals.check_env_vals())
        os.environ.pop(self.get_id_env_vals.TOKEN_ENV_VAL, None)
        self.assertFalse(self.get_id_env_vals.check_env_vals())


if __name__ == '__main__':
    unittest.main()
