# app/request_handler.py
import hashlib

class RequestHandler:
    def __init__(self, clients):
        self.clients = clients

    def extract_client_id(self, request_hash):
        client_id_hash = request_hash[4:8]
        for client in self.clients:
            # Certificar que o hash_pattern do cliente é o que estamos tentando comparar
            if client.hash_pattern == client_id_hash:
                return client.client_id
        return None
