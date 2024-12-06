import json
from database import Database

class Ranking:
    def __init__(self, player):
        self.player = player
        self.database = Database()

    def show_leaderboard(self):
        leaderboard = self.database.get_top_players()
        print("\n--- Leaderboard ---")
        for rank, player in enumerate(leaderboard, 1):
            print(f"Rank {rank}: {player['username']} - Level {player['level']} - Rank {player['rank']}")

    def update_rank(self):
        # Dummy rank progression logic
        rank_thresholds = ['Bronze', 'Silver', 'Gold', 'Diamond', 'Crown', 'Ace', 'Conqueror']
        self.player.profile['rank'] = rank_thresholds[self.player.profile['level'] // 10]
