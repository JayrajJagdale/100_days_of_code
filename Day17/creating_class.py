class User:
    def __init__(self,user_id,username):
        self.user_id = user_id
        self.username = username
        self.follower  = 0
        self.following = 0
    
    def follow(self, user):
        user.follower += 1
        self.following += 1

user_1 = User("001","Jay")
user_2 = User("002","Angela")

user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)     

 # user_1 = User("001","Jay")
# print(user_1.user_id)
# print(user_1.follower)

# user_1.id ="001"
# user_1.name = "Jay"
# print(user_1.name)

# user_2 = User()
# user_2.id = "002"
# user_2.name = "angela"