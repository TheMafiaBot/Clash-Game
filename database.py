import json
import os

class Database:
    def __init__(self):
        self.db_file = 'players.json'
        self.create_db_if_not_exists()

    def create_db_if_not_exists(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as file:
                json.dump({}, file)

    def player_exists(self, username):
        with open(self.db_file, 'r') as file:
            data = json.load(file)
            return username in data

    def add_player(self, username, password):
        with open(self.db_file, 'r') as file:
            data = json.load(file)
        
        data[username] = {
            'password': password,
            'rank': 'Bronze 5',
            'level': 1,
            'experience': 0,
            'gold': 100,
            'food': 50,
            'diamonds': 0,
            'achievements': []
        }

        with open(self.db_file, 'w') as file:
            json.dump(data, file)

    def verify_credentials(self, username, password):
        with open(self.db_file, 'r') as file:
            data = json.load(file)
            return data.get(username, {}).get('password') == password

    def get_player_profile(self, username):
        with open(self.db_file, 'r') as file:
            data = json.load(file)
            return data.get(username, {})
        
    def get_top_players(self):
        with open(self.db_file, 'r') as file:
            data = json.load(file)
            players = [{"username": k, "level": v["level"], "rank": v["rank"]} for k, v in data.items()]
            return sorted(players, key=lambda x: x['level'], reverse=True)
