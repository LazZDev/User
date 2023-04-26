# Creating a file with the User class, including the __init__ with all the attributes, parameters and default values.

class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

# Adding the display_info(self) method to the User class

    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Rewards Member:", self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points)

# Adding the enroll method to the User class

    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("User is already a member.")

# Adding the spend_points(self, amount) method

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print("Insufficient points.")


# Creating a user instance and calling the display_info method
user1 = User("Laz", "Dev", "laz.dev@example.com", 30)
user1.display_info()
print()

# Enrolling the user and testing by calling the method on the user in the outer scope
user1.enroll()
user1.display_info()
print()

# Creating two more instances of the User class
user2 = User("Ana", "Nur", "ana.nur@example.com", 25)

# Having the first user spend 50 points
user1.spend_points(50)

# Having the second user enroll
user2.enroll()

# Having the second user spend 80 points
user2.spend_points(80)

# Calling the display_info method on all users
user1.display_info()
print()
user2.display_info()
print()
