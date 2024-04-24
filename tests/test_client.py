# tests/test_client.py
import unittest
from app.client import Client

class TestClient(unittest.TestCase):
    def test_client_representation(self):
        client = Client("001", "abcd")
        self.assertEqual(str(client), "Client(client_id=001, hash_pattern=abcd)")
