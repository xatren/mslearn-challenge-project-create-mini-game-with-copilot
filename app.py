import random

def get_user_choice():
    user_input = input("Seçiminizi yapın (taş, kağıt, makas): ").lower()
    while user_input not in ['taş', 'kağıt', 'makas']:
        user_input = input("Geçersiz seçim. Lütfen tekrar deneyin (taş, kağıt, makas): ").lower()
    return user_input

def get_computer_choice():
    return random.choice(['taş', 'kağıt', 'makas'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Berabere!"
    elif (user_choice == 'taş' and computer_choice == 'makas') or \
         (user_choice == 'kağıt' and computer_choice == 'taş') or \
         (user_choice == 'makas' and computer_choice == 'kağıt'):
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"

def play_game():
    wins = 0
    rounds = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Sizin seçiminiz: {user_choice}")
        print(f"Bilgisayarın seçimi: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "Kazandınız!":
            wins += 1
        rounds += 1
        
        play_again = input("Tekrar oynamak ister misiniz? (e/h): ").lower()
        if play_again != 'e':
            break
    
    print(f"Oyun bitti! Toplam kazandığınız oyun sayısı: {wins}, Toplam oynanan tur sayısı: {rounds}")

if __name__ == "__main__":
    play_game()