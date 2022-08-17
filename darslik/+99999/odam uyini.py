# import random
# stages   = ["""
#   +---+
#   |   |
#   o   |
#  /|\  |
#  / \  |
#       |
# ==========afsuz  siz qoldingiz :
# """, """
#   +---+
#   |   |
#   o   |
#  /|\  |
#  /    |
#       |
# ==========
# """, """
#   +---+
#   |   |
#   o   |
#  /|\  |
#       |
#       |
# ==========
# """, """
#   +---+
#   |   |
#   o   |
#  /|   |
#       |
#       |
# ==========
# """, """
#   +---+
#   |   |
#   o   |
#   |   |
#       |
#       |
# ==========
# """, """
#   +---+
#   |   |
#   o   |
#       |
#       |
#       |
# ==========
# """, """
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# ==========
# """]
#
# words = ['lola', 'banan', 'book']
# tsoz = random.choice(words)
#
# word_len = len(tsoz)
# display = []
# for _ in range(word_len):
#     display += "_"
# print(display)
#
# gameover = True
# jon = 6
#
# while gameover:
#     ksoz = input('So`z kiriting<>: ').lower()
#     for orni in range(word_len):
#         harf = tsoz[orni]
#         if ksoz == tsoz[orni]:
#             display[orni] = harf
#
#     print(f"{' '.join(display)}")
#
#     if "_" not in display:
#         gameover = False
#         print('You Win! | Siz yutdingiz!')
#
#     if ksoz not in tsoz:
#         jon -= 1
#         if jon == 0:
#             gameover = False
#             print("You Lose!")
#     print(stages[jon])
# #
# """so`z uyini 2"""
#
# import random
#
# words = ['lola', 'banan', 'book','maktab']
# tsoz = random.choice(words)
#
#
# display = []
# for _ in range(len(tsoz)):
#     display += "_"
# print(display)
# gameover = True
# jon = 3
# while gameover:
#     ksoz = input('so`z uyini kirit so`z: ').lower()
#     for orni in range(len(tsoz)):
#         harf = tsoz[orni]
#         if ksoz == tsoz[orni]:
#             display[orni] = harf
#
#
#     print(f"{' '.join(display)}")
#
#
#     if ksoz not in tsoz:
#         jon -= 1
#         if jon == 0:
#             gameover = False
#             print("You Lose!aka qoldizu")