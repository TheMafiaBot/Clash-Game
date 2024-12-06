import random
from utils import generate_random_reward

class GameMechanics:
    def __init__(self, player):
        self.player = player

    def play(self):
        print("\nYou are now playing the game...")
        self.complete_challenge()
        self.battle()

    def complete_challenge(self):
        # Random daily challenge generation
        challenges = ['Farm 100 Gold', 'Win 2 Battles', 'Complete 5 Defenses']
        challenge = random.choice(challenges)
        print(f"Your challenge for today: {challenge}")
        reward = generate_random_reward()
        self.player.profile['diamonds'] += reward['diamonds']
        self.player.profile['gold'] += reward['gold']
        print(f"You earned: {reward['gold']} Gold, {reward['diamonds']} Diamonds as reward!")

    def battle(self):
        print("\nYou are now in a battle with another player!")
        result = random.choice(['win', 'lose'])
        if result == 'win':
            print("You won the battle!")
            self.player.profile['gold'] += 200
        else:
            print("You lost the battle.")
            self.player.profile['food'] -= 50
