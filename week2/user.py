class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_cards_points = 0


    def display_info(self):
        print(f'First name: {self.first_name}')
        print(f'Last name: {self.last_name}')
        print(f'Email: {self.email}')
        print(f'Age: {self.age}')
        print(f'Rewards Member: {self.is_rewards_member}')
        print(f'Gold cards points: {self.gold_cards_points}')

    def enroll(self):
        if self.is_rewards_member:
            print('User already a member.')
            return False
        else:
            self.is_rewards_member = True
            self.gold_cards_points = 200
            return True


    def spend_points(self, amount):
        if self.gold_cards_points >= 0:
            self.gold_cards_points -= amount
        else:
            print('Not enough points to spend!')


user1 = User("Ross", "Geller", "rossgeller@gmail.com", 30 )
user2 = User("Joy", "Baker", "j.baker@gmail.com", 28)


user1.spend_points(50)
user2.enroll()
user2.spend_points(80)
user1.display_info()
user2.display_info()