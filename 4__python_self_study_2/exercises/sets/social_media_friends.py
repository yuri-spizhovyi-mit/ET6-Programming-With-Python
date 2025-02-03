"""Social Media Friend Suggestions
Find mutual friends between two users"""

user_A_friends = {"Alice", "Bob", "Charlie"}
user_B_friends = {"Charlie", "Dave", "Eve"}

mutual_friends = user_A_friends.intersection(user_B_friends)

print("Mutual friends: ", mutual_friends)
