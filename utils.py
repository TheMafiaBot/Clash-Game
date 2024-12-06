import random

def generate_random_reward():
    return {
        'gold': random.randint(50, 500),
        'diamonds': random.randint(5, 100)
    }
