import time
from player import Player
from game_mechanics import GameMechanics
from ranking import Ranking

def print_banner():
    print("""
    *******************************
    *                             *
    *      WELCOME TO EMPIRE      *
    *           CLASH            *
    *                             *
    *******************************
    """)

def main():
    print_banner()
    
    action = input("Do you want to Register (R) or Login (L)? ").lower()
    
    if action == 'r':
        username = input("Enter username: ")
        password = input("Enter password: ")
        player = Player(username, password)
        player.register()
    elif action == 'l':
        username = input("Enter username: ")
        password = input("Enter password: ")
        player = Player(username, password)
        player.login()
    else:
        print("Invalid input. Please restart the game.")
        return

    game_mechanics = GameMechanics(player)
    ranking = Ranking(player)
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Play Game")
        print("2. View Profile")
        print("3. View Leaderboard")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            game_mechanics.play()
        elif choice == '2':
            player.view_profile()
        elif choice == '3':
            ranking.show_leaderboard()
        elif choice == '4':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
