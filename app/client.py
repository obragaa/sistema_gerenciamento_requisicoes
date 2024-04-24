# app/client.py

class Client:
    def __init__(self, client_id, hash_pattern):
        self.client_id = client_id
        self.hash_pattern = hash_pattern

    def __repr__(self):
        return f"Client(client_id={self.client_id}, hash_pattern={self.hash_pattern})"
