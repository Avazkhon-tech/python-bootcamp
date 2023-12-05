# enemies = 1
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


# # local scope
# def drink_postion():
#     position_strength = 2
#     print(position_strength)
#
# drink_postion()
# print(postion_strength)



# # Global scope
# player_health = 10
#
# def game():
#     def drink_postion():
#         position_strength = 2
#         print(position_strength)
#     drink_postion()
#
# print(player_health)


# #  there is no block scope
# # game_level = 3
# # def create_enemy():
# #     enemies = ["Skeleton", "Zombie", "Alien"]
# #     if game_level < 5:
# #         new_enemy = enemies[0]
# #     print(new_enemy)
# #
# # create_enemy()


# # Modifying global scope
# enemies = 0
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Global constants
# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@yu_angela"













