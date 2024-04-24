import unittest
from app.client import Client
from app.request_handler import RequestHandler

class TestRequestHandler(unittest.TestCase):
    def setUp(self):
        # Configurando os clientes com hash_patterns que correspondem ao esperado
        self.client1 = Client("001", "a01e")
        self.client2 = Client("002", "88e0")
        self.handler = RequestHandler([self.client1, self.client2])

    def test_extract_client_id(self):
        # Usando hashes que incluem os hash_patterns corretamente
        test_hash_for_client1 = "xxxxa01exxxx"
        test_hash_for_client2 = "xxxx88e0xxxx"

        self.assertEqual(self.handler.extract_client_id(test_hash_for_client1), "001")
        self.assertEqual(self.handler.extract_client_id(test_hash_for_client2), "002")
        self.assertIsNone(self.handler.extract_client_id("xxxxxxxxxxxx"))


if __name__ == "__main__":
    unittest.main()
