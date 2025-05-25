from deck import Deck
from player import Player
from storage import save_game, load_game

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("You")
        self.dealer = Player("Dealer")
        load_game(self.player)

    def start_round(self):
        self.deck = Deck()  
        self.player.clear_hand()
        self.dealer.clear_hand()
        print(f"💰 Your current score: {self.player.score}")
        print(f"🏅 Your medals: {self.player.medals}")
        while True:
            try:
                bet = int(input("Enter your bet amount: "))
                if 0 < bet <= self.player.score:
                    self.player.current_bet = bet
                    break
                else:
                    print("Invalid bet. Must be between 1 and your current score.")
            except ValueError:
                print("Please enter a valid number.")


        for _ in range(2):
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

        print("\nYour hand:")
        for card in self.player.hand:
            print(card)
        print("Total:", self.player.get_total())

        print("\nDealer shows:")
        print(self.dealer.hand[0])  


        while self.player.get_total() < 21:
            move = input("Hit or Stand? (h/s): ").lower()
            if move == 'h':
                self.player.add_card(self.deck.deal_card())
                print("You drew:", self.player.hand[-1])
                print("Total:", self.player.get_total())
                if self.player.get_total() > 21:
                    print("You bust! 💥")
                    self.player.score -= self.player.current_bet
                    self.player.losses += 1
                    print(f"💳 Current score: {self.player.score}")
                    return
            elif move == 's':
                break
            else:
                print("Invalid input.")

        print("\nDealer's turn:")
        for card in self.dealer.hand:
            print(card)
        while self.dealer.get_total() < 17:
            new_card = self.deck.deal_card()
            self.dealer.add_card(new_card)
            print("Dealer drew:", new_card)


        print("\n--- Final Hands ---")
        print("You:", [str(c) for c in self.player.hand], "→", self.player.get_total())
        print("Dealer:", [str(c) for c in self.dealer.hand], "→", self.dealer.get_total())


        p_total = self.player.get_total()
        d_total = self.dealer.get_total()

        if d_total > 21 or p_total > d_total:
            print("✅ You win!")
            self.player.score += self.player.current_bet
            self.player.wins += 1
        elif p_total < d_total:
            print("❌ You lose.")
            self.player.score -= self.player.current_bet
            self.player.score = max(0, self.player.score)
            self.player.losses += 1
        else:
            print("🤝 It's a draw.")
            self.player.draws += 1
        print(f"💳 Current score: {self.player.score}")
        score = self.player.score
        medals = self.player.medals

        if score >= 500 and "Gold" not in medals:
            medals.append("Gold")
            print("🥇 You've unlocked the Gold Medal!")
        elif score >= 300 and "Silver" not in medals:
            medals.append("Silver")
            print("🥈 You've unlocked the Silver Medal!")
        elif score >= 200 and "Bronze" not in medals:
            medals.append("Bronze")
            print("🥉 You've unlocked the Bronze Medal!")
    
    def play(self):
        print("🎮 Welcome to Blackjack Royale!")
        print(f"💳 Restored score: {self.player.score}")
        print(f"🏅 Your medals: {self.player.medals}")
        print(f"📊 Record: {self.player.wins}W / {self.player.losses}L / {self.player.draws}D")
        if self.player.score == 0:
            print("😵 Your score is 0. You're broke!")
            choice = input("🌱 Do you want to reset and start a new game? (y/n): ").lower()
            if choice == 'y':
                self.player = Player("You")  # 重置为新玩家
                print("🔁 Restarted game with fresh score!")
            else:
                print("❌ Exiting... No progress saved.")
                return
        while self.player.score > 0:
            self.start_round()

            again = input("🔁 Play another round? (y/n): ").lower()
            if again != 'y':
                break

        print("🏁 Game over. Final score:", self.player.score)
        print("🏅 Your medals:", self.player.medals)
        print(f"📊 Record: {self.player.wins}W / {self.player.losses}L / {self.player.draws}D")
        save_game(self.player)