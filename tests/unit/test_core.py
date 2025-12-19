import unittest
from my_addon.core.client import Client
from my_addon.core.state import State

class TestCore(unittest.TestCase):
    def test_client_connection(self):
        client = Client()
        self.assertFalse(client.connected)
        success = client.connect()
        self.assertTrue(success)
        self.assertTrue(client.connected)

    def test_state_management(self):
        state = State()
        state.update("version", "1.0")
        self.assertEqual(state.data["version"], "1.0")
