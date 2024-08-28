class User:
    def __init__(self, user_id, user_name): # Initialize attributes
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1 #following another user object
        self.following += 1


user_1 = User("001", "Nasir")
user_2 = User("002", "Tanvir")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)