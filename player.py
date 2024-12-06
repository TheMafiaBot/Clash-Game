import json
import os
from database import Database

class Player:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.database = Database()
        self.profile = {}

    def register(self):
        if not self.database.player_exists(self.username):
            self.database.add_player(self.username, self.password)
            print("Registration successful!")
            self.login()
        else:
            print("Player already exists. Please log in.")
            self.login()

    def login(self):
        if self.database.verify_credentials(self.username, self.password):
            print("Login successful!")
            self.profile = self.database.get_player_profile(self.username)
        else:
            print("Invalid credentials, please try again.")
            self.register()

    def view_profile(self):
        print(f"\nPlayer: {self.username}")
        print(f"Rank: {self.profile['rank']}")
        print(f"Level: {self.profile['level']}")
        print(f"Experience: {self.profile['experience']}")
        print(f"Resources: Gold={self.profile['gold']} Food={self.profile['food']} Diamonds={self.profile['diamonds']}")
        print(f"Completed Achievements: {', '.join(self.profile['achievements'])}")
